from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setting import DATA_BASE_PATH
from work_with_database import (
    User,
    Brand,
    add_user,
    delete_user,
    update_user,
    get_user,
    test_alter_table_with_brand_table,
    add_brand,
    create_brand_description,
    is_brand_taken,
    is_username_taken,
    display_table_data,
    delete_brand,
    delete_table_data,
    edit_brand_data,
    add_category,
    edit_category_data,
)

# b = add_user(
#     username="user3",
#     address="",
#     email="",
#     fullname="",
#     img="",
#     is_admin=False,
#     password="user123",
#     phone_number="",
# )
# print(b)

# delete_user(user_id=2)

# new_data = {
#     "username": "Nguyen Tung Lam",
#     "email": "new_email@example.com",
#     "fullname": "Nguyễn Tùng Lâm",
#     "phone_number": "987654321",
#     "address": "New Address",
#     "img": "new_image.jpg",
#     "is_admin": False,
# }

# update_user(user_id=3, new_data=new_data)

# a = get_user(user_id=3)
# print(a)

# test_alter_table_with_brand_table(
#     "databases/ecommerce_database.db", "brands", "add", "url_web"
# # )

description_json = create_brand_description(
    lich_su="Thành lập năm 1969 tại California, Hoa Kỳ.",
    san_pham="Cung cấp CPU, GPU và chipset cho máy tính cá nhân, máy tính xách tay, máy chủ và máy trạm.",
    uu_diem="Giá thành cạnh tranh, hiệu năng ngày càng được cải thiện, đặc biệt trong phân khúc tầm trung và cao cấp.",
    nhuoc_diem="Một số dòng sản phẩm có thể tiêu thụ nhiều điện năng hơn so với Intel.",
    dong_san_pham="Ryzen 3, Ryzen 5, Ryzen 7, Ryzen 9, Radeon RX 6000 series.",
    website="https://shop-us-en.amd.com/",
)
# a = add_brand(brand_name="AMD", description=description_json, img="")
# print(a)


# Sử dụng hàm clear_table_data
# clear_table_data(DATA_BASE_PATH, "brands")
# clear_table(DATA_BASE_PATH, "brands")

# display_table_data(db_path=DATA_BASE_PATH, table_name="brands")

# a = delete_brand(brand_name="AMD")
# print(a)

# a = delete_table_data(DATA_BASE_PATH, "brands")
# print(a)

# a = edit_brand_data(new_brand_name="AMD", brand_id=1)
# print(a)

# category_description = "Main máy tính (hay còn gọi là bo mạch chủ hoặc motherboard) là thành phần cốt lõi trong một hệ thống máy tính. Nó là một bảng mạch điện tử lớn được thiết kế để kết nối và điều khiển các thành phần khác nhau của máy tính như bộ vi xử lý (CPU), bộ nhớ (RAM), ổ đĩa cứng, đồ họa, âm thanh, cổng kết nối và các linh kiện khác.\nMain máy tính chịu trách nhiệm quản lý và điều phối hoạt động của các thành phần khác nhau trong hệ thống. Nó cung cấp các kết nối và giao tiếp giữa các thành phần, cho phép truyền dữ liệu và tín hiệu điện trong hệ thống máy tính."

# a = add_category(category_name="Main", description=category_description)
# print(a)

a = edit_category_data(new_category_name="Main", category_id=1)
print(a)
