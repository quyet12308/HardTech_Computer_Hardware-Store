# Dự án phát triển hệ thống thương mại điện tử của nhóm 10 

## Tổng quan web bán phần cứng máy tính 
- Ở thời điểm hiện tại thì thương mại điện tử không còn là 1 điều xa lạ gì đến mọi người nữa 
- Vậy nên chúng tôi nhóm 10 quyết định xây dựng 1 web bán phần cứng máy tính làm bài tập lớn cho môn học này

## Công nghệ sử dụng 
- Backend: FastAPI
- Database: SQLite
- Front-end: Html , Css , JS

## Kiến trúc xây dựng 
- Dự án được xây dựng theo kiến trúc Client - Server. Tức là dự án sẽ chia ra làm 2 phần front-end và backend riêng biệt liên kết với nhau thông qua các API

## Cấu trúc dự án
- Dự án chia thành 2 thư mục (2 phần là font-end và backend) 
- Khi chạy cần tách riêng chúng ra 2 cửa sổ riêng biệt để tránh bị lỗi live server

## Các khởi chạy
1. Tải dự án về máy tính bằng lệnh:
```cmd
git clone https://github.com/quyet12308/phat_trien_he_thong_thuong_mai_dien_tu_nhom_10.git
```

2. Tách riêng 2 phần front-end và backend ra (ở đây tôi sử dụng vscode và thao tác tắc trên cmd để mở 2 bọn chúng ở từng cửa sổ vscode khác nhau)
- Mở thư mục chứa dự án này lên cmd 
- Sau đó dùng lệnh **cd front_end** để vào thư mục front-end
```cmd
cd front_end
```
- Sau đó dùng lệnh **code .** để mở thư mục front-end bên trong 1 cửa sổ vscode
```cmd
code .
```
- Backend làm tương tự 
- Dùng lệnh **cd ..** để quay lại thư mục gốc và lệnh **cd backend** để vào thư mục backend và lệnh **code .** để mở thư mục backend bên trong 1 cửa sổ khác của vscode
```cmd
cd .. ; cd backend ; code .
```
3. Chạy front-end bằng cách dùng go live để chạy file index.html(cái này rất cơ bản, nếu các bạn không biết có thể gg search nhá)
4. Chạy backend 
- Di chuyển vào cửa sổ vscode đang mở thư mục backend và mở terminel lên (có thể ấn ctrl + ` cho nhanh)
- Tải các thư viện cần thiết bằng lệnh 
```cmd
pip install -r requirements.txt
```
- Ở đây tôi mặc định là các bạn đã có môi trường python và công cụ quản lý gói pip rồi nhá (nếu chưa thì có thể lên gg tải về, chỉ cần tải xong ấn next => next ... là được, nhưng phải nhớ tích vào ô thêm vào đường dẫn của hệ thống trước khi cài đặt nhá)
- Tiếp đó cần vào trong thư mục base_codes và tạo file backend\base_codes\security_info.py 
    - File security_info.py là 1 file bảo mật cho các apikey , password .... cho các dịch vụ của bên thứ 3 nên tôi sẽ ko public nó lên git 
    - Sau đó hãy điền nội dung sau vào file 
    ```cmd
    urls = {"test_url": ""}

    passwords = {
        "outlook": "",
        "gmail_application_password": "",
    }

    emails = {
        "gmail": "",
        "outlook": "",
        "email_test_to_send": "quyet12306@gmail.com",
        "email_admin": "quyet12306@gmail.com",
    }

    api_key = {
        "openweather": "",
        "X-RapidAPI-Key": "",
    }

    host = {"X-RapidAPI-Host": ""}
    ```
    - Trong đó :
        1. urls chưa dùng đến nên hiện chưa phải điền
        2. outlook trong passwords là để điền mật khẩu email outlook làm mail server
        3. gmail_application_password trong passwords là để điền mật khẩu email gmail làm mail server(chọn 1 trong 2 là được nhưng khuyến khích dùng outlook vì tôi cũng đang dùng , còn nếu bạn dùng gmail thì có lẽ sẽ phải sửa lại code đôi chút)
        4. gmail trong emails là địa chỉ gmail dùng làm mail server
        5. outlook trong emails là địa chỉ outlook dùng làm mail server
        6. 2 cái bên dưới các bạn nhìn tên là cũng đoán được rồi phải không ? nó là dùng để test khi gửi email và địa chỉ email admin sẽ nhận phản hồi 
        7. api_key hiện chưa dùng đến nên có thể không phải điền gì
        8. host cũng chưa dùng đến
- Sau đó chạy file main.py để hệ thống backend chạy là được có thể chạy nó bằng lệnh sau
```cmd
python main.py
```
