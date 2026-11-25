# Báo cáo cá nhân — ChuQuangLinh-2A202603809

## 1. Thông tin thành viên

- Họ tên: Chu Quang Linh
- MSSV: 2A202603809
- Email: quanglinh1286@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1 (Thành viên 3) · Chỉ số, event và bảng lỗi

## 2. Phần việc phụ trách

- `report/team/chi_so.md`: đặc tả chỉ số E1 (hai chỉ số tự đề xuất), danh sách event có `trace_id`, kiểm tra chéo chỉ số với event, rà soát luật dừng.
- `report/team/bang_loi.md`: hai bộ nhãn độc lập 20 ca (bộ nhãn người 1), tỉ lệ đồng thuận, quy tắc phân biệt, bảng khắc phục 5 ca.
- Phối hợp với Thành viên 2 về năm câu D2 và ba luật dừng trong `report/team/pilot_plan.yaml`.

## 3. Đóng góp cụ thể

- Hoàn thiện `chi_so.md`: 12 event, mỗi event có `trace_id` (vượt mức tối thiểu 6); hai chỉ số tự đề xuất (tỉ lệ yêu cầu được mở gợi ý, tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu); bảng kiểm tra chéo cho thấy cả 5 chỉ số tính được từ danh sách event.
- Rà soát 4 luật dừng của `pilot_plan.yaml` theo hai tiêu chí: đo được từ event, và nhất quán với số của nhóm. Phát hiện luật chi phí (> 8.000 đ trong 2 tuần liên tiếp) sẽ tự kích hoạt khi hai bước đầu xem lại 100%, vì B4 cho 11.743 đ/việc [simulated]; đã ghi đề xuất sửa cho Thành viên 2 trong `chi_so.md`.
- Soạn bảng khắc phục 5 ca (ca 9, 7, 18, 4, 17), mỗi dòng có event, ngưỡng đo được và một vai trò phụ trách.
- Dựng khung `bang_loi.md` với 20 ca và các ô nhãn để gắn độc lập.

## 4. Bằng chứng

- Files: `report/team/chi_so.md`, `report/team/bang_loi.md`, `report/team/2A202603809_ChuQuangLinh.md`.
- Số liệu trong phần rà soát lấy từ output của `python lab13.py` (B4 11.743 đ = 0,98×; A3 hang_nang 8.221 đ; E1 4,25% và 3,97%; sửa + bỏ 27,12%), đều là dữ liệu giả lập của lab.
- Bộ nhãn người 1 (20 ca) do Thành viên 3 tự gắn, đã điền trong `report/team/bang_loi.md` (cột "Nhãn người 1") trước khi so với Thành viên 4.
- Đồng thuận gắn nhãn: **chưa có**; chờ Thành viên 4 gắn cột "Nhãn người 2" rồi hai người mới so nhãn.

## 5. Công cụ AI đã dùng

- Claude Code: soạn bản nháp `chi_so.md` (event, kiểm tra chéo, rà luật dừng), bảng khắc phục 5 ca và khung `bang_loi.md`, trên cơ sở output `src/lab13.py` và hướng dẫn của lab.
- Tự kiểm tra: đối chiếu từng số với output `lab13.py` và `report/team/bang_chi_phi.md`; đối chiếu tên event với cột chỉ số E1; kiểm lại mỗi dòng khắc phục có ngưỡng đo được và một vai trò.
- AI **không** được dùng để gắn nhãn 20 ca lỗi hay tính tỉ lệ đồng thuận (theo `RULES.md`). Các ô nhãn do Thành viên 3 và Thành viên 4 tự điền.

## 6. Tự đánh giá

- **Phần làm tốt:** danh sách event đủ và nối được với cả 5 chỉ số; rà soát luật dừng chỉ ra điểm mâu thuẫn mà hội đồng dễ hỏi.
- **Phần còn thiếu:** cột nhãn người 2 (Thành viên 4), tỉ lệ đồng thuận, nhãn thống nhất và quy tắc phân biệt cho các ca lệch trong `bang_loi.md`; sau khi có nhãn thống nhất phải chọn lại 5 ca của bảng khắc phục cho đủ 5 loại (ca 17 và 18 hiện ghi khác nhãn người 1); chưa trao đổi với Thành viên 2 về đề xuất sửa luật dừng chi phí.
- **Điều rút ra:** chỉ số nào không có event tương ứng thì chưa đo được; và một luật dừng viết đúng mẫu vẫn có thể tự kích hoạt vì ngưỡng chưa tính tới giai đoạn xem lại 100%.
