# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83% = 994/1.200** |
| Dùng | Tỉ lệ bỏ qua gợi ý | Trong các yêu cầu `duoc_xem_lai == 1`, đếm `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12% = 48/177** |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25% = 51/1.200** |
| Dùng (tự đề xuất) | Tỉ lệ yêu cầu của nhóm can thiệp được nhân viên mở gợi ý của trợ lý | Số yêu cầu `arm = tro_ly` có event `agent_suggestion_shown`, chia số yêu cầu `arm = tro_ly` được giao cho nhân viên đó, theo tuần | Không cần tính (CSV không có cột `arm`) |
| An toàn (tự đề xuất) | Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, ca 17) | Số mẫu có `so_tien_da_hoan` khác `so_tien_dung` chia số mẫu `audit_sample_checked`; mẫu 100 đơn/tuần | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

**Bàn giao số E1 — Thành viên 2, Vũ Văn Chủ:** `tinh_chi_so()` / `in_chi_so()` trong `src/lab13.py` tính ba dòng trên; trong phạm vi `noi_dia` + `hang_nang`, mở lại là **39/982 = 3,97%** (D3). Toàn bộ là dữ liệu giả lập của lab. Chỉ số chính 994 ca khác 978 ca `ket_qua == 'thanh_cong'` của mô hình chi phí vì định nghĩa thành công chi phí còn xét sai tiền; không thay hai mẫu số/tử số cho nhau.

Trong pilot, chỉ tính chỉ số chính và mở lại trên cohort được theo dõi đủ 7 ngày. Baseline 70% là giả định thiết kế, chưa thể dùng 82,83% của mẫu chạy thử để kết luận có tác động. Hai chỉ số tự đề xuất, event và kiểm tra chéo bên dưới do Thành viên 3 tiếp tục hoàn thiện theo phân công.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Ứng dụng của khách | request_id, order_id, loai, so_tien, arm, created_at, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | request_id, attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | request_id, staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | staff_id, quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật), trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | staff_id, phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | order_id, idempotency_key, so_tien, ket_qua (ok/503/...), trace_id | Mỗi lần ghi sổ, kể cả lần lỗi |
| `refund_notice_sent` | Agent | request_id, kenh, noi_dung_co_bao_da_hoan, gio_gui, trace_id | Khi gửi tin nhắn cho khách |
| `handoff_to_staff` | Agent | reason (thieu_du_lieu, ngoai_pham_vi, ...), tom_tat, trace_id | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | request_id, closed_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | request_id, reopened_at, reason (so_tien, khac), trace_id | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | request_id, so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần, mẫu 100 đơn |

Tổng cộng mười hai event (mười một ở bảng trên và một ở bảng bổ sung), đủ yêu cầu tối thiểu sáu. Hai event do nhóm thêm ngoài mẫu của hướng dẫn: `refund_notice_sent` (để đối soát ca 7: báo "đã hoàn" mà sổ cái chưa ghi) và `input_validation_failed` (ca 1, ca 9).

| Event bổ sung | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `input_validation_failed` | Agent | request_id, truong_loi (so_tai_khoan, ma_van_don), loai_ma_nhap, trace_id | Khi đầu vào của khách không hợp lệ (ca 1, ca 9) |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, event dùng để tính. Cả năm chỉ số đều tính được từ danh sách event; không chỉ số nào ở trạng thái chưa đo được.

| Chỉ số | Event dùng để tính | Cách ghép |
| --- | --- | --- |
| Chính: đóng trong 24 giờ và không mở lại 7 ngày | `refund_request_created`, `ticket_closed`, `ticket_reopened` | Ghép theo `trace_id`: `closed_at − created_at ≤ 24 giờ` và không có `ticket_reopened` trong 7 ngày; chỉ tính cohort đã đủ 7 ngày theo dõi |
| Dùng: tỉ lệ bỏ qua gợi ý | `agent_suggestion_shown`, `staff_review_decision` | Mẫu số: yêu cầu có `agent_suggestion_shown` và được xem lại; tử số: `quyet_dinh` là `sua` hoặc `bo` |
| An toàn: mở lại trong 7 ngày | `refund_request_created`, `ticket_reopened` | Số yêu cầu có `ticket_reopened` trong 7 ngày chia số yêu cầu đã đủ 7 ngày |
| Dùng (tự đề xuất): % yêu cầu được mở gợi ý | `refund_request_created` (có `arm`), `agent_suggestion_shown` | Chỉ tính nhóm `arm = tro_ly`; ghi theo `staff_id` để phát hiện nhân viên không mở trợ lý |
| An toàn (tự đề xuất): % đơn hoàn sai tiền | `audit_sample_checked`, `refund_ledger_write` | So `so_tien_da_hoan` với `so_tien_dung` của mẫu 100 đơn; ca lệch ghép sổ cái bằng `trace_id` |

Chi phí thật của pilot cũng tính được từ event: token và tool từ `agent_run_completed`, phút xem lại từ `staff_review_decision.phut_xem_lai`, phút làm lại từ `staff_rework_completed.phut_lam_lai`. Đây là chỗ thay hai cột `_simulated` bằng số đo thật.

Số mẫu "đủ 7 ngày" có độ trễ: chỉ số chính và chỉ số mở lại của một yêu cầu gửi ngày D chỉ đủ dữ liệu sau D + 7. Vì vậy ở bước 0.10 (kéo dài 7 ngày) chưa có cohort nào đủ 7 ngày để chấm luật dừng về mở lại; xem mục "Rà soát luật dừng" bên dưới.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công +51,8%, từ 4.472 đ lên 6.787 đ [simulated] (B1, toàn mẫu) | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 48/982 = 4,9% trong phạm vi `noi_dia` + `hang_nang`) | Rà 20 trace làm lại gần nhất trong 3 ngày; chưa về dưới 7% ở tuần kế tiếp thì thu hẹp về `noi_dia` | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ nếu làm lại 9 phút; 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated] (B4, chưa gồm chi phí cố định) | Phút xem lại trung bình > 4,8 phút (mức hoà vốn), hoặc còn xem lại > 50% yêu cầu ở cuối bước rollout 0.25 (đợt chạy thử: 128/982 = 13,0%) | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%; chưa đạt thì không sang bước 0.50 | Trưởng nhóm CSKH |
| Khối lượng thấp hơn kế hoạch | Chi phí cố định từ 1.185 đ lên 2.370 đ mỗi việc khi khối lượng còn một nửa; tổng từ 4.599 đ (0,38×) lên 5.784 đ (0,48×) [simulated] (A4) | Số việc thành công theo tuần < 50% kế hoạch của bước rollout, 2 tuần liên tiếp | Không mở rộng pilot; xem lại hợp đồng chi phí cố định và tính lại theo khối lượng thật, không kết luận trợ lý đắt khi khối lượng còn nhỏ | Giám đốc vận hành |

Chi phí cố định theo bước rollout, nếu một mình nhóm can thiệp gánh cả 40 triệu đ/tháng (cách tính từ A4: việc/tháng = 33.750 × tỉ lệ; cố định = 40.000.000 ÷ việc/tháng; tổng = cố định + 3.414 đ biến đổi [simulated], giữ như đợt chạy thử; xem lại 100% ở bước 0.10 và 0.25 thì còn cao hơn):

| Bước | Việc thành công mỗi tháng | Cố định mỗi việc | Tổng mỗi việc | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 0.10 (4 người) | 3.375 | 11.852 đ [simulated] | 15.266 đ [simulated] | 1,27× [simulated] |
| 0.25 (10 người) | 8.437,5 | 4.741 đ [simulated] | 8.155 đ [simulated] | 0,68× [simulated] |
| 0.50 (20 người) | 16.875 | 2.370 đ [simulated] | 5.784 đ [simulated] | 0,48× [simulated] |

Vì vậy ngưỡng 8.000 đ của luật dừng 3 chỉ tính chi phí biến đổi (token, tool, xem lại, làm lại). Cộng cả cố định thì bước 0.10 và 0.25 vượt ngưỡng chỉ vì ít việc, dù chi phí biến đổi không đổi [simulated].

Hai con số bất lợi cần nêu khi trình hội đồng: xem lại 100% gần như không tiết kiệm (0,98×–1,03×) [simulated], và phút xem lại, làm lại đều là số giả lập, cần thay bằng số đo thật trong pilot. Các ngưỡng 7%, 50%, 15% là đề xuất của nhóm, không phải số tính từ dữ liệu.

## Rà soát luật dừng trong `pilot_plan.yaml` · Thành viên 3

Mỗi luật được kiểm tra hai điều: đo được từ danh sách event ở trên không, và có tự mâu thuẫn với số của nhóm không. `pilot_plan.yaml` thuộc phần của Thành viên 2, nên chưa sửa file đó; các điểm cần sửa chuyển cho Thành viên 2 quyết định.

| Luật | Chỉ số, event | Ngưỡng và cửa sổ | Người có quyền dừng | Kết quả rà soát |
| --- | --- | --- | --- | --- |
| 1. Mở lại 7 ngày | `ticket_reopened` / `refund_request_created`, tách theo `arm` | Cao hơn đối chứng ≥ 2 điểm phần trăm hoặc > 6%, 3 lần kiểm tra hằng ngày liên tiếp | Giám đốc vận hành | Đo được. Hiện tại 4,25% (3,97% trong phạm vi) nên trần 6% không tự kích hoạt [simulated]. Cohort đủ 7 ngày chỉ xuất hiện từ ngày thứ 8, nên ở bước 0.10 (7 ngày, 4 nhân viên) luật này chưa chấm được và mẫu rất nhỏ; nên ghi rõ bước này chỉ dựa vào luật 2 |
| 2. Hoàn trùng hoặc sổ cái bất nhất | `refund_notice_sent` đối chiếu `refund_ledger_write` theo `trace_id` và `order_id` | ≥ 1 ca trong bất kỳ lần đối soát hằng giờ nào | Giám đốc vận hành (tắt), Kế toán trưởng (xử lý) | Đo được nhờ hai event `refund_notice_sent` và `refund_ledger_write.idempotency_key`; thiếu hai event này thì luật không chạy được. Đã nằm trong điều kiện 1 của hồ sơ launch (ca 7, ca 20) |
| 3. Chi phí biến đổi mỗi việc thành công | `agent_run_completed`, `staff_review_decision.phut_xem_lai`, `staff_rework_completed.phut_lam_lai` | > 8.000 đ trong 2 tuần liên tiếp tại mốc tuần | PM trợ lý hoàn phí | **Có điểm mâu thuẫn.** Bước 0.10 và 0.25 đều xem lại 100% (mỗi bước 1 tuần). Với số giả lập, xem lại 100% cho 11.743 đ/việc (B4) > 8.000 đ, nên luật sẽ tự kích hoạt đúng sau hai tuần đầu, trước khi tới bước 0.50. Ngoài ra `hang_nang` riêng đã là 8.221 đ [simulated] (A3) |
| 4. Bỏ qua gợi ý | `staff_review_decision` / `agent_suggestion_shown` | Sửa + bỏ > 40% trong 1 tuần (hiện tại 27,12%, 48/177 [simulated]) | Trưởng nhóm CSKH | Đo được. Chưa có số quyết định tối thiểu: bước 0.10 chỉ có 4 nhân viên nên một tuần có thể dưới 100 quyết định; nên đòi ít nhất 100 quyết định xem lại như điều kiện của `review_policy` |

Đề xuất cho Thành viên 2 (chưa áp dụng): (a) luật 3 chỉ tính từ bước 0.50, hoặc dùng ngưỡng riêng cho giai đoạn xem lại 100% (ví dụ ngưỡng theo B4 là 12.415 đ); nêu rõ luật đo trên phút xem lại thật, không phải phút giả lập; (b) luật 1 ghi rõ không chấm ở bước 0.10; (c) luật 4 thêm điều kiện tối thiểu 100 quyết định. Hội đồng khó hỏi nhất sẽ là câu "chi phí nếu tuần đầu xem lại 100%": 11.743 đ = 0,98× [simulated], gần hoà vốn.
