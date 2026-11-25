# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: A90 · Lớp: L3B · Số liệu: `src/lab13.py` trên mẫu 1.200 yêu cầu / 1.624 lần chạy (dữ liệu giả lập của lab)

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** (4.373.585 đ / 978 việc thành công) **[simulated]**; gấp 16,3× hoá đơn token + tool chia số yêu cầu (274,7 đ); giờ nhân viên chiếm 92,5% tổng chi phí (làm lại 51,8%, xem lại 40,7%) **[simulated]** | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại ×2: **+51,8%** (6.787 đ) · 2. Tỉ lệ xem lại ×2: **+40,7%** (6.292 đ) · 3. Lương +25%: **+23,1%** (5.506 đ) **[simulated]**; giá token ×2 chỉ +5,6% | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm (12.000 đ) | Toàn mẫu **0,37×**; cả hệ thống (cộng 222 ca chuyển nhân viên) 5.865 đ = **0,49×**. Theo loại: noi_dia 0,22× · hang_nang 0,69× · doi_tac 0,85× · **quoc_te 1,88×** (thành công 27,3%). Phạm vi noi_dia + hang_nang cộng cố định 40 triệu/tháng: 4.599 đ = **0,38×** (một nửa khối lượng: 5.784 đ = 0,48×) **[simulated]** | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử (không có đối chứng): chính **82,83%** (994/1.200) · dùng: bỏ qua gợi ý **27,12%** (48/177) · an toàn: mở lại 7 ngày **4,25%** (51/1.200), trong phạm vi 3,97% (39/982) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận gắn nhãn: **16/20 = 80%**; 5 ca đủ 5 loại PAIR, mỗi dòng có event + ngưỡng. Lỗi phải chặn trước pilot: ca 7 (sổ cái 503 vẫn báo "đã hoàn") và ca 20 (hoàn hai lần, thiếu khoá chống trùng) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo **nhân viên 20 + 20**, ngẫu nhiên phân tầng theo depot. Chênh 5 điểm cần 1.251/nhóm nhưng 20 cụm chỉ đạt tối đa 1.000 → chấp nhận **mde 6 điểm**: 859/nhóm, DE 6,96, ≥ 299 yêu cầu/nhân viên. Bất lợi: nếu tác động thật 5 điểm thì **power chỉ 0,64**. Theo depot (6 + 6) bị loại: tối đa 300. Lịch: bắt đầu 2026-11-30, rollout 10% → 25% → 50% (đo chính 14–27/12), quyết định 2027-01-04 | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại ×2 → 6.787 đ (+51,8%); xem lại 100% noi_dia + hang_nang → **11.743 đ = 0,98×** (12.415 đ = 1,03× nếu làm lại 15,3 phút), hoà vốn khi xem lại ≤ 5,12 phút/ca; khối lượng còn một nửa → cố định 2.370 đ/việc **[simulated]** | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** — pilot chỉ cho `noi_dia` + `hang_nang` (982/1.200 yêu cầu; 0,22× và 0,69×), loại `quoc_te` (1,88×; chạy lại lần 3 chỉ 2,2% ok) và `doi_tac` (0,85×). Con số bất lợi đã nêu: power 0,64 ở mức 5 điểm, xem lại 100% gần hoà vốn (0,98×), 92,5% chi phí là phút **simulated** chưa đo thật.

- Điều kiện 1: sửa khoá chống trùng và đối soát sổ cái (ca 7, ca 20), bật đủ event có `trace_id`, 0 ca hoàn trùng trong thử nghiệm nội bộ · Kỹ sư trưởng agent · kiểm tra 2026-11-29 (trước ngày bắt đầu pilot 2026-11-30).
- Điều kiện 2: xác nhận đủ 40 nhân viên ở 12 depot, ký chấp nhận mde 6 điểm (power 0,64 nếu tác động thật 5 điểm) và khoá trước chỉ số, ngưỡng, luật dừng, ngày quyết định 2027-01-04 · Giám đốc vận hành · 2026-11-29 (trước ngày bắt đầu pilot 2026-11-30).
- Điều kiện 3: thay phút xem lại / làm lại **simulated** bằng phút đo thật sau tuần 1 (bước 0.10, 30/11–06/12); nếu chi phí mỗi việc thành công đo thật > 8.000 đ trong 2 tuần liên tiếp thì thu hẹp về noi_dia · PM trợ lý hoàn phí · 2026-12-07.
- Điều kiện 4: giảm xem lại theo bậc trong bước 0.25 (xem lại 100% chỉ còn 0,98×), mục tiêu xem lại ≤ 5,12 phút/ca, và xác nhận đủ 299 yêu cầu/nhân viên trước bước đo chính · Trưởng nhóm CSKH · 2026-12-13 (trước bước 0.50 bắt đầu 2026-12-14).
