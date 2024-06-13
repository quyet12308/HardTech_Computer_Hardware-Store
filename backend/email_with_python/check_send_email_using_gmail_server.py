# import smtplib
# from email.mime.text import MIMEText
# from .base_code.security_info import *

# subject = "Email subject"
# body = "Test send email with python using gmail server"
# sender = "quyet12306@gmail.com"
# recipients = {sender, "quyet12308@gmail.com"}


# def send_email(subject, body, sender, recipients):
#     msg = MIMEText(body)
#     msg["Subject"] = subject
#     msg["From"] = sender
#     msg["To"] = ",".join(recipients)

#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
#         smtp_server.login(emails["gmail"], passwords["gmail"])
#         smtp_server.sendmail(emails["gmail"], recipients, msg.as_string())
#     print("Message sent")


# send_email(subject, body, sender, recipients)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Bạn cần cung cấp thông tin bảo mật của mình ở đây
# từ tệp `security_info.py` hoặc trực tiếp như sau:
emails = {"gmail": "quyet12306@gmail.com", "email_test_to_send": "quyet12308@gmail.com"}

passwords = {"gmail": "dfej bnsz uxza bzkn"}


def send_email(subject, body, sender, recipients, password):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ",".join(recipients)

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
        smtp_server.login(emails["gmail"], password)
        smtp_server.sendmail(emails["gmail"], recipients, msg.as_string())
    print("Message sent")


# Hàm gửi email quên mật khẩu
def send_email_forgot_password(email, username, password, code, to_email, minutes):
    subject = "Send email from Nhom10"
    body = f"""Hello {username}, did you forget your password?

Here is your code:
{code}

Remember your code is only valid for {minutes} minutes."""

    send_email(subject, body, email, [to_email], password)


# Hàm gửi email nhắc nhở admin
def send_email_reminder_admin_about_contact_customer(
    email, username, to_email, created_time, password
):
    subject = "Reminder email for Admin about contact customer"
    body = f"""Hello Admin, you have a contact from {username}.

This contact was sent at {created_time}.

Remember to give feedback to customers."""

    send_email(subject, body, email, [to_email], password)


# Hàm gửi email xác nhận đăng ký
def send_email_confirm_registration(email, username, password, code, to_email, minutes):
    subject = "Send email from Nhom10"
    body = f"""Hello {username}, you registered a new account.

Here is your code:
{code}

Remember your code is only valid for {minutes} minutes."""

    send_email(subject, body, email, [to_email], password)


# Sử dụng các hàm
# if __name__ == "__main__":
#     password = passwords["gmail"]
#     code = "000000"  # Thay bằng code bạn muốn gửi đi
#     to_email = emails["email_test_to_send"]  # Địa chỉ email của người nhận

#     # Gửi email quên mật khẩu
#     result = send_email_forgot_password(
#         email=emails["gmail"],
#         username="test",
#         password=password,
#         code=code,
#         to_email=to_email,
#         minutes=10,
#     )

#     # Gửi email nhắc nhở admin
#     result = send_email_reminder_admin_about_contact_customer(
#         email=emails["gmail"],
#         username="test_user",
#         password=password,
#         to_email=to_email,
#         created_time="2024-06-13 12:00:00",
#     )

#     # Gửi email xác nhận đăng ký
#     result = send_email_confirm_registration(
#         email=emails["gmail"],
#         username="test",
#         password=password,
#         code=code,
#         to_email=to_email,
#         minutes=10,
#     )
#     print(result)

#     if result == "Email sent successfully":
#         print("ok")
#     else:
#         print("something wrong to send email, please check your email again")
