# Báo cáo cá nhân — VuDuyKhanh-2A202603865

## 1. Thông tin thành viên

- Họ tên: Vũ Duy Khánh
- MSSV: 2A202603865
- Email: khanhduy1609@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 2 kiêm giữ hồ sơ (Thành viên 4)

## 2. Phần việc phụ trách

- `report/team/ho_so_launch_v0.md`: điền cuốn chiếu sau mỗi checkpoint CP1–CP5, chốt đề xuất cuối.
- CP3: gắn nhãn độc lập 20 ca lỗi (bộ nhãn người 2 trong `report/team/bang_loi.md`), sau đó cùng Người gắn nhãn 1 so nhãn.
- Duyệt chéo Gate 2a: trình bày hồ sơ nhóm A90, ghi `report/team/phieu_cham.md` khi nhóm chấm nhóm n + 1.
- Tổng hợp `TEAM.md`, `report/team/group_report.md`; rà checklist `SUBMISSION.md`, nhắc cả nhóm nộp link LMS.

## 3. Đóng góp cụ thể

- Điền đủ 7 mục hồ sơ launch v0 với con số chính, trạng thái, người phụ trách là một vai trò; đề xuất **Go có điều kiện** cho phạm vi noi_dia + hang_nang, kèm 4 điều kiện có vai trò phụ trách và ngày kiểm tra.
- Nêu rõ các con số bất lợi trong đề xuất: power 0,64 nếu tác động thật 5 điểm; xem lại 100% còn 11.743 đ = 0,98× (simulated); 92,5% chi phí là phút nhân viên simulated.
- Gắn nhãn 20 ca lỗi (bộ nhãn người 2): ...
- Ghi phiếu chấm nhóm ...: ...
- Viết `report/team/group_report.md` và mục Thành viên 4 trong `TEAM.md`.

## 4. Bằng chứng

- Commit: ... (điền hash sau khi push)
- File: `report/team/ho_so_launch_v0.md`, `report/team/phieu_cham.md`, `report/team/group_report.md`, `TEAM.md`, cột "Nhãn người 2" trong `report/team/bang_loi.md`.
- Con số trong hồ sơ đối chiếu với output `python3 lab13.py`: 4.472 đ/việc thành công [simulated], 82,83% / 27,12% / 4,25%, D1 1.251 · 859 · DE 6,96.

## 5. Công cụ AI đã dùng

- Claude Code: đọc đề, chạy `src/lab13.py`, soạn khung `ho_so_launch_v0.md` và `group_report.md` từ output của script.
- Tự kiểm tra: mọi số trong hồ sơ được so lại với output `lab13.py` và bảng số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch ≤ 2%); rà lại để hồ sơ không dùng từ cấm theo quy tắc 5 của `README.md`.
- Không dùng AI để gắn nhãn 20 ca lỗi hay để chấm điểm nhóm khác.

## 6. Tự đánh giá

...
