# Báo cáo cá nhân — NguyenLeTrongManh-2A202603857

## 1. Thông tin thành viên

- Họ tên: Nguyễn Lê Trọng Mạnh
- MSSV: 2A202603857
- Email: manh025011@gmail.com
- Vai trong nhóm: Người viết code (Ca 1) → Người kiểm số & QA (Ca 2)

## 2. Phần việc phụ trách

- CP1, CP2: `src/lab13.py`, nhiệm vụ A1–A4 và B1–B4.
- CP3: cùng Thành viên 2 hoàn thiện câu trả lời B3, B4 và bàn giao code.
- CP4, CP5: tính tay kiểm chứng D1, viết mục E2, kiểm tra cuối trước khi nộp.

## 3. Đóng góp cụ thể

- **A:** ba hàm A1 và `mo_hinh`. Chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ). Cộng chi phí cố định trong phạm vi pilot: 4.599 đ = 0,38× [simulated].
- **B:** chín kịch bản độ nhạy. Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%) [simulated].
- **E2:** ba dòng rủi ro kinh tế trong `chi_so.md`, số lấy từ A4, B1, B4.
- File cũng in sẵn D1 và E1 để Thành viên 2 kiểm tra và tiếp nhận.
- **D1 (tính tay kiểm chứng):** hoàn thành tính tay 5 câu cỡ mẫu a–e khớp với `src/lab13.py` (1.251/nhóm; 3.103/nhóm → 84 người > 40; trần 1.000; trần 300; m ≥ 299 với DE = 6,96 cho mức chênh 6 điểm).
- **Kiểm tra cuối (chạy với Claude Code, trước duyệt chéo):** `lab13.py` chạy hết, A1 ĐẠT; `pilot_plan.yaml` đọc được, không còn dấu hỏi, 4 luật dừng đủ bốn vế; `report/team` không có từ bị cấm; hai CSV và file gốc không bị sửa. Các điểm lệch phát hiện được (ví dụ ca 17 trong bảng khắc phục khác nhãn thống nhất) thuộc file của thành viên khác, chưa sửa tại thời điểm viết; `phieu_cham.md` chờ duyệt chéo.

## 4. Bằng chứng

| Việc | Bằng chứng |
| --- | --- |
| Code A, B | Commit `5e09dc7`, gộp vào `main` qua PR #1 (`548aa34`) |
| A1 | `python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` |
| A2 | Tổng 4.373.585 đ ÷ 978 việc thành công = 4.472 đ [simulated] |
| B1 | Làm lại gấp đôi: 6.787 đ; giảm một nửa: 3.315 đ [simulated] |
| B3 | Giới hạn 2 lần rẻ nhất cả hệ thống: 6.901.220 đ [simulated] |
| B4 | 11.743 đ (làm lại 9 phút), 12.415 đ (làm lại 15,3 phút) [simulated] |
| E2 | `report/team/chi_so.md`, mục E2 |
| Tính tay A1, D1 | Mục 5 của báo cáo này |

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code (Anthropic).
- **Dùng vào việc:** tóm tắt đề, xử lý lỗi môi trường Python, viết `src/lab13.py`, thao tác Git, soạn mục E2, phần đóng góp trong `TEAM.md` và bản nháp báo cáo này. A1, `mo_hinh` và `co_mau` bám sát code mẫu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- **Kiểm tra tự động:** ba phép thử A1; assert "giảm một nửa" bằng nửa mức tăng "gấp đôi"; assert tác động của cặp B2 bằng tổng hai tác động riêng; Claude đối chiếu kết quả in ra với số trong hướng dẫn.
- **Tôi tự kiểm tra:**
  - Tự tính tay lại 3 phép thử A1 (`p = 0,8`): `k=2` ra `1,20`; `k=∞` ra `1,25`; `k=3` ra `1,24 / 0,992 = 1,25`.
  - Tự tính tay toàn bộ 5 câu D1: câu (a) `1.250` yêu cầu/nhóm với z làm tròn, code ra `1.251` (lệch dưới 0,1%); câu (b) `DE = 1 + 74 × 0,02 = 2,48` → `3.103` yêu cầu/nhóm (`84 > 40` người); câu (c) trần `20 / 0,02 = 1.000`; câu (d) trần `6 / 0,02 = 300`; câu (e) giải `20m / (0,98 + 0,02m) ≥ 859` → `2,82m ≥ 841,82` → `m ≥ 299` yêu cầu/người (`DE = 6,96`), khớp trong sai số làm tròn với hàm `in_d1()` trong `src/lab13.py`.

## 6. Tự đánh giá

- **Phần làm tốt:** Hoàn thành sớm và đầy đủ phần code mô hình chi phí (`src/lab13.py`), với hỗ trợ của Claude Code, cho cả A, B, D1, E1 và phần rủi ro kinh tế E2 đúng chuẩn quy tắc (đủ nhãn `simulated`, không dùng từ bị cấm theo quy tắc 5), giúp nhóm có số liệu chuẩn để triển khai các bước sau.
- **Phần còn yếu:** Ban đầu chưa nắm sâu ý nghĩa thống kê của các công thức (như cỡ mẫu hiệu dụng khi chia cụm, nghịch lý tối ưu cục bộ ở B3) nên cần kiểm tra và tính tay lại để hiểu bản chất phục vụ bảo vệ trước hội đồng.
- **Điều học được:** Chi phí thật của AI agent nằm phần lớn ở thời gian con người xem lại và làm lại (chiếm 92,5% tổng chi phí [simulated]), không phải tiền token; khi thiết kế pilot theo cụm (nhân viên/depot), số cụm quyết định trần cỡ mẫu hiệu dụng chứ không phải tổng số yêu cầu.
