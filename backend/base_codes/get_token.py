import secrets
import time


def generate_token(lenth=16):
    random_string = secrets.token_urlsafe(lenth)  # Tạo chuỗi ngẫu nhiên
    timestamp = str(int(time.time()))  # Lấy thời gian tạo token và chuyển thành chuỗi
    token = random_string + timestamp  # Kết hợp chuỗi ngẫu nhiên và thời gian
    return token


# a = generate_token()
# print(a)
