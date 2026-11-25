# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Nhóm tự đề xuất: ... | ... | Không cần tính |
| An toàn | Nhóm tự đề xuất: ... | ... | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- ...

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công +51,8%, từ 4.472 đ lên 6.787 đ [simulated] (B1, toàn mẫu) | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 48/982 = 4,9% trong phạm vi `noi_dia` + `hang_nang`) | Rà 20 trace làm lại gần nhất trong 3 ngày; chưa về dưới 7% ở tuần kế tiếp thì thu hẹp về `noi_dia` | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ nếu làm lại 9 phút; 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated] (B4, chưa gồm chi phí cố định) | Phút xem lại trung bình > 4,8 phút (mức hoà vốn), hoặc còn xem lại > 50% yêu cầu ở cuối bước rollout 0.25 (đợt chạy thử: 128/982 = 13,0%) | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%; chưa đạt thì không sang bước 0.50 | Trưởng nhóm CSKH |
| Khối lượng thấp hơn kế hoạch | Chi phí cố định từ 1.185 đ lên 2.370 đ mỗi việc khi khối lượng còn một nửa; tổng từ 4.599 đ (0,38×) lên 5.784 đ (0,48×) [simulated] (A4) | Số việc thành công theo tuần < 50% kế hoạch của bước rollout, 2 tuần liên tiếp | Không mở rộng pilot; tính lại chi phí cố định mỗi việc theo khối lượng thật | Giám đốc vận hành |

Hai con số bất lợi cần nêu khi trình hội đồng: xem lại 100% gần như không tiết kiệm (0,98×–1,03×) [simulated], và phút xem lại, làm lại đều là số giả lập, cần thay bằng số đo thật trong pilot. Các ngưỡng 7%, 50%, 15% là đề xuất của nhóm, không phải số tính từ dữ liệu.
