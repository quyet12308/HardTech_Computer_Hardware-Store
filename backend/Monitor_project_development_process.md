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

## Ngày 31/5/2024
- Xóa file base_codes\security_info.py ra khỏi git ( hóa ra là do sử dụng dấu / \ nên có sự nhầm lẫn của file .gitignore vì vậy file bảo mật của mình vẫn nằm trong git)
- Đã khắc phục bằng cách thay đổi đường dẫn file thành \ , remove file bằng lệnh 
    ```cmd 
    git rm --cached base_codes\security_info.py
    ```
    Và đẩy nó lại lên git
- Test lại web thì thấy lỗi ở phần hàm get_product_overview do không lấy được cái product_name . Mà hiện tịa hết thời gian làm cái này rồi , nên tạm gác nó lại về tối nay làm sau 

## Ngày 13/6/2024 
- có thử đẩy web lên hosting vercel nhưng nó bị lỗi cái cors và bị giới hạn truyền tải mãi ko fix được nên hiện tại sẽ tạm từ bỏ nó để tập trung vào các chức năng chính trước

## Ngày 20/6/2024 
- Lúc rảnh thì cần xem lại cái api lấy dữ liệu để vẽ biểu đồ đơn hàng ( chỉ lấy các đơn hàng ở trạng thái đã thanh toán)
- Thằng paypal nó khá là chi tiết khi tạo thanh toán , nhưng hiện tại mấy phần đó chưa cần thiết lắm nên tập trung vào trạng thái chính còn mấy phần khác như : recall , xác nhận thông tin ... thì để đợt sau khi rảnh sẽ chú ý thêm , dưới đây là mẫu trả về của 1 thanh toán paypal
    ```cmd
    {"id":"PAYID-MZZKF4Q4PK63359P4965762W","intent":"sale","state":"approved","cart":"8EY20799CH0371617","payer":{"payment_method":"paypal","status":"VERIFIED","payer_info":{"email":"sb-g47h43e30937823@personal.example.com","first_name":"John","last_name":"Doe","payer_id":"83PKG4TRLBLCA","shipping_address":{"recipient_name":"John Doe","line1":"1 Main St","city":"San Jose","state":"CA","postal_code":"95131","country_code":"US"},"country_code":"US"}},"transactions":[{"amount":{"total":"10.00","currency":"USD","details":{"subtotal":"10.00","shipping":"0.00","insurance":"0.00","handling_fee":"0.00","shipping_discount":"0.00","discount":"0.00"}},"payee":{"merchant_id":"TFNDN2QS3JVWG","email":"sb-sceol30939219@business.example.com"},"description":"Payment description","item_list":{"shipping_address":{"recipient_name":"John Doe","line1":"1 Main St","city":"San Jose","state":"CA","postal_code":"95131","country_code":"US"}},"related_resources":[{"sale":{"id":"45B28214FP854144Y","state":"completed","amount":{"total":"10.00","currency":"USD","details":{"subtotal":"10.00","shipping":"0.00","insurance":"0.00","handling_fee":"0.00","shipping_discount":"0.00","discount":"0.00"}},"payment_mode":"INSTANT_TRANSFER","protection_eligibility":"ELIGIBLE","protection_eligibility_type":"ITEM_NOT_RECEIVED_ELIGIBLE,UNAUTHORIZED_PAYMENT_ELIGIBLE","transaction_fee":{"value":"0.84","currency":"USD"},"parent_payment":"PAYID-MZZKF4Q4PK63359P4965762W","create_time":"2024-06-19T09:23:30Z","update_time":"2024-06-19T09:23:30Z","links":[{"href":"https://api.sandbox.paypal.com/v1/payments/sale/45B28214FP854144Y","rel":"self","method":"GET"},{"href":"https://api.sandbox.paypal.com/v1/payments/sale/45B28214FP854144Y/refund","rel":"refund","method":"POST"},{"href":"https://api.sandbox.paypal.com/v1/payments/payment/PAYID-MZZKF4Q4PK63359P4965762W","rel":"parent_payment","method":"GET"}]}}]}],"failed_transactions":[],"create_time":"2024-06-19T09:20:49Z","update_time":"2024-06-19T09:23:30Z","links":[{"href":"https://api.sandbox.paypal.com/v1/payments/payment/PAYID-MZZKF4Q4PK63359P4965762W","rel":"self","method":"GET"}]}
    ```
- Có dùng thử cái alembic để đỡ phải thay đổi dữ liệu nhưng khó dùng quá , mà hiện tại ko có time để nghiên cứu nên sẽ tạm hoãn nó lại => dùng cách cữ ( xóa bảng cữ đi kèm theo dữ liệu trong đó để tạo 1 cái bảng mới)
- Hiểu sai về cái checksum nên mà hiện tại éo còn thời gian sửa csdl nữa nên gán tạm nó bằng order_id ( lúc thanh toán ấy chứ ko phải order_id của csdl)
- Thằng paypal vẫn chưa hiểu hoạt động của nó , nhưng là 1 phương thức thanh toán phổ biến trên quốc tế nên cần sắp xếp thời gian nghiên cứu lại nó ( thi thoảng nó mới trừ tiền chưa hiểu tại sao ?)
- Cái mô tả của paypal nó ko nhận tiếng việt