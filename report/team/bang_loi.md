# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Chu Quang Linh (Thành viên 3) · Người gắn nhãn 2: Vũ Duy Khánh (Thành viên 4) (gắn trong 8 phút, không trao đổi)

Theo `RULES.md`, hai bộ nhãn phải do hai người tự gắn độc lập, trước khi so, và không sửa sau khi đã so. Các ô `[điền]` dưới đây chưa có nhãn: mỗi người tự gắn cột của mình rồi mới nhìn cột của người kia.

| Ca | Tóm tắt ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- | --- |
| 1 | Khách nhập thiếu hai chữ số tài khoản, ngân hàng trả lỗi | [điền] | [điền] | [điền] | [điền] |
| 2 | Kiện 28 kg, tool tra giá sai tham số, hoàn thiếu 45.000 đ | [điền] | [điền] | [điền] | [điền] |
| 3 | Hoàn về ví LogiX trong 5 phút, khách chờ về ngân hàng | [điền] | [điền] | [điền] | [điền] |
| 4 | Chặng hãng nước ngoài, không có dữ liệu, chuyển nhân viên | [điền] | [điền] | [điền] | [điền] |
| 5 | 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, chỉ thấy khi kiểm mẫu | [điền] | [điền] | [điền] | [điền] |
| 6 | Khách chọn mục "giao trễ" nhưng mô tả hàng vỡ, bị từ chối | [điền] | [điền] | [điền] | [điền] |
| 7 | Sổ cái 503 sau 3 lần thử, vẫn báo "đã hoàn" | [điền] | [điền] | [điền] | [điền] |
| 8 | Dẫn "Điều 7.2" không tồn tại, số tiền vẫn đúng | [điền] | [điền] | [điền] | [điền] |
| 9 | Khách nhập mã đơn sàn TMĐT thay mã vận đơn, trợ lý chỉ báo không hợp lệ | [điền] | [điền] | [điền] | [điền] |
| 10 | Đơn trễ do bão, từ chối đúng chính sách, ứng dụng vẫn hiện "cam kết 24 giờ" | [điền] | [điền] | [điền] | [điền] |
| 11 | Tin nhắn thoại 40 giây, trợ lý không xử lý được âm thanh | [điền] | [điền] | [điền] | [điền] |
| 12 | Tool depot D05 thiếu trường, token gấp 3 lần suốt 3 tuần, không ai thấy | [điền] | [điền] | [điền] | [điền] |
| 13 | Hỏi hoàn phí bảo hiểm của đối tác, trợ lý trả lời chung chung về phí vận chuyển | [điền] | [điền] | [điền] | [điền] |
| 14 | Khách bấm nhầm "Xác nhận đã nhận tiền", yêu cầu bị đóng | [điền] | [điền] | [điền] | [điền] |
| 15 | Trễ 26 giờ phải hoàn 50% nhưng tính 100%, nhân viên bắt được | [điền] | [điền] | [điền] | [điền] |
| 16 | Gửi thông báo Zalo lúc 2:14 sáng theo đúng thiết kế | [điền] | [điền] | [điền] | [điền] |
| 17 | Bộ nhớ đệm bảng giá cũ, 212 đơn lệch 1.000–2.000 đ trong 9 ngày | [điền] | [điền] | [điền] | [điền] |
| 18 | Tính đúng 15.000 đ nhưng tin nhắn không ghi cách tính, khách mở lại | [điền] | [điền] | [điền] | [điền] |
| 19 | Đơn 14 tháng trước, trợ lý chỉ truy cập 12 tháng, nói rõ và chuyển nhân viên | [điền] | [điền] | [điền] | [điền] |
| 20 | Khách gửi lại sau 10 phút, hoàn hai lần vì thiếu khoá chống trùng | [điền] | [điền] | [điền] | [điền] |

**Tỉ lệ đồng thuận:** [điền] / 20 = [điền]% (số ca trùng ÷ 20; cần ≥ 16/20 = 80%)

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại. Điền sau khi hai người đã so nhãn, theo đúng các ca lệch thực tế.

- Ca [điền]: [điền một câu quy tắc, ví dụ theo cặp câu hỏi nhận diện của từng loại: đầu vào của khách sai? có vi phạm thiết kế và có người thấy? chỉ giả định không khớp? làm được không dù có cố gắng? chỉ phát hiện qua kiểm mẫu?]

Câu hỏi nhận diện dùng khi tranh luận (lấy từ hướng dẫn của lab, nguyên tắc "theo nguyên nhân gốc, không theo chỗ cần sửa"):

| Loại | Câu hỏi để nhận ra |
| --- | --- |
| Do người dùng | Đầu vào của khách có sai không? |
| Hệ thống | Có vi phạm thiết kế hoặc chính sách, và có người thấy? |
| Ngữ cảnh | Kết quả đúng, chỉ giả định không khớp hoàn cảnh? |
| Giới hạn hệ thống | Có làm được không, dù có cố gắng? |
| Ngầm | Chỉ phát hiện qua kiểm tra mẫu? |

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội". Năm ca dưới đây chọn mỗi loại một ca; nếu nhãn thống nhất của nhóm khác với cột "Loại lỗi", đổi ca đại diện cho đúng loại. Tên event nằm trong `chi_so.md`. Các ngưỡng là đề xuất của nhóm, chưa đo trên dữ liệu thật.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` với `truong_loi = ma_van_don`; cảnh báo khi vượt 2% số yêu cầu mỗi ngày, hoặc cùng một khách nhập sai ≥ 2 lần trong 10 phút | Nhận diện mẫu mã sàn thương mại điện tử và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh chỗ tìm mã vận đơn, không dừng ở "mã không hợp lệ" | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: `refund_notice_sent` báo "đã hoàn" mà không có `refund_ledger_write` có `ket_qua = ok` cùng `trace_id`; ngưỡng 0 ca (cũng là luật dừng 2 trong `pilot_plan.yaml`) | Chỉ báo "đã hoàn" khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo "đang xử lý" và chuyển nhân viên bằng `handoff_to_staff` kèm tóm tắt | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` có `reason = so_tien` mà `audit_sample_checked` thấy số tiền đúng, theo tuần; ngưỡng đề xuất > 2% số yêu cầu đã hoàn | Mẫu tin nhắn luôn ghi cách tính: 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu`, theo `loai` mỗi tuần; ngưỡng đề xuất > 20% số yêu cầu của một loại (đợt chạy thử: `quoc_te` thành công 27,3%, 150 yêu cầu [simulated]) | Giữ cách chuyển nhân viên kèm tóm tắt; đưa `quoc_te` ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn mỗi tuần (`audit_sample_checked`) so với bảng giá hiện hành; ngưỡng 1% đơn lệch; so `phien_ban_bang_gia` trong trace với bản đang có hiệu lực | Xoá bộ nhớ đệm khi có bảng giá mới và ghi phiên bản bảng giá vào trace | Kế toán trưởng |

Hai ca cần chặn trước ngày bắt đầu pilot (2026-11-30): ca 7 (sổ cái 503 vẫn báo "đã hoàn") và ca 20 (hoàn hai lần, thiếu khoá chống trùng). Phát hiện bằng đối soát `refund_ledger_write` hằng giờ theo `idempotency_key` và `order_id`; người phụ trách là Kỹ sư trưởng agent.
