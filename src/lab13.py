"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; phần power ở Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
from statistics import NormalDist

import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000           # đồng chi phí cố định của trợ lý mỗi tháng
YEU_CAU_THANG = 45_000               # số yêu cầu mỗi tháng ở quy mô đầy đủ
PHAM_VI = ['noi_dia', 'hang_nang']   # phạm vi pilot


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1/p if k is None else (1-(1-p)**k)/p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k)/ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict chi phí; cps = chi phí mỗi việc thành công.
    - token, tool: cộng trên MỌI lần chạy, kể cả lần lỗi. chay_lai đã nằm trong token + tool.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Số GIẢ LẬP, ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # Yêu cầu cần nhiều lần chạy hơn giới hạn: chuyển nhân viên, không còn phút xem lại/làm lại.
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    token, tool = tien_token.sum(), tien_tool.sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=token, tool=tool,
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong, thanh_cong=thanh_cong,
                cps=tong / thanh_cong if thanh_cong else math.inf,
                hoa_don_moi_yc=(token + tool) / len(reqs))


def in_a2(runs, reqs):
    print('\n=== A2 · Mô hình chi phí từ trace ===')
    r = mo_hinh(runs, reqs)
    phut_xem = reqs['phut_xem_lai_simulated'].sum()
    phut_lam = reqs['phut_lam_lai_simulated'].sum()
    for ten, gia_tri, nhan in [
        ('Token (mọi lần chạy)', r['token'], 'đo từ trace'),
        (f"Tool ({runs['tool_calls'].sum():,} lần gọi)", r['tool'], 'đo từ trace'),
        ('Trong đó, lần chạy thứ 2 và 3', r['chay_lai'], 'đo từ trace'),
        (f'Xem lại ({phut_xem:,.0f} phút)', r['xem_lai'], 'simulated'),
        (f'Làm lại ({phut_lam:,.0f} phút)', r['lam_lai'], 'simulated'),
        ('Tổng chi phí', r['tong'], 'có phần simulated'),
        ('Số việc thành công', r['thanh_cong'], 'đếm từ dữ liệu'),
        ('Chi phí mỗi việc thành công', r['cps'], 'simulated'),
    ]:
        print(f'{ten:40s} {gia_tri:>12,.0f}  [{nhan}]')
    print(f"{'Hoá đơn token + tool chia số yêu cầu':40s} {r['hoa_don_moi_yc']:>12,.1f}  [đo từ trace]")
    print(f"Gấp {r['cps'] / r['hoa_don_moi_yc']:.1f} lần hoá đơn; làm lại {r['lam_lai'] / r['tong']:.1%}, "
          f"xem lại {r['xem_lai'] / r['tong']:.1%}, giờ nhân viên "
          f"{(r['lam_lai'] + r['xem_lai']) / r['tong']:.1%} tổng chi phí [simulated]")
    khong_tc = len(reqs) - r['thanh_cong']
    he_thong = (r['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Cả hệ thống (cộng {khong_tc} ca nhân viên làm thay): {he_thong:,.0f} đ/yêu cầu '
          f'= {he_thong / BASELINE:.2f}× [simulated]')


def in_a3(runs, reqs):
    print('\n=== A3 · Tách theo loại yêu cầu ===')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        nhom = reqs[reqs['loai'] == loai]
        r = mo_hinh(runs, nhom)
        so_chay = runs['request_id'].isin(nhom['request_id']).sum() / len(nhom)
        print(f"{loai:10s} {len(nhom):5d} yêu cầu · thành công {r['thanh_cong'] / len(nhom):.1%} · "
              f"{so_chay:.2f} lần chạy/yêu cầu · {r['cps']:,.0f} đ = {r['cps'] / BASELINE:.2f}× [simulated]")
    print('Tỉ lệ ok theo lần thử:')
    gop = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    gop['ok'] = gop['status'] == 'ok'
    ok = gop.groupby(['loai', 'attempt'])['ok'].mean().unstack()
    for loai, dong in ok.iterrows():
        print(f'{loai:10s} ' + ' · '.join(f'lần {k}: {x:.1%}' for k, x in dong.items() if pd.notna(x)))


def in_a4(runs, reqs):
    print('\n=== A4 · Chi phí cố định (noi_dia + hang_nang) ===')
    r = mo_hinh(runs, reqs[reqs['loai'].isin(PHAM_VI)])
    viec_thang = YEU_CAU_THANG * r['thanh_cong'] / len(reqs)
    print(f"Chưa cộng cố định: {r['cps']:,.0f} đ [simulated]")
    for ten, ti_le in [('Quy mô đầy đủ', 1), ('Khối lượng một nửa', 0.5)]:
        co_dinh = CO_DINH_THANG / (viec_thang * ti_le)
        cps = r['cps'] + co_dinh
        print(f'{ten}: {viec_thang * ti_le:,.0f} việc/tháng · cố định {co_dinh:,.0f} đ/việc · '
              f'tổng {cps:,.0f} đ = {cps / BASELINE:.2f}× [simulated]')


# ---------- Nhiệm vụ B · Bảng độ nhạy ----------
KICH_BAN = {
    'Giá token gấp đôi': dict(gia_vao=GIA_VAO * 2, gia_ra=GIA_RA * 2),
    'Giá token giảm một nửa': dict(gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2),
    'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2),
    'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
    'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2),
    'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
    'Lương nhân viên tăng 25%': dict(luong_phut=LUONG_PHUT * 1.25),
    'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
    'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
}


def in_b1_b2(runs, reqs):
    print('\n=== B1 · Đổi từng yếu tố [simulated] ===')
    goc = mo_hinh(runs, reqs)['cps']
    print(f"{'Gốc (A2)':30s} {goc:>8,.0f} đ")
    doi = {}
    for ten, tham_so in KICH_BAN.items():
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        doi[ten] = cps / goc - 1
        print(f'{ten:30s} {cps:>8,.0f} đ  {doi[ten]:+.1%}')
    for ten in ['Giá token', 'Tỉ lệ xem lại', 'Số ca làm lại']:
        assert abs(doi[f'{ten} giảm một nửa'] * 2 + doi[f'{ten} gấp đôi']) < 1e-9, ten
    print('Tự kiểm tra "giảm một nửa" = nửa mức tăng "gấp đôi": ĐẠT')
    top3 = sorted(doi, key=doi.get, reverse=True)[:3]
    print('Xếp hạng: ' + ' · '.join(f'{i}. {t} ({doi[t]:+.1%})' for i, t in enumerate(top3, 1)))

    print('\n=== B2 · Đổi một cặp [simulated] ===')
    cps = mo_hinh(runs, reqs, gia_vao=GIA_VAO * 2, gia_ra=GIA_RA * 2, he_so_xem_lai=2)['cps']
    tong_rieng = doi['Giá token gấp đôi'] + doi['Tỉ lệ xem lại gấp đôi']
    assert abs(cps / goc - 1 - tong_rieng) < 1e-9, 'tác động của cặp phải bằng tổng hai tác động riêng'
    print(f'Token gấp đôi + xem lại gấp đôi: {cps:,.0f} đ ({cps / goc - 1:+.1%}) = tổng hai tác động riêng')


def in_b3(runs, reqs):
    print('\n=== B3 · Giới hạn số lần chạy [simulated] ===')
    for k in [1, 2, 3]:
        r = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - r['thanh_cong']
        print(f"Tối đa {k} lần: trợ lý {r['tong']:,.0f} đ · không thành công {khong_tc} · "
              f"cả hệ thống {r['tong'] + BASELINE * khong_tc:,.0f} đ · mỗi việc thành công {r['cps']:,.0f} đ")


def in_b4(runs, reqs, phut_xem=5):
    print('\n=== B4 · Xem lại 100% noi_dia + hang_nang [simulated] ===')
    nhom = reqs[reqs['loai'].isin(PHAM_VI)]
    chay = runs[runs['request_id'].isin(nhom['request_id'])]
    so_ok = chay.loc[chay['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((nhom['ket_qua'] == 'lam_lai').sum())
    r = mo_hinh(runs, nhom)
    may = r['token'] + r['tool']
    print(f"{len(nhom)} yêu cầu · {so_ok} có lần chạy ok · {so_lam_lai} ca làm lại · "
          f"{r['thanh_cong']} thành công · token + tool {may:,.0f} đ")
    # Đề cho 9 phút/ca làm lại; dữ liệu giả lập trung bình cao hơn nên tính cả hai.
    phut_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    for phut_lam in [9, round(phut_tb, 1)]:
        lam = so_lam_lai * phut_lam * LUONG_PHUT
        tong = so_ok * phut_xem * LUONG_PHUT + lam + may
        cps = tong / r['thanh_cong']
        hoa_von = (BASELINE * r['thanh_cong'] - lam - may) / (so_ok * LUONG_PHUT)
        print(f'Làm lại {phut_lam} phút/ca: tổng {tong:,.0f} đ · {cps:,.0f} đ = {cps / BASELINE:.2f}× · '
              f'hoà vốn khi xem lại ≤ {hoa_von:.2f} phút')


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Số yêu cầu mỗi nhóm để so hai tỉ lệ (hai phía)."""
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=0.02):
    return 1 + (m - 1) * icc


def tinh_d1(p0=0.70, icc=0.02, m=75, nhan_vien=40):
    """Ca 2: tiếp nhận D1, trả số để đối chiếu YAML; n là mẫu hiệu dụng mỗi nhóm."""
    n5, n6 = co_mau(p0, p0 + 0.05), co_mau(p0, p0 + 0.06)
    de = he_so_thiet_ke(m, icc)
    n_cum = math.ceil(n5 * de)
    nguoi = math.ceil(n_cum / m)
    cum = nhan_vien // 2
    if cum <= n6 * icc:
        raise ValueError('Số cụm không đủ cho mức chênh 6 điểm, dù tăng số yêu cầu mỗi cụm.')
    # 20m / (1 + (m − 1)·icc) ≥ n6  ⇔  m ≥ n6·(1 − icc) / (20 − n6·icc)
    m6 = math.ceil(n6 * (1 - icc) / (cum - n6 * icc))
    de6 = he_so_thiet_ke(m6, icc)
    pw = NormalIndPower().power(proportion_effectsize(p0 + 0.05, p0), n6, 0.05)
    return dict(n5=n5, n6=n6, de75=de, n_cum=n_cum, nguoi=nguoi,
                gioi_han_staff=cum / icc, gioi_han_depot=6 / icc,
                clusters_per_arm=cum, m6=m6, de6=de6, raw_per_arm=cum * m6,
                effective_per_arm=cum * m6 / de6, power_at_5=float(pw))


def in_d1():
    print('\n=== D1 · Cỡ mẫu (xấp xỉ theo công thức của lab) ===')
    d = tinh_d1()
    print(f"a · Theo yêu cầu, chênh 5 điểm: {d['n5']:,} mỗi nhóm")
    print(f"b · Theo nhân viên, m = 75: DE = {d['de75']:.2f} → {d['n_cum']:,} mỗi nhóm → "
          f"{d['nguoi']} người mỗi nhóm, tổng {2 * d['nguoi']} > 40: không đủ người")
    print(f"c · 20 nhân viên mỗi nhóm: hiệu dụng luôn < {d['gioi_han_staff']:,.0f} < {d['n5']:,}: không đạt")
    print(f"d · 6 depot mỗi nhóm: hiệu dụng luôn < {d['gioi_han_depot']:,.0f} < {d['n5']:,}: không đạt")
    print(f"e · Chênh 6 điểm ({d['n6']}/nhóm), 20 người mỗi nhóm: m ≥ {d['m6']} yêu cầu mỗi người "
          f"(DE {d['de6']:.2f})")
    print(f"Mẫu thô {d['raw_per_arm']:,}/nhóm → hiệu dụng {d['effective_per_arm']:.2f}/nhóm; "
          'chỉ tính ở bước 0.50, mọi yêu cầu được theo dõi đủ 7 ngày')
    print(f"Nếu tác động thật chỉ 5 điểm với n = {d['n6']}: power = {d['power_at_5']:.2f}")


# ---------- Nhiệm vụ D3, E1 · Chỉ số ----------
def tinh_chi_so(reqs):
    """Ca 2: đếm cả tử số/mẫu số E1 và D3, không dùng ket_qua thay chỉ số chính."""
    dat = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    mo_lai = reqs['mo_lai_trong_7_ngay'] == 1
    return {
        'chinh': (int(dat.sum()), len(dat)),
        'bo_qua': (int(bo_qua.sum()), len(bo_qua)),
        'an_toan': (int(mo_lai.sum()), len(mo_lai)),
        'an_toan_pham_vi': (int(mo_lai[reqs['loai'].isin(PHAM_VI)].sum()),
                           int(reqs['loai'].isin(PHAM_VI).sum())),
    }


def in_chi_so(reqs):
    print('\n=== D3 + E1 · Chỉ số trong đợt chạy thử (không có nhóm đối chứng) ===')
    chi_so = tinh_chi_so(reqs)
    for ten, key in [
        ('Chính: đóng trong 24h, không mở lại 7 ngày', 'chinh'),
        ('Dùng: bỏ qua gợi ý (sua + bo) / được xem lại', 'bo_qua'),
        ('An toàn: mở lại trong 7 ngày', 'an_toan'),
        ('An toàn, phạm vi noi_dia + hang_nang', 'an_toan_pham_vi'),
    ]:
        tu, mau = chi_so[key]
        ti_le = f'{tu / mau:.2%}' if mau else 'chưa có mẫu'
        print(f'{ten:46s} {ti_le} ({tu}/{mau})')


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')   # để Windows in được tiếng Việt
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_a2(runs, reqs)
    in_a3(runs, reqs)
    in_a4(runs, reqs)
    in_b1_b2(runs, reqs)
    in_b3(runs, reqs)
    in_b4(runs, reqs)
    in_d1()
    in_chi_so(reqs)
