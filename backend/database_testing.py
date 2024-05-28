from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setting import *

from Database_initialization_and_structure import *
from work_with_databases.work_with_products_and_discount_service import *
from work_with_databases.work_with_payment_service import *
from work_with_databases.work_with_cart_service import *
from work_with_databases.work_with_order_service import *
from work_with_databases.work_with_user_and_sesion_service import *
from work_with_databases.work_with_brand_and_category_service import *
from work_with_databases.work_with_comment_and_ranking_service import *

from base_codes.get_token import generate_token
from base_codes.gettime import gettime2, add_time_to_datetime, convert_to_datetime
from base_codes.hash_function import *

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

# b = add_user(
#     username="user4",
#     email="",
#     password="user123",
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

# new_data = {"username": "user2", "fullname": "Đỗ Thị Phương Anh"}

# a = update_user(email="user4@example.com", new_data=new_data)
# print(a)

# new_data = creat_new_data_for_update_user(
#     fullname="Đỗ Thị Phương Anh", phone_number="123456789"
# )
# print(new_data)

# a = update_user(email="user4@example.com", new_data=new_data["message"])
# print(a)


# a = get_user(user_id=3)
# print(a)

# test_alter_table_with_brand_table(
#     "databases/ecommerce_database.db", "brands", "add", "url_web"
# # )

# description_json = create_brand_description(
#     lich_su="Thành lập năm 1969 tại California, Hoa Kỳ.",
#     san_pham="Cung cấp CPU, GPU và chipset cho máy tính cá nhân, máy tính xách tay, máy chủ và máy trạm.",
#     uu_diem="Giá thành cạnh tranh, hiệu năng ngày càng được cải thiện, đặc biệt trong phân khúc tầm trung và cao cấp.",
#     nhuoc_diem="Một số dòng sản phẩm có thể tiêu thụ nhiều điện năng hơn so với Intel.",
#     dong_san_pham="Ryzen 3, Ryzen 5, Ryzen 7, Ryzen 9, Radeon RX 6000 series.",
#     website="https://shop-us-en.amd.com/",
# )
# a = add_brand(brand_name="AMD", description=description_json, img="")
# print(a)


# Sử dụng hàm clear_table_data
# clear_table_data(DATA_BASE_PATH, "brands")
# clear_table(DATA_BASE_PATH, "brands")

# display_table_data(db_path=DATA_BASE_PATH, table_name="brands")

# a = delete_brand(brand_name="AMD")
# print(a)

# a = delete_table_data(DATA_BASE_PATH, "payment_details")
# print(a)

# b = delete_table_data(DATA_BASE_PATH, "cart_item")
# print(b)

# a = edit_brand_data(new_brand_name="AMD", brand_id=1)
# print(a)

# category_description = "RAM (Random Access Memory) là một loại bộ nhớ trong máy tính được sử dụng để lưu trữ dữ liệu tạm thời và dùng làm bộ nhớ làm việc cho các chương trình và hệ điều hành.\n Hiệu suất của RAM được đánh giá dựa trên dung lượng (thường được đo bằng đơn vị gigabyte - GB) và tốc độ truyền dữ liệu (thường được đo bằng megahertz - MHz). RAM có thể được nâng cấp hoặc mở rộng để cung cấp hiệu suất tốt hơn cho các ứng dụng đòi hỏi nhiều tài nguyên."

# a = add_category(category_name="RAM", description=category_description)
# print(a)

# a = edit_category_data(new_category_name="Main", category_id=1)
# print(a)

# product_name = "CPU1"
# price = 3000000
# description = "CPU Test1"
# category_id = 2
# brand_id = 1
# quantity = 5
# image = "cpu_test1.jpg"

# result = add_product(
#     product_name=product_name,
#     price=price,
#     description=description,
#     category_id=category_id,
#     brand_id=brand_id,
#     quantity=quantity,
#     image=image,
# )

# print(result)

# a = get_product_details(product_id=1)
# print(a)

# b = compress_order_items(
#     product_ids=[1, 2, 3], quantities=[2, 1, 2], unit_prices=[400, 600, 500]
# )
# a = add_order(
#     order_items=b,
#     order_status="đang chờ xác nhận",
#     payment_method="paypay",
#     shipping_address="test",
#     total_price="200000",
#     user_id=2,
# )
# print(a)

# a = edit_order(order_id=1, order_status="Đang giao", payment_method="Momo")
# print(a)

# a = add_to_cart(product_id=2, quantity=1, user_id=3)
# print(a)

# result = add_payment(order_id=1, amount=100, provider="PayPal", status="Thành công")
# print(result)

# result = edit_payment(
#     payment_id=1, amount=150, provider="Stripe", status="Đã hoàn thành"
# )
# print(result)

# a = add_login_session(
#     user_id=2,
#     expiration_date=convert_to_datetime(
#         time_string=add_time_to_datetime(hours=2)["message"]
#     ),
#     token_value=generate_token(),
# )
# print(a)

# update password

# user_infor = get_user(user_id=1)["message"]
# old_password = user_infor["password"]

# new_password = hash_password(password=old_password)
# user_infor["password"] = new_password
# a = update_user(new_data=user_infor, user_id=1)
# print(a)

# old_password = "admin123"

# new_password = get_user(user_id=1)["message"]["password"]
# a = verify_password(hex_string=new_password, password=old_password)
# print(a)

# a = get_user_id_by_username(username="user2")
# print(a)

# a = add_authentication_code(
#     code="111111",
#     email="quyet12305@gmail.com",
#     expiration_time=convert_to_datetime(
#         time_string=add_time_to_datetime(minutes=3)["message"]
#     ),
# )
# print(a)

# a = query_authentication_code_by_email(email="quyet12306@gmail.com")
# print(a["code"].code)

# a = get_user(email="quyet12306@gmail.com")
# print(a)

# a = get_product_overview()
# # print(a)
# for i in a:
#     print(i)

# a = drop_table(table_name="products", db_path=DATA_BASE_PATH)
# print(a)

# a = drop_table2(table_name="products")
# print(a)

# a = drop_table3(table_name="orders")
# print(a)

# a = query_category_by_name(category_name="CPU")
# print(a["messgae"].category_id)

# a = generate_token()
# print(a)

# a = get_product_overview(
#     order_by="created_at",
#     reverse=True,
#     category_name=PRODUCT_TYPES_ON_HOMEPAGE[0],
#     limit=3,
# )
# for i in a:
#     print(i)

# a = get_product_detail(product_id=3)
# print(a)

# a = get_user_comments(limit=10, user_id=1)
# print(a)

# a = get_user_id_from_token(token_value="hIqILgWLZHDJYZHh9xPDTQ1716172722")
# print(a)

# a = add_to_cart(
#     quantity=3,
#     user_id=3,
#     product_id=2,
# )
# print(a)

# search_results = search_products(keyword="main")
# for product in search_results:
#     print(product)

# a = get_unique_category_and_brand_names()
# print(a)

# list_order_statuses = [
#     "Pending",
#     "Processing",
#     "Shipped",
#     "Delivered",
#     "Cancelled",
#     "Returned",
# ]
# a = add_order_statuses(list_order_statuses)
# print(a)
