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
- Có lẽ có thể dùng key word là thực thi câu lệnh sqlite trong sqlalchemy để có thể thay đổi cấu trúc bảng 

## Ngày 25/5/2024
- để ý cái time settup trong sqlalchemy vì hình như nó dùng utc0 mà mình là utc07 nên lúc lấy dữ liệu ra nếu là thời gian mà thằng sqlalchemy tạo thì cần 1 hàm để cover utc0 thành utc07 còn nếu là thời gian được thêm từ bên ngoài thì không cần xử lý

## Ngày 26/5/2024
- Thấy rằng cấu trúc dự án nếu ném tất cả các logic thao tác với db trong 1 file thì sẽ rất khó quản lý nên đã thay đổi cấu trúc của nó đi thành 1 thư mục chứa các code có thể thao tác với db , tác riêng từng file là 1 mảng khác nhau 
- Đường dẫn tương đối khi chia ra như vậy nó không hoạt dộng phải áp dụng đường dẫn khác để giải quyết cụ thể có thể xem ở trong thư mục work_with_databases

## Ngày 27/5/2024
- Cái giá trị thời gian trong 2 bảng cart thì cái update nó theo utc7 còn created thì nó theo utc0
- À mà đã xóa 2 bảng cart cũ đi thay bằng 2 cái mới nhá ( vì bảng cũ có cái tổng giá tiền không hợp lý)
- Định làm 6 trạng thái đơn hàng như sau:
```cmd
Pending: Đơn hàng chưa được xử lý hoặc chưa được xác nhận.
Processing: Đơn hàng đang được xử lý, các hoạt động như gói hàng, chuẩn bị vận chuyển đang diễn ra.
Shipped: Đơn hàng đã được vận chuyển hoặc giao cho đơn vị vận chuyển.
Delivered: Đơn hàng đã được giao thành công và nhận được bởi khách hàng.
Cancelled: Đơn hàng đã bị hủy bỏ trước khi được xử lý hoặc giao hàng.
Returned: Đơn hàng đã được trả lại bởi khách hàng sau khi đã được giao.
```
