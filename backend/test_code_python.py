# import datetime
from sqlalchemy import MetaData, Table, Column, String, create_engine
from setting import *
from Database_initialization_and_structure import *


# def get_current_time():
#     current_time = datetime.datetime.now()
#     formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
#     return formatted_time


# # Sử dụng hàm
# current_time = get_current_time()
# print(current_time)

# from base_codes.hash_function import *
# from work_with_database import *

# old_password = "admin123"

# new_pass = ""


# def change_table_structure():
#     # Tạo engine cho SQLite
#     engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")

#     # Tạo Base class
#     # Base = declarative_base()
#     # Tạo đối tượng metadata và liên kết với cơ sở dữ liệu
#     metadata = MetaData(
#         bind=engine
#     )  # Thay "engine" bằng đối tượng SQLAlchemy Engine của bạn

#     # Lấy đối tượng bảng "products" từ metadata
#     products_table = Table("products", metadata, autoload=True)

#     # Kiểm tra xem cột "img" có tồn tại trong bảng hay không
#     if "img" in products_table.c:
#         # Xóa cột "img" từ bảng "products"
#         products_table.c.img.drop()

#         # # Tạo cột mới (ví dụ: cột "new_column") để thay thế cột "img"
#         # new_column = Column('new_column', String)

#         # # Thêm cột mới vào bảng "products"
#         # new_column.create(products_table)

#         # Cập nhật cấu trúc bảng trong cơ sở dữ liệu
#         metadata.drop_all(bind=engine)
#         metadata.create_all(bind=engine)

#         print("Cấu trúc bảng đã được thay đổi thành công.")
#     else:
#         print("Cột 'img' không tồn tại trong bảng 'products'.")


# # Gọi hàm để thực hiện thay đổi cấu trúc bảng
# change_table_structure()

from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DDL

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String)
    price = Column(Numeric)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey("categories.category_id"))
    brand_id = Column(Integer, ForeignKey("brands.brand_id"))
    quantity = Column(Integer)
    image = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    img = Column(String)
    category = relationship("Category", backref="products")
    brand = relationship("Brand", backref="products")


# Tạo một câu lệnh DDL để xóa cột 'img'
drop_img_column = DDL("ALTER TABLE products DROP COLUMN img")

# Tạo engine và liên kết với cơ sở dữ liệu
engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")

# Tạo tất cả các bảng
Base.metadata.create_all(engine, [drop_img_column])
