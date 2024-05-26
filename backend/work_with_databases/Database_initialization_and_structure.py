from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime,
    ForeignKey,
    Numeric,
    func,
    MetaData,
    Table,
    text,
    select,
    Float,
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
from setting import DATA_BASE_PATH
from sqlalchemy.orm import sessionmaker
import json
import sqlite3
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError


def convert_to_json(**kwargs):
    return json.dumps(kwargs)


####################################################
################ create database ###################
####################################################
# Tạo engine cho SQLite
engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")

# Tạo Base class
Base = declarative_base()


# Định nghĩa các model
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    fullname = Column(String)
    phone_number = Column(String)
    address = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    img = Column(String)
    is_admin = Column(Boolean, default=False)


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
    category = relationship("Category", backref="products")
    brand = relationship("Brand", backref="products")


class Discount(Base):
    __tablename__ = "discounts"
    discount_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.product_id"))
    discount_percentage = Column(Float)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    product = relationship("Product", backref="discounts")


class Category(Base):
    __tablename__ = "categories"
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String)
    description = Column(Text)


class Brand(Base):
    __tablename__ = "brands"
    brand_id = Column(Integer, primary_key=True, autoincrement=True)
    brand_name = Column(String)
    description = Column(Text)
    img = Column(String)
    # url_web = Column(String)  # Thêm cột "url" vào bảng "brands"


class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    order_date = Column(DateTime, server_default=func.now())
    order_status = Column(String)
    total_price = Column(Numeric)
    shipping_address = Column(String)
    payment_method = Column(String)
    user = relationship("User", backref="orders")


class OrderDetail(Base):
    __tablename__ = "order_details"
    order_detail_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))
    quantity = Column(Integer)
    unit_price = Column(Numeric)
    order = relationship("Order", backref="order_details")
    product = relationship("Product", backref="order_details")


class Cart(Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    total = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    user = relationship("User", backref="cart")


class CartItem(Base):
    __tablename__ = "cart_item"
    id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey("cart.id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))
    quantity = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    cart = relationship("Cart", backref="cart_items")
    product = relationship("Product", backref="cart_items")


class PaymentDetail(Base):
    __tablename__ = "payment_details"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    amount = Column(Integer)
    provider = Column(String)
    status = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    order = relationship("Order", backref="payment_details")


class Token(Base):
    __tablename__ = "tokens"
    token_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    token_value = Column(String)
    expiration_date = Column(DateTime)  # Thêm trường hợp lệ của token
    created_at = Column(DateTime, server_default=func.now())
    user = relationship("User", backref="tokens")


class Comment(Base):
    __tablename__ = "comments"
    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))
    content = Column(Text)
    rating = Column(Integer)  # Thêm trường đánh giá
    is_approved = Column(Boolean, default=False)  # Thêm trường được chấp nhận
    is_deleted = Column(Boolean, default=False)  # Thêm trường đã bị xóa
    created_at = Column(DateTime, server_default=func.now())
    user = relationship("User", backref="comments")
    product = relationship("Product", backref="comments")


class AuthenticationCode(Base):
    __tablename__ = "authentication_codes"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    code = Column(String)
    expiration_time = Column(DateTime)


##################################################################################
################ delete or clear or drop table in database ###################
##################################################################################


def drop_table(table_name, db_path):
    # Tạo đối tượng SQLAlchemy Engine
    engine = create_engine(f"sqlite:///{db_path}")

    # Xác định tên bảng và kiểm tra xem bảng có tồn tại hay không
    if engine.has_table(table_name):
        # Xóa bảng
        engine.execute(f"DROP TABLE {table_name}")
        message = f"Bảng '{table_name}' đã được xóa thành công."
        return {"status": True, "message": message}
    else:
        message = f"Bảng '{table_name}' không tồn tại."
        return {"status": True, "message": message}


def drop_table2(table_name):
    # Tạo đối tượng engine để kết nối với cơ sở dữ liệu SQLite
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")

    # Tạo đối tượng metadata để lấy thông tin về cơ sở dữ liệu
    metadata = MetaData(bind=engine)
    metadata.reflect()

    # Kiểm tra xem bảng có tồn tại hay không
    if table_name in metadata.tables:
        # Lấy đối tượng bảng từ metadata
        table = metadata.tables[table_name]

        # Xóa bảng
        table.drop(engine)
        message = f"Bảng '{table_name}' đã được xóa thành công."
        return {"status": True, "message": message}
    else:
        message = f"Bảng '{table_name}' không tồn tại trong cơ sở dữ liệu."
        return {"status": False, "message": message}


def drop_table3(table_name):
    # Kết nối tới cơ sở dữ liệu SQLite
    conn = sqlite3.connect(f"{DATA_BASE_PATH}")
    cursor = conn.cursor()

    # Kiểm tra xem bảng có tồn tại hay không
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,)
    )
    result = cursor.fetchone()

    if result is not None:
        # Xóa bảng
        cursor.execute(f"DROP TABLE {table_name}")
        conn.commit()
        message = f"Bảng '{table_name}' đã được xóa thành công."
        # Đóng kết nối
        cursor.close()
        conn.close()
        return {"status": True, "message": message}
    else:
        message = f"Bảng '{table_name}' không tồn tại trong cơ sở dữ liệu."
        return {"status": False, "message": message}


def delete_table_data(db_path, table_name):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{db_path}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Xóa sạch dữ liệu của bảng
    table = Base.metadata.tables[table_name]
    session.execute(table.delete())
    session.commit()

    message = f"Đã xóa sạch dữ liệu của bảng '{table_name}'."
    return {"status": True, "message": message}


######################################################################
################ execute sql in database ###########################
######################################################################


def execute_sql(sql_statement):
    # Tạo đối tượng engine để kết nối với cơ sở dữ liệu SQLite
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")

    try:
        # Kết nối và thực thi câu lệnh SQL
        with engine.connect() as conn:
            conn.execute(sql_statement)

        print("Câu lệnh SQL đã được thực thi thành công.")
        return True
    except SQLAlchemyError as e:
        print("Lỗi trong quá trình thực thi câu lệnh SQL:", str(e))
        return False


######################################################################
################ display table in database ###########################
######################################################################


def display_table_data(db_path, table_name):
    engine = create_engine(f"sqlite:///{db_path}")
    metadata = MetaData()

    with engine.connect() as connection:
        metadata.reflect(bind=engine)
        table = metadata.tables[table_name]

        # Lấy toàn bộ dữ liệu từ bảng
        select_statement = select([table])
        result = connection.execute(select_statement)

        print(f"Nội dung của bảng '{table_name}':")
        for row in result:
            print(row)


# test
def test_alter_table_with_brand_table(db_path, table_name, operation, column):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{db_path}")
    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()

    # Định nghĩa lớp tạm thời để áp dụng thay đổi cấu trúc bảng
    class TempTable(Base):
        __tablename__ = table_name

        # Định nghĩa các cột hiện có trong bảng
        brand_id = Column(Integer, primary_key=True, autoincrement=True)
        brand_name = Column(String)
        description = Column(Text)
        img = Column(String)

    # Kiểm tra loại thao tác
    if operation == "add":
        # Thêm cột mới vào bảng
        setattr(TempTable, column, Column(String))

    elif operation == "drop":
        # Xóa cột khỏi bảng
        delattr(TempTable, column)

    # Tạo bảng tạm thời
    Base.metadata.create_all(bind=engine)

    # Thực hiện thay đổi cấu trúc bảng bằng cách tạo bảng mới và sao chép dữ liệu từ bảng cũ
    session.execute(f"INSERT INTO {TempTable.__tablename__} SELECT * FROM {table_name}")
    session.commit()

    # Xóa bảng cũ
    session.execute(f"DROP TABLE {table_name}")
    session.commit()

    # Đổi tên bảng tạm thời thành tên bảng gốc
    session.execute(f"ALTER TABLE {TempTable.__tablename__} RENAME TO {table_name}")
    session.commit()

    # Đóng phiên làm việc
    session.close()


# Tạo các bảng trong cơ sở dữ liệu
# Base.metadata.create_all(engine)
