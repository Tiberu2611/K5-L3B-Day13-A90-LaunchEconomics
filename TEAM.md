# Team

## Thông tin nhóm

- Tên nhóm: A90
- Lớp: L3B
- Repo nhóm: `K5-L3B-Day13-A90-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics` · nhánh `main`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Lê Trọng Mạnh | 2A202603857 | manh025011@gmail.com | Tiberu2611 | Người viết code (Ca 1) → Người kiểm số & QA (Ca 2) |
|   2 | Vũ Văn Chủ | 2A202603873 | vuvanchu3012@gmail.com | chur04 | Người kiểm số (Ca 1) → Người viết code (Ca 2) |
|   3 | Chu Quang Linh | 2A202603809 | quanglinh1286@gmail.com | ArsNeonci | Người gắn nhãn 1 · Chỉ số, Event & Bảng lỗi |
|   4 | Vũ Duy Khánh | 2A202603865 | khanhduy1609@gmail.com | khanhduyvu1 | Người gắn nhãn 2 · Giữ hồ sơ Launch v0 & Quản lý nộp bài |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

### Bảng phân quyền sở hữu file (tránh xung đột Git)

| File cần nộp | Người phụ trách chính | Phối hợp |
| --- | --- | --- |
| `src/lab13.py` | Thành viên 1 (CP1–CP2) → Thành viên 2 (CP4–CP5) | Đổi ca sau giờ giải lao (15:35) |
| `report/team/bang_chi_phi.md` | Thành viên 2 | Thành viên 1 xuất số từ `src/lab13.py` |
| `report/team/bang_loi.md` | Thành viên 3 | Thành viên 3 & 4 gắn nhãn độc lập 8 phút trước khi so |
| `report/team/pilot_plan.yaml` | Thành viên 2 | Thành viên 1 kiểm số D1, Thành viên 3 rà 3 `stop_rules` |
| `report/team/chi_so.md` | Thành viên 3 | Thành viên 2 đưa 3 số E1, Thành viên 1 viết bảng rủi ro E2 |
| `report/team/ho_so_launch_v0.md` | Thành viên 4 | Cập nhật cuốn chiếu sau mỗi checkpoint (CP1–CP5) |
| `report/team/phieu_cham.md` | Thành viên 4 | Cả 4 thành viên cùng đọc hồ sơ nhóm n + 1 và chốt điểm |
| `TEAM.md`, `report/team/group_report.md` | Thành viên 4 | Từng thành viên bổ sung Họ tên, MSSV, Email, GitHub và bằng chứng |
| `report/team/<MSSV>_<HoTen>.md` | Từng thành viên (4 file riêng) | Copy từ `report/team/MSSV_HoTen.md`, giữ nguyên file mẫu |

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## Thành viên 1 — Người viết code (Ca 1) → Người kiểm số & QA (Ca 2)

### Phần việc phụ trách

- CP1 & CP2: Cài môi trường `src/requirements.txt`, code `src/lab13.py` (A1 `kiem_tra_dap_an_biet_truoc()`, A2 `mo_hinh()`, A3 tách `loai`, A4 chi phí cố định 40 triệu đ/tháng, B1–B4 bảng độ nhạy).
- CP3 (8 phút đầu): Cùng Thành viên 2 hoàn thiện câu trả lời B3, B4 trong `report/team/bang_chi_phi.md` và bàn giao `src/lab13.py`.
- CP4 & CP5: Tính tay kiểm chứng 5 câu cỡ mẫu D1; viết mục E2 (Rủi ro kinh tế) trong `report/team/chi_so.md`; chạy kiểm tra cuối (`yaml.safe_load`, không còn `?`, không có từ `production`, chạy `python3 lab13.py` trên máy thứ 2).

### Đóng góp cụ thể

- Phụ trách `src/lab13.py` cho A1–A4 và B1–B4, viết với trợ lý AI (Claude Code); file cũng in sẵn D1 và ba chỉ số E1 để Thành viên 2 kiểm tra và tiếp nhận.
- Phụ trách mục E2 (ba dòng rủi ro kinh tế) trong `report/team/chi_so.md`, soạn với trợ lý AI.
- Tính tay kiểm chứng ba phép thử A1 và năm câu cỡ mẫu D1.

### Bằng chứng

- Commit `5e09dc7` (nhánh `manh`), gộp vào `main` qua PR #1 (`548aa34`).
- `python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT`; A2 = 4.472 đ [simulated], A4 = 4.599 đ [simulated], B3 giới hạn 2 lần = 6.901.220 đ [simulated].
- Phép tính tay A1, D1: mục 5 của báo cáo cá nhân `report/team/2A202603857_NguyenLeTrongManh.md`.

## Thành viên 2 — Người kiểm số (Ca 1) → Người viết code (Ca 2)

### Phần việc phụ trách

- CP1 & CP2: Tính tay đối chiếu công thức A1–A4, B1–B4 (sai lệch ≤ 2%); điền hoàn chỉnh `report/team/bang_chi_phi.md` (đủ nhãn `simulated`, câu trả lời ≤ 3 dòng có số).
- CP4 & CP5: Nhận `src/lab13.py` sau giải lao, code phần D1 (cỡ mẫu, `NormalIndPower`, tỉ lệ `mo_lai_trong_7_ngay` hiện tại) và 3 chỉ số tính thử E1; điền hoàn chỉnh `report/team/pilot_plan.yaml` (comment D1/D2, mọi trường YAML, ≥ 3 `stop_rules` đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`, không còn `?`).

### Đóng góp cụ thể

- Hoàn thiện `report/team/bang_chi_phi.md`: A1–A4, đủ 9 kịch bản B1, B2, B3, B4; bổ sung bảng phép tính đối chiếu từ CSV và nhãn `simulated`.
- Tiếp nhận D1/E1 Mạnh đã viết sẵn trong `src/lab13.py`; bổ sung `tinh_d1()` / `tinh_chi_so()` trả kết quả có thể kiểm tra, phân biệt 5.980 yêu cầu thô và 859,20 mẫu hiệu dụng mỗi nhóm, không bỏ qua `NormalIndPower` khi thiếu thư viện.
- Hoàn thiện `report/team/pilot_plan.yaml`: đủ D1/D2, chia 20–20 theo nhân viên, MDE 6 điểm kèm power khoảng 0,64 nếu hiệu quả thật 5 điểm, 4 luật dừng, rollback và lịch đợi đủ 7 ngày theo dõi.
- Điền ba số E1 và số an toàn trong phạm vi cho Thành viên 3; bổ sung phần bàn giao của mình trong `group_report.md` và báo cáo `2A202603873_VuVanChu.md`.
- Thực hiện với hỗ trợ Codex; phép tính đối chiếu đã được kiểm bằng chương trình, chưa ghi nhận buổi tự kiểm tay hoặc phê duyệt kế hoạch ngoài thực tế.

### Bằng chứng

- Chạy trên môi trường Python 3.12 tại workspace của Thành viên 2: `src/lab13.py` kết thúc thành công; A1 in ĐẠT, tự kiểm B1/B2 đều ĐẠT.
- A2: (245.585,132 + 84.000 + 1.780.000 + 2.264.000) / 978 = 4.471,968 đ → **4.472 đ [simulated]**; bảng đối chiếu chi tiết ở cuối `report/team/bang_chi_phi.md`.
- B3: **6.901.220 đ [simulated]** khi giới hạn 2 lần là nhỏ nhất cho cả hệ thống; B4 làm tròn **11.743 đ / 12.415 đ [simulated]**.
- D1: **1.251; DE 2,48; 3.103; 42 người/nhóm; trần 1.000/300; m tối thiểu 299**, DE 6,96; E1: **994/1.200, 48/177, 51/1.200**, an toàn trong phạm vi **39/982**.
- YAML được kiểm bằng `yaml.safe_load`, không còn dấu hỏi, đủ 4 luật dừng theo mẫu; đã push lên `main` ở commit `781d314`.

## Thành viên 3 — Người gắn nhãn 1 · Chỉ số, Event & Bảng lỗi

### Phần việc phụ trách

- CP1 & CP2: Theo dõi điều kiện "Xong khi" của A, B; soạn trước khung E1 (5 chỉ số và ≥ 6 event có `trace_id`, kiểm tra chéo) trong `report/team/chi_so.md`.
- CP3: Ngồi tách biệt với Thành viên 4 gắn nhãn độc lập 20 ca lỗi trong 8 phút; tính tỉ lệ đồng thuận (≥ 80%), viết quy tắc phân biệt các ca lệch, và điền bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- CP4 & CP5: Phối hợp viết 5 câu D2 và 3 luật dừng; hoàn tất `report/team/chi_so.md` và chuẩn bị câu hỏi phản biện khi chấm chéo.

### Đóng góp cụ thể

- Hoàn thiện `report/team/chi_so.md`: 12 event có `trace_id`, hai chỉ số tự đề xuất, bảng kiểm tra chéo chỉ số với event; soạn với trợ lý AI (Claude Code), đối chiếu số với output `lab13.py`.
- Rà soát 4 luật dừng trong `pilot_plan.yaml`: đo được từ event; phát hiện luật chi phí > 8.000 đ có thể tự kích hoạt khi xem lại 100% (B4 11.743 đ [simulated]); đề xuất sửa cho Thành viên 2 (chưa sửa file YAML).
- Soạn bảng khắc phục 5 ca (9, 7, 18, 4, 17) và khung `bang_loi.md`. Không dùng AI để gắn nhãn 20 ca (theo `RULES.md`).

### Bằng chứng

- File: `report/team/chi_so.md`, `report/team/bang_loi.md`, `report/team/2A202603809_ChuQuangLinh.md`.
- Số trong phần rà soát khớp output `lab13.py`: B4 11.743 đ = 0,98×, A3 hang_nang 8.221 đ, E1 82,83% · 27,12% · 4,25%.
- Bộ nhãn người 1 (20 ca) đã gắn trong `bang_loi.md`. Còn thiếu: bộ nhãn người 2 của Thành viên 4, tỉ lệ đồng thuận và nhãn thống nhất.

## Thành viên 4 — Người gắn nhãn 2 · Giữ hồ sơ Launch v0 & Quản lý nộp bài

### Phần việc phụ trách

- Xuyên suốt CP1–CP5: Điền cuốn chiếu `report/team/ho_so_launch_v0.md` sau mỗi checkpoint (7 mục, trạng thái `Xong, có bằng chứng` / `Chưa` / `Giả lập`, 1 vai trò phụ trách/mục, đề xuất cuối kèm điều kiện & số bất lợi).
- CP3: Ngồi tách biệt với Thành viên 3 gắn nhãn độc lập 20 ca lỗi trong 8 phút, sau đó đối chiếu thống nhất nhãn.
- 17:00–18:00: Trình bày hồ sơ trước hội đồng, ghi `report/team/phieu_cham.md` khi chấm nhóm khác, tổng hợp `TEAM.md` và `report/team/group_report.md`, rà checklist `SUBMISSION.md` và nhắc cả 4 thành viên nộp link lên LMS.

### Đóng góp cụ thể

- Điền đủ 7 mục `report/team/ho_so_launch_v0.md` (con số chính, trạng thái, vai trò phụ trách), đề xuất **Go có điều kiện** cho `noi_dia` + `hang_nang`, nêu cả số bất lợi (`power 0,64`; xem lại 100% = `0,98×–1,03×` [simulated]) và khớp ngày điều kiện với `pilot_plan.yaml`.
- Viết khung `report/team/group_report.md` và chuẩn bị sẵn 3 câu hỏi dự phòng trong `report/team/phieu_cham.md`.
- Chạy `python3 lab13.py` trên máy thứ hai (tạo `.venv`, cài `requirements.txt`): ba phép thử ĐẠT.
- Chưa thực hiện (đang chờ tại lớp): gắn nhãn độc lập 20 ca lỗi cùng Thành viên 3 vào `report/team/bang_loi.md` và chấm chéo nhóm n + 1 vào `report/team/phieu_cham.md`.

### Bằng chứng

- File đã hoàn thành: `report/team/ho_so_launch_v0.md`, `report/team/2A202603865_VuDuyKhanh.md`; file đã dựng khung chờ duyệt chéo: `report/team/phieu_cham.md`, `report/team/group_report.md`.
- Commit: `5f9e938` (hồ sơ launch v0, group report, phiếu chấm, báo cáo cá nhân), `17b79fc` (khớp ngày điều kiện với `pilot_plan.yaml`).
