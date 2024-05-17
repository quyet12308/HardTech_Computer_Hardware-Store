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
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
from setting import DATA_BASE_PATH
from sqlalchemy.orm import sessionmaker
import json


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
    img = Column(String)
    category = relationship("Category", backref="products")
    brand = relationship("Brand", backref="products")


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


######################################################################
################ delete or clear table in database ###################
######################################################################


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


##################################################################
########## interact with the user table in database ##############
##################################################################


# check user is taken
def is_username_taken(username):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Kiểm tra xem tên người dùng đã tồn tại trong cơ sở dữ liệu hay chưa
    existing_user = session.query(User).filter_by(username=username).first()

    # Trả về True nếu tên người dùng đã được sử dụng, False nếu chưa
    return existing_user is not None


# add user
def add_user(
    username, password, email, fullname, phone_number, address, img, is_admin=False
):
    # Kiểm tra xem tên người dùng đã tồn tại hay chưa
    if is_username_taken(username):
        messgae = f"Tên người dùng đã tồn tại. Vui lòng chọn tên người dùng khác."
        return {"status": False, "messgae": messgae}
    else:
        # Tạo engine và phiên làm việc
        engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
        Session = sessionmaker(bind=engine)
        session = Session()

        # Tạo đối tượng User mới
        new_user = User(
            username=username,
            password=password,
            email=email,
            fullname=fullname,
            phone_number=phone_number,
            address=address,
            img=img,
            is_admin=is_admin,
        )

        # Thêm đối tượng User mới vào phiên làm việc và commit thay đổi
        session.add(new_user)
        session.commit()
        messgae = f"Thêm người dùng thành công"
        return {"status": True, "messgae": messgae}


# delete user
def delete_user(user_id):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Tìm người dùng dựa trên user_id
    user = session.query(User).filter_by(user_id=user_id).first()

    if user:
        # Xóa người dùng và commit thay đổi
        session.delete(user)
        session.commit()
        message = f"Người dùng với user_id {user_id} đã được xóa."
        return {"status": True, "message": message}
    else:
        message = f"Không tìm thấy người dùng với user_id {user_id}."
        return {"status": False, "message": message}


# update user
def update_user(user_id, new_data):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Tìm người dùng dựa trên user_id
    user = session.query(User).filter_by(user_id=user_id).first()

    if user:
        # Cập nhật thông tin người dùng với dữ liệu mới
        for key, value in new_data.items():
            setattr(user, key, value)

        # Commit thay đổi
        session.commit()
        message = f"Thông tin người dùng với user_id {user_id} đã được cập nhật."
        return {"status": True, "message": message}
    else:
        message = f"Không tìm thấy người dùng với user_id {user_id}."
        return {"status": False, "message": message}


def get_user(user_id):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Tìm người dùng dựa trên user_id
    user = session.query(User).filter_by(user_id=user_id).first()

    if user:
        # Trả về thông tin người dùng
        user_info = {
            "user_id": user.user_id,
            "username": user.username,
            "email": user.email,
            "fullname": user.fullname,
            "phone_number": user.phone_number,
            "address": user.address,
            "img": user.img,
            "is_admin": user.is_admin,
        }
        return {"status": True, "messgae": user_info}
    else:
        messgae = f"Không tìm thấy người dùng với user_id {user_id}."
        return {"status": False, "messgae": messgae}


##################################################################
########## interact with the brands table in database ############
##################################################################


# check brand is taken
def is_brand_taken(brand_name):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    existing_brand = session.query(Brand).filter_by(brand_name=brand_name).first()

    return existing_brand is not None


def create_brand_description(
    lich_su, san_pham, uu_diem, nhuoc_diem, dong_san_pham, website
):
    brand_description = {
        "lich_su": lich_su,
        "san_pham": san_pham,
        "uu_diem": uu_diem,
        "nhuoc_diem": nhuoc_diem,
        "dong_san_pham": dong_san_pham,
        "website": website,
    }
    return json.dumps(brand_description, ensure_ascii=False)


def add_brand(brand_name, description, img):
    # print(brand_name)
    # print(is_brand_taken(brand_name=brand_name))
    if is_brand_taken(brand_name):
        messgae = f"Tên thương hiệu đã tồn tại. Vui lòng chọn tên thương hiệu khác."
        return {"status": False, "messgae": messgae}
    else:
        # Tạo engine và phiên làm việc
        engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
        Session = sessionmaker(bind=engine)
        session = Session()

        # Tạo đối tượng Brand mới
        new_brand = Brand(brand_name=brand_name, description=description, img=img)

        # Thêm đối tượng Brand mới vào phiên làm việc và commit thay đổi
        session.add(new_brand)
        session.commit()
        messgae = f"Thêm thương hiệu thành công"
        return {"status": True, "messgae": messgae}


def edit_brand_data(brand_id, new_brand_name=None, new_description=None, new_img=None):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Lấy đối tượng Brand cần chỉnh sửa
    brand = session.query(Brand).filter_by(brand_id=brand_id).first()

    if not brand:
        message = f"Không tìm thấy thương hiệu với ID {brand_id}."
        return {"status": False, "message": message}

    # Cập nhật thông tin của thương hiệu
    if new_brand_name is not None:
        brand.brand_name = new_brand_name
    if new_description is not None:
        brand.description = new_description
    if new_img is not None:
        brand.img = new_img

    # Commit thay đổi
    session.commit()

    message = f"Đã chỉnh sửa thông tin thương hiệu với ID {brand_id}."
    return {"status": True, "message": message}


def delete_brand(brand_name):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Kiểm tra xem thương hiệu có tồn tại trong cơ sở dữ liệu hay không
    brand = session.query(Brand).filter_by(brand_name=brand_name).first()
    if brand is None:
        message = f"Thương hiệu '{brand_name}' không tồn tại trong cơ sở dữ liệu."
        return {"status": False, "message": message}

    # Xóa thương hiệu từ cơ sở dữ liệu
    session.delete(brand)
    session.commit()
    message = f"Đã xóa thương hiệu '{brand_name}' thành công."
    return {"status": True, "message": message}


##################################################################
########## interact with the categories table in database ########
##################################################################


def is_categorie_taken(category_name):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    existing_brand = (
        session.query(Category).filter_by(category_name=category_name).first()
    )

    return existing_brand is not None


def add_category(category_name, description):
    # print(brand_name)
    # print(is_brand_taken(brand_name=brand_name))
    if is_categorie_taken(category_name):
        messgae = f"Tên thể loại đã tồn tại. Vui lòng chọn tên thể loại khác."
        return {"status": False, "messgae": messgae}
    else:
        # Tạo engine và phiên làm việc
        engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
        Session = sessionmaker(bind=engine)
        session = Session()

        # Tạo đối tượng Brand mới
        new_category = Category(category_name=category_name, description=description)

        # Thêm đối tượng Brand mới vào phiên làm việc và commit thay đổi
        session.add(new_category)
        session.commit()
        messgae = f"Thêm thể loại thành công"
        return {"status": True, "messgae": messgae}


def edit_category_data(category_id, new_category_name=None, new_description=None):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Lấy đối tượng Brand cần chỉnh sửa
    category = session.query(Category).filter_by(category_id=category_id).first()

    if not category:
        message = f"Không tìm thấy thể loại với ID {category_id}."
        return {"status": False, "message": message}

    # Cập nhật thông tin của thương hiệu
    if new_category_name is not None:
        category.category_name = new_category_name
    if new_description is not None:
        category.description = new_description

    # Commit thay đổi
    session.commit()

    message = f"Đã chỉnh sửa thông tin thể loại với ID {category_id}."
    return {"status": True, "message": message}


def delete_category(category_name):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Kiểm tra xem thương hiệu có tồn tại trong cơ sở dữ liệu hay không
    category = session.query(Category).filter_by(category_name=category_name).first()
    if category is None:
        message = f"Thể loại '{category_name}' không tồn tại trong cơ sở dữ liệu."
        return {"status": False, "message": message}

    # Xóa thương hiệu từ cơ sở dữ liệu
    session.delete(category)
    session.commit()
    message = f"Đã xóa thể loại '{category_name}' thành công."
    return {"status": True, "message": message}


##################################################################
########## interact with the products table in database ##########
##################################################################
