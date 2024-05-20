import smtplib
from email.mime.text import MIMEText
from ..base_code.security_info import *

subject = "Email subject"
body = "Test send email with python using gmail server"
sender = "quyet12306@gmail.com"
recipients = {sender, "quyet12308@gmail.com"}


def send_email(subject, body, sender, recipients):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ",".join(recipients)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
        smtp_server.login(emails["gmail"], passwords["gmail"])
        smtp_server.sendmail(emails["gmail"], recipients, msg.as_string())
    print("Message sent")


send_email(subject, body, sender, recipients)
