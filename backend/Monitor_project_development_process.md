# Tổng quát
- File này được tạo ra để ghi lại quá trình phát triển dự án (các thay đổi , các lỗi tìm thấy , các phương án khắc phục, rút kinh nghiệm ...vv)
- Nó rất hữu ích để sau này có bảo trì hay nâng cấp dự án hoặc đơn giản hơn là xem lại , bàn giao cho người mới thì họ sẽ nắm bắt nhanh hơn
## Ngày 15/5/2024
- Đã tạo ra 3 hàm add_user , delete_user,update_user . Bọn nó đề hoạt động khá ổn (dùng sqlalchemy - thăng này rất mạnh, dùng thay thế cho sqlite truyền thống)
## Ngày 16/5/2024
- Có ý định thay đổi bảng brands để thêm thuộc tính url_web nhưng khá là khó khăn và cồng kềnh nên sẽ tạm gác lại để bao giờ rảnh để làm sau . Vì cái này chỉ là ý muốn nhất thời , nó không quan trọng lắm . Hàm test_alter_table_with_brand_table là hàm chính cho việc này

## Ngày 18/5/2024 
- Nhận thấy rằng hình như cái sqlalchemy nó ghi thời gian vơí múi giờ utc mà mình là utc 07 . Đã thử khắc phục qua nhưng chưa dược => Tạm để đó đã , nếu thời gian thật sự cần thiết thì có thể sẽ viết 1 cái hàm nhỏ chuyển thời gian về utc07 sau khi lấy dữ liệu từ db ra
- Tính thêm thuộc tính update_at cho bảng order nhưng khá khó khăn hoặc do chưa tìm hiểu kỹ vì vậy tạm thời sẽ không thay đổi cấu trúc bảng để sau fix
