# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: A90
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a duyệt **kế hoạch pilot**, trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra được quyết định. Mọi con số do `src/lab13.py` tính trên mẫu 1.200 yêu cầu / 1.624 lần chạy (dữ liệu giả lập); số từ cột `_simulated` ghi nhãn **simulated**. Vai đổi sau giải lao: Thành viên 1 viết code CP1–CP2, Thành viên 2 viết code CP4–CP5.

## 3. Giải pháp

- **A · Chi phí** ([bang_chi_phi.md](bang_chi_phi.md)): tử số cộng token + tool của mọi lần chạy (kể cả lỗi) và phút xem lại / làm lại; mẫu số chỉ đếm `ket_qua == 'thanh_cong'`. Tách theo `loai`, cộng chi phí cố định 40 triệu đ/tháng cho noi_dia + hang_nang.
- **B · Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): gọi lại `mo_hinh` cho 9 kịch bản, 1 cặp, giới hạn 1/2/3 lần chạy và kịch bản xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): hai người gắn nhãn độc lập 20 ca theo 5 loại Google PAIR, so nhãn, viết quy tắc cho ca lệch, bảng khắc phục 5 ca.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): tính đủ 5 câu D1 trước khi chọn cách chia; chọn chia theo nhân viên 20 + 20; 3 luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ.
- **E · Chỉ số và hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): 3 chỉ số tính thử, ≥ 6 event có `trace_id`, ≥ 2 dòng rủi ro kinh tế, hồ sơ 7 mục.

## 4. Kết quả

- Ba phép thử A1: ĐẠT (1,20 · 1,25 · 1,25).
- Chi phí mỗi việc thành công **4.472 đ** = 0,37× so với 12.000 đ, gấp 16,3× hoá đơn token chia số yêu cầu; 92,5% là giờ nhân viên **[simulated]**.
- Theo loại: noi_dia 0,22× · hang_nang 0,69× · doi_tac 0,85× · quoc_te 1,88× **[simulated]** → thu hẹp phạm vi pilot về noi_dia + hang_nang (4.599 đ = 0,38× sau khi cộng cố định).
- Ba yếu tố nhạy nhất: làm lại ×2 (+51,8%), xem lại ×2 (+40,7%), lương +25% (+23,1%) **[simulated]**. Xem lại 100% đẩy lên 11.743 đ = 0,98× **[simulated]**.
- Chỉ số trong đợt chạy thử: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%.
- Pilot: chia theo nhân viên 20 + 20, mde 6 điểm (859/nhóm, DE 6,96); power 0,64 nếu tác động thật 5 điểm.
- Đồng thuận gắn nhãn CP3: 16 / 20 (80%).
- **Đề xuất cuối: Go có điều kiện** (4 điều kiện, xem `ho_so_launch_v0.md`).
- Kết quả duyệt chéo nhóm nhận được từ hội đồng: ... / 30, quyết định ...

## 5. Khó khăn và cách xử lý

- Máy Thành viên 4 chưa có `pandas` (`ModuleNotFoundError: No module named 'pandas'` khi chạy `python3 lab13.py`). Xử lý: tạo `src/.venv`, `pip install -r requirements.txt`, chạy lại thì ba phép thử in ĐẠT; đây cũng là lần chạy kiểm tra trên máy thứ hai.
- Không cách chia theo cụm nào đủ mẫu cho mức chênh 5 điểm với 40 nhân viên: nhóm chấp nhận mde 6 điểm và ghi rõ power 0,64 trong hồ sơ.
- ...

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

### Bàn giao Thành viên 2 — Vũ Văn Chủ (2A202603873, chur04)

- Hoàn tất [bảng chi phí A–B](bang_chi_phi.md), gồm phép tính đối chiếu và nhãn `simulated`: 4.472 đ/việc thành công, chi phí cả hệ thống 5.865 đ/yêu cầu; giới hạn 2 lần chạy rẻ nhất cả hệ thống ở 6.901.220 đ [simulated].
- Tiếp nhận code D1/E1 có sẵn của Thành viên 1, bổ sung kết quả có thể kiểm tra và hoàn tất [kế hoạch pilot](pilot_plan.yaml): 20 cụm/nhóm, tối thiểu 299 yêu cầu/nhân viên, 5.980 yêu cầu thô/nhóm, MDE 6 điểm; power chỉ khoảng 0,64 nếu tác động thật 5 điểm.
- Bàn giao [ba chỉ số E1](chi_so.md): 82,83% (994/1.200), 27,12% (48/177), 4,25% (51/1.200); mở lại trong phạm vi 3,97% (39/982). Toàn bộ dữ liệu lab là giả lập, chưa có đối chứng để kết luận cải thiện.
- Python mặc định 3.15 thiếu thư viện; đã tạo `.venv` bằng Python 3.12 và cài `src/requirements.txt`, chạy code hết và kiểm YAML. Môi trường `.venv` được Git bỏ qua.
- Kế hoạch đề xuất bắt đầu 30/11/2026, thu mẫu chính 14–27/12, theo dõi đến 03/01/2027, quyết định 04/01/2027; các ngày và ngưỡng chưa phải kết quả đã thực hiện. Hồ sơ nhóm, nhãn độc lập và duyệt chéo vẫn cần các thành viên phụ trách hoàn thiện.

Bằng chứng và khai báo hỗ trợ AI: [báo cáo cá nhân Vũ Văn Chủ](2A202603873_VuVanChu.md). Phần này chỉ tổng hợp đóng góp Thành viên 2; Thành viên 4 tiếp tục hoàn thiện toàn bộ báo cáo nhóm và đề xuất cuối.

## 7. Hạn chế và hướng cải thiện

- 92,5% chi phí dựa trên phút xem lại / làm lại **simulated**; cần đo phút thật bằng event `staff_review_decision`, `staff_rework_completed` từ tuần 1 pilot.
- Đợt chạy thử không có nhóm đối chứng nên chưa nói được trợ lý đã nâng chỉ số; pilot có đối chứng mới trả lời được.
- Power 0,64 ở mức 5 điểm: nếu tác động thật nhỏ, pilot có thể không kết luận được; cân nhắc kéo dài pilot để tăng m mỗi nhân viên.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure"
- Tài liệu statsmodels, `NormalIndPower` (mục `stats.power`)
- `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`
