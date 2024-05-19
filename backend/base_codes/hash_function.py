import hashlib
import os


# def hash_password(password, salt=None):
#     """
#     Hàm này mã hóa một mật khẩu bằng thuật toán băm SHA256.
#     Nếu cung cấp muối, muối sẽ được thêm vào mật khẩu trước khi băm.

#     Args:
#       password (str): Mật khẩu cần mã hóa.
#       salt (str, tùy chọn): Muối để tăng cường bảo mật.

#     Returns:
#       str: Băm mật khẩu.
#     """

#     # Tạo muối nếu không được cung cấp
#     if salt is None:
#         salt = os.urandom(32)  # Tạo muối ngẫu nhiên dài 32 byte

#     # Thêm muối vào mật khẩu
#     salted_password = password + salt.decode("utf-8")

#     # Mã hóa mật khẩu đã thêm muối bằng SHA256
#     hashed_password = hashlib.sha256(salted_password.encode("utf-8")).hexdigest()

#     # Trả về băm mật khẩu
#     return hashed_password


# # Ví dụ sử dụng
# password1 = "quyet12306"
# password2 = "0985199843quyet"
# hashed_password1 = hash_password(password1)
# hashed_password2 = hash_password(password2)
# print(hashed_password1)
# print(hashed_password2)

import hashlib
import os


def hash_password(password):
    # Tạo một salt ngẫu nhiên
    salt = os.urandom(16)

    # Sử dụng thuật toán PBKDF2 để mã hóa mật khẩu với salt
    hashed_password = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, 100000
    )

    # Kết hợp salt và mật khẩu đã mã hóa thành một chuỗi
    encoded_password = salt + hashed_password

    return encoded_password.hex()


def verify_password(password, hex_string):
    # Lấy salt từ chuỗi đã mã hóa
    encoded_password = bytes.fromhex(hex_string)
    salt = encoded_password[:16]

    # Mã hóa mật khẩu nhập vào với salt đã lấy
    hashed_password = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, 100000
    )

    # So sánh mật khẩu đã mã hóa từ dữ liệu nhập vào với mật khẩu đã mã hóa trong cơ sở dữ liệu
    if encoded_password[16:] == hashed_password:
        return True
    else:
        return False


# Mã hóa mật khẩu trước khi lưu vào cơ sở dữ liệu
# password = "my_password"
# encoded_password = hash_password(password)
# print("Mật khẩu đã mã hóa:", encoded_password)
# print(type(encoded_password))

# # Xác minh mật khẩu khi người dùng đăng nhập
# input_password = "my_password1"
# if verify_password(input_password, encoded_password):
#     print("Mật khẩu chính xác!")
# else:
#     print("Mật khẩu không chính xác!")
