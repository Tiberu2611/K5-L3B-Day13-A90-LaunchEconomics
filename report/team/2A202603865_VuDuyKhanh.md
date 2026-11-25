# Báo cáo cá nhân — VuDuyKhanh-2A202603865

## 1. Thông tin thành viên

- Họ tên: Vũ Duy Khánh
- MSSV: 2A202603865
- Email: khanhduy1609@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 2 kiêm giữ hồ sơ (Thành viên 4)

## 2. Phần việc phụ trách

- `report/team/ho_so_launch_v0.md`: giữ và cập nhật cuốn chiếu hồ sơ một trang (7 mục) từ CP1 đến CP5, chốt đề xuất cuối và các điều kiện ràng buộc cho hội đồng Gate 2a.
- CP3 (`report/team/bang_loi.md`): gắn nhãn độc lập 20 ca lỗi theo 5 loại của Google PAIR (cột `Nhãn người 2`, 8 phút không trao đổi), sau đó đối chiếu với Thành viên 3 để tính tỉ lệ đồng thuận và viết quy tắc phân biệt.
- Duyệt chéo Gate 2a (`report/team/phieu_cham.md`): đại diện trình bày hồ sơ nhóm A90, đồng thời ghi phiếu chấm khi nhóm A90 làm hội đồng chấm nhóm n + 1.
- Tổng hợp `TEAM.md` và `report/team/group_report.md`; chạy kiểm tra `src/lab13.py` trên máy thứ hai; rà checklist `SUBMISSION.md` và nhắc cả 4 thành viên nộp link repo lên LMS trước 23h59 GMT+7.

## 3. Đóng góp cụ thể

- **Hồ sơ launch v0 (`report/team/ho_so_launch_v0.md`):**
  - Hoàn thiện đủ 7 mục với con số chính, trạng thái (`Xong, có bằng chứng` / `Giả lập` / `Chưa`) và người phụ trách là một vai trò cụ thể (không ghi "cả đội").
  - Chốt đề xuất **Go có điều kiện** cho phạm vi `noi_dia` + `hang_nang` (982/1.200 yêu cầu; 0,22× và 0,69×), loại bỏ `quoc_te` (1,88×; chạy lại lần 3 chỉ đạt 2,2% ok) và `doi_tac` (0,85×).
  - Nêu thẳng các con số bất lợi: `power = 0,64` nếu tác động thật chỉ 5 điểm; xem lại 100% đẩy chi phí lên 11.743 đ = 0,98× (hoặc 12.415 đ = 1,03× nếu làm lại 15,3 phút) [simulated]; 92,5% tổng chi phí đến từ phút nhân viên [simulated].
  - Kèm 4 điều kiện nghiệm thu có vai trò phụ trách và mốc thời gian khớp với `report/team/pilot_plan.yaml` (kiểm tra trước ngày bắt đầu 2026-11-30, rà soát sau bước 0.10 ngày 2026-12-07, xác nhận đủ 299 yêu cầu/nhân viên trước bước 0.50 ngày 2026-12-13, ngày quyết định 2027-01-04).
- **Báo cáo nhóm (`report/team/group_report.md`) & `TEAM.md`:**
  - Soạn hoàn chỉnh `group_report.md` (8 mục, tóm tắt phương pháp, kết quả A–E, khó khăn kỹ thuật khi cài đặt trên máy thứ hai, hạn chế và hướng cải thiện).
  - Cập nhật thông tin đóng góp, bằng chứng của Thành viên 4 trong `TEAM.md` và chuẩn bị khung tổng hợp cho cả nhóm.
- **CP3 (`report/team/bang_loi.md`):** hoàn thành gắn nhãn độc lập 20 ca lỗi cùng Thành viên 3, đạt tỉ lệ đồng thuận **16/20 = 80%**, thống nhất nhãn và 4 câu quy tắc phân biệt cho các ca lệch. Cập nhật chuyển trạng thái Mục 5 trong `ho_so_launch_v0.md` sang **Xong, có bằng chứng**.
- **Phiếu chấm hội đồng (`report/team/phieu_cham.md`):**
  - Thiết lập sẵn thông tin nhóm chấm (A90 · L3B) và soạn 3 câu hỏi phản biện dự phòng bám sát số liệu đối chiếu (chi phí xem lại 100%, ngưỡng 20 cụm và power 0,64, tỉ lệ mở lại 4,25% với luật dừng tuần đầu).
- **Kiểm chứng trên máy thứ hai:**
  - Tự thiết lập môi trường `src/.venv`, cài đặt `src/requirements.txt` và chạy lại `python lab13.py` để xác nhận toàn bộ kết quả khớp trên máy khác.
- **Phần đang chờ phiên duyệt chéo 17:00:**
  - Điền kết quả chấm chéo thực tế vào `phieu_cham.md` và `group_report.md` trong phiên bảo vệ tại lớp.

## 4. Bằng chứng

| Việc | Bằng chứng |
| --- | --- |
| Hồ sơ launch v0, phiếu chấm, báo cáo nhóm | Commit `5f9e938` |
| Đồng bộ mốc ngày điều kiện với `pilot_plan.yaml` | Commit `17b79fc` |
| Chạy kiểm chứng trên máy thứ hai | `cd src && .venv/bin/python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` (1,20 · 1,25 · 1,25) |
| Đối chiếu số liệu hồ sơ với output `lab13.py` | CPS 4.472 đ (16,3× hoá đơn; 92,5% giờ nhân viên) [simulated]; B4 11.743 đ = 0,98× / 12.415 đ = 1,03× [simulated]; D1 1.251 · 859 · DE 6,96 · power 0,64; E1 82,83% / 27,12% / 4,25% / 3,97% |
| Hồ sơ và báo cáo đã nộp | `report/team/ho_so_launch_v0.md`, `report/team/phieu_cham.md`, `report/team/group_report.md`, `TEAM.md` |

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code (soạn khung ban đầu cho `ho_so_launch_v0.md`, `group_report.md`, `phieu_cham.md` từ output của `src/lab13.py`) và Antigravity / Gemini (rà soát toàn bộ project, đối chiếu phần việc còn thiếu của Thành viên 4 và hoàn thiện lại báo cáo cá nhân này).
- **Tự kiểm tra kết quả:**
  - Chạy trực tiếp `src/lab13.py` trong `src/.venv`, đối chiếu từng con số trong `ho_so_launch_v0.md` và `group_report.md` với output của script và bảng đáp án trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (sai lệch ≤ 2%).
  - Rà soát bằng `grep` để đảm bảo toàn bộ số tính từ `_simulated` đều có nhãn `simulated`, không có từ bị cấm theo quy tắc 5 của `README.md`, và các mốc ngày khớp hoàn toàn với `pilot_plan.yaml`.
  - **Không** dùng AI để gắn nhãn 20 ca lỗi hay chấm điểm nhóm khác (tuân thủ `RULES.md`).

## 6. Tự đánh giá

- **Phần làm tốt:** Chủ động dựng và cập nhật cuốn chiếu `ho_so_launch_v0.md` đủ 7 mục rõ ràng, trung thực với dữ liệu (nêu thẳng các con số bất lợi như `power 0,64` và ngưỡng hoà vốn xem lại `≤ 5,12 phút/ca`), hoàn thành gắn nhãn CP3 đạt đồng thuận 80%, đồng thời đối khớp chặt chẽ mốc thời gian với kế hoạch pilot và kiểm chứng chạy code trên máy thứ hai.
- **Phần còn thiếu / cần hoàn thiện:** Cập nhật kết quả duyệt chéo và hoàn thiện `phieu_cham.md` sau phiên hội đồng 17:00 tại lớp.
- **Điều học được:** Một hồ sơ duyệt Gate 2a thuyết phục không phải là hồ sơ chọn phương án lạc quan nhất, mà là hồ sơ tách rõ dữ liệu đo thật với dữ liệu giả lập (`simulated`), chỉ ra được giới hạn cỡ mẫu khi chia cụm, và gắn mỗi rủi ro kinh tế với một điều kiện dừng có người chịu trách nhiệm cụ thể.
