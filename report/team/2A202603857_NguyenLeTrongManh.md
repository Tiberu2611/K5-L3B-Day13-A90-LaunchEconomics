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
- Chưa làm tại thời điểm viết: tính tay D1, kiểm tra cuối trên máy thứ hai.

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

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code (Anthropic).
- **Dùng vào việc:** tóm tắt đề, xử lý lỗi môi trường Python, viết `src/lab13.py`, thao tác Git, soạn mục E2, phần đóng góp trong `TEAM.md` và bản nháp báo cáo này. A1, `mo_hinh` và `co_mau` bám sát code mẫu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- **Kiểm tra tự động:** ba phép thử A1; assert "giảm một nửa" bằng nửa mức tăng "gấp đôi"; assert tác động của cặp B2 bằng tổng hai tác động riêng; Claude đối chiếu kết quả in ra với số trong hướng dẫn.
- **Tôi tự kiểm tra:** [Mạnh điền: đã tính tay con số nào, kết quả bao nhiêu]

## 6. Tự đánh giá

[Mạnh điền: phần làm tốt, phần còn yếu, điều học được]
