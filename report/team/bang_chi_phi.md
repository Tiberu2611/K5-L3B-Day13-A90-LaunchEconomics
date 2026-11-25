# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 — ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 — ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 — ĐẠT |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv`, mọi lần chạy | đo từ trace |
| Tool | 84.000 | 5.600 lần gọi × 15 đ | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1; đã nằm trong token + tool | đo từ trace |
| Xem lại | 1.780.000 | 890 phút `phut_xem_lai_simulated` × 2.000 đ | simulated |
| Làm lại | 2.264.000 | 1.132 phút `phut_lam_lai_simulated` × 2.000 đ | simulated |
| Tổng chi phí | 4.373.585 | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 việc | `ket_qua == 'thanh_cong'` | đếm từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 | Tổng ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,3 lần** hoá đơn chia số yêu cầu [simulated]; tử số tính cả lần lỗi, mẫu số chỉ tính 978 việc thành công.
- Khoản lớn nhất là **làm lại: 51,8%**; xem lại 40,7%, tổng giờ nhân viên 92,5% chi phí [simulated].

Khi so chi phí toàn công ty với nhân viên tự làm: (4.373.585 + 222 × 12.000) ÷ 1.200 = **5.865 đ/yêu cầu = 0,49×** [simulated], chưa cộng cố định; 222 gồm 74 ca làm lại và 148 ca chuyển nhân viên theo quy ước B3 của lab.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% (783/824) | 1,11 | 2.696 đ [simulated] | 0,22× [simulated] |
| hang_nang | 158 | 74,1% (117/158) | 1,47 | 8.221 đ [simulated] | 0,69× [simulated] |
| quoc_te | 150 | 27,3% (41/150) | 2,32 | 22.515 đ [simulated] | 1,88× [simulated] |
| doi_tac | 68 | 54,4% (37/68) | 1,88 | 10.215 đ [simulated] | 0,85× [simulated] |

- `quoc_te`: 22.515 đ = 1,88× [simulated], thành công 27,3%; tỉ lệ `ok` lần 1/2/3 là 30,0%/11,4%/2,2%, nên chạy lại đến 3 lần giúp rất ít. Pilot chỉ nhận `noi_dia` + `hang_nang`; `doi_tac` cũng loại vì 0,85× [simulated], thành công 54,4% và có điều khoản riêng.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× [simulated] |
| Một nửa khối lượng (22.500 yêu cầu/tháng) | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× [simulated] |

- Với 45.000 hoặc 22.500 yêu cầu/tháng, cộng 40 triệu đ cố định vẫn dưới 12.000 đ/việc [simulated]; dưới khoảng **6.212 yêu cầu/tháng** thì chỉ tiêu A4 vượt 12.000 đ [simulated], nếu cơ cấu và năng suất giữ nguyên.

A4 dùng 900 việc thành công trong phạm vi trên **1.200 yêu cầu toàn mẫu** để suy ra 33.750 việc/tháng; chi phí biến đổi trong phạm vi là 3.072.513 ÷ 900 = 3.414 đ [simulated]. Đây là chi phí mỗi việc trợ lý thành công, chưa cộng phần nhân viên làm thay như B3.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ attempt > 2; yêu cầu có so_lan_chay > 2 chuyển nhân viên, phút xem lại/làm lại = 0 | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

Toàn bộ chi phí và thay đổi ở B1 là **simulated**, so với gốc A2 chưa làm tròn: 4.471,968 đ; giữ nguyên mẫu số trừ hai kịch bản giới hạn chạy.

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%) [simulated]**; mức tăng bằng tổng hai tác động riêng vì chi phí cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: **1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%) [simulated]**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

Các cột tiền B3 đều **simulated**, chưa cộng cố định; chi phí cả hệ thống = tổng trợ lý + 12.000 × số yêu cầu không thành công, theo quy ước của đề.

- **2 lần** rẻ nhất cho công ty: 6.901.220 đ [simulated]; chi phí mỗi việc thấp nhất ở **1 lần**: 4.111 đ [simulated], nhưng đẩy thêm 85 yêu cầu sang nhân viên so với 2 lần (97 so với 3 lần).

## B4 · Nếu phải xem lại tất cả

- Xem lại 948 yêu cầu chạy `ok` × 5 phút, 48 ca làm lại × 9 phút: **11.743 đ = 0,98×**; thay bằng 15,3 phút/ca làm lại: **12.415 đ = 1,03×** [simulated], chưa cộng cố định.
- Pilot cần tìm mức xem lại thấp nhất vẫn an toàn; hoà vốn cần ≤ **5,12 phút** (làm lại 9 phút) hoặc ≤ **4,80 phút** (15,3 phút) mỗi lần xem [simulated], rồi thay phút giả lập bằng số đo thật.

## Đối chiếu số học · Người kiểm số: Vũ Văn Chủ — 2A202603873

Các phép tính dưới đây được Codex tính lại từ CSV và đối chiếu code; là cách tính minh bạch để thành viên tự kiểm lại, không xác nhận đã có buổi kiểm tay hay chữa bài tại lớp. Dữ liệu gốc đều giả lập; nhãn “đo từ trace” chỉ phân biệt nguồn trong bộ dữ liệu lab.

| Mục | Phép tính đối chiếu | Kết quả |
| --- | --- | --- |
| A1 | (1 − 0,2²)/0,8; 1/0,8; [(1 − 0,2³)/0,8]/(1 − 0,2³) | 1,20; 1,25; 1,25 |
| A2 | 5.771.712/1.000 × 26 + 734.774/1.000 × 130 = 245.585,132; cộng 84.000 + 890 × 2.000 + 1.132 × 2.000, chia 978 | 4.471,968 đ → 4.472 đ [simulated] |
| A3 | 783 + 117 + 41 + 37 = 978; 824 + 158 + 150 + 68 = 1.200 | Khớp cả thành công và số yêu cầu A2 |
| A4 | 45.000 × 900/1.200 = 33.750; 3.072.513/900 + 40.000.000/33.750 | 4.599 đ; còn nửa khối lượng: 5.784 đ [simulated] |
| B1 | Gấp đôi làm lại: (4.373.585 + 2.264.000)/978; giảm nửa: (4.373.585 − 1.132.000)/978 | 6.787 đ (+51,8%); 3.315 đ (−25,9%) [simulated] |
| B2 | (4.373.585 + 245.585 + 1.780.000)/978 | 6.543 đ (+46,3%) [simulated] |
| B3 | 4.093.220 + 234 × 12.000 | 6.901.220 đ [simulated], nhỏ nhất ba giới hạn |
| B4 | (224.513 + 948 × 5 × 2.000 + 48 × 9 × 2.000)/900 | 11.743 đ [simulated]; dùng 15,3 phút: 12.414,79 → 12.415 đ |

Nguồn: `src/lab13.py`, hai CSV và `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; tính với số chưa làm tròn, trình bày tiền nguyên đồng. Hướng dẫn có dòng B4 ghi 12.414 đ; tính lại và làm tròn đúng ra 12.415 đ (sai khác dưới 0,01%).
