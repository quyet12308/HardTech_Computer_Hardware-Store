from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from sqlalchemy.sql import and_
from datetime import datetime
from Database_initialization_and_structure import *
from setting import *

# Giả sử bạn đã định nghĩa các class như đã nêu trên
# và đã có URL của cơ sở dữ liệu của bạn
DATABASE_URL = (
    f"sqlite:///{DATA_BASE_PATH}"  # Thay thế bằng URL của cơ sở dữ liệu của bạn
)

# Tạo engine và session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def get_all_products_admin_product_management():
    current_date = datetime.now()

    # Truy vấn để lấy thông tin sản phẩm cùng với các thông tin liên quan
    products = (
        session.query(
            Product.product_id,
            Product.product_name,
            Product.price,
            Category.category_name,
            Brand.brand_name,
            func.coalesce(Discount.discount_percentage, 0).label("discount_percentage"),
            Product.quantity,
        )
        .join(Category, Product.category_id == Category.category_id)
        .join(Brand, Product.brand_id == Brand.brand_id)
        .outerjoin(
            Discount,
            and_(
                Product.product_id == Discount.product_id,
                Discount.start_date <= current_date,
                Discount.end_date >= current_date,
            ),
        )
        .all()
    )

    # Chuyển kết quả truy vấn thành danh sách các dictionary
    result = [
        {
            "product_id": product.product_id,
            "product_name": product.product_name,
            "price": float(product.price),
            "category_name": product.category_name,
            "brand_name": product.brand_name,
            "discount_percentage": product.discount_percentage,
            "quantity": product.quantity,
        }
        for product in products
    ]

    return result


def is_product_taken(product_name):

    existing_product = (
        session.query(Product).filter_by(product_name=product_name).first()
    )

    return existing_product is not None


def get_product_details(product_id):
    # Truy vấn thông tin sản phẩm
    product = (
        session.query(Product).filter(Product.product_id == product_id).one_or_none()
    )

    if not product:
        return None

    # Truy vấn thông tin giảm giá nếu có
    discount = (
        session.query(Discount).filter(Discount.product_id == product_id).one_or_none()
    )

    # Tạo từ điển chứa thông tin chi tiết sản phẩm
    product_details = {
        "id": product.product_id,
        "name": product.product_name,
        "price": float(product.price),
        "description": product.description,
        "category_name": product.category.category_name if product.category else None,
        "brand_name": product.brand.brand_name if product.brand else None,
        "product_image": product.image,
        "brand_image": product.brand.img if product.brand else None,
        "created_at": product.created_at,
        "updated_at": product.updated_at,
        "discount_percentage": discount.discount_percentage if discount else None,
        "discount_start_date": discount.start_date if discount else None,
        "discount_end_date": discount.end_date if discount else None,
    }

    return product_details


##################################################################
########## interact with the brands table in database ############
##################################################################
def is_brand_taken(brand_name):

    existing_brand = session.query(Brand).filter_by(brand_name=brand_name).first()

    return existing_brand is not None


def get_all_brands():
    brands = session.query(Brand).all()
    return [brand.to_dict() for brand in brands]


def get_brand_details(brand_id):

    try:
        brand = session.query(Brand).filter(Brand.brand_id == brand_id).first()
        if brand:
            brand_details = {
                "brand_id": brand.brand_id,
                "brand_name": brand.brand_name,
                "description": brand.description,
                "img": brand.img,
            }
            return brand_details
        else:
            return None
    except SQLAlchemyError as e:
        print(f"Error: {str(e)}")
        return None
    finally:
        session.close()


def add_brand_product_management(brand_name, description, img):
    if is_brand_taken(brand_name=brand_name):
        return {"status": False, "message": "Brand name is taken"}
    new_brand = Brand(brand_name=brand_name, description=description, img=img)
    session.add(new_brand)
    session.commit()
    return {"status": True, "message": ""}


# def delete_brand_product_management_with_id(brand_id):
#     brand_to_delete = session.query(Brand).filter_by(brand_id=brand_id).first()
#     if brand_to_delete:
#         session.delete(brand_to_delete)
#         session.commit()


def delete_brand_product_management_with_id(brand_id):
    # Tìm hãng sản xuất cần xóa
    brand_to_delete = session.query(Brand).filter_by(brand_id=brand_id).first()

    if brand_to_delete:
        # Tìm tất cả các sản phẩm liên kết với hãng sản xuất này
        products_to_delete = session.query(Product).filter_by(brand_id=brand_id).all()

        # Xóa các sản phẩm này
        for product in products_to_delete:
            session.delete(product)

        # Xóa hãng sản xuất
        session.delete(brand_to_delete)

        # Commit tất cả các thay đổi
        session.commit()


def delete_catagory_product_management_with_id(category_id):
    # Tìm hãng sản xuất cần xóa
    catagory_to_delete = (
        session.query(Category).filter_by(category_id=category_id).first()
    )

    if catagory_to_delete:
        # Tìm tất cả các sản phẩm liên kết với hãng sản xuất này
        products_to_delete = (
            session.query(Product).filter_by(category_id=category_id).all()
        )

        # Xóa các sản phẩm này
        for product in products_to_delete:
            session.delete(product)

        # Xóa hãng sản xuất
        session.delete(catagory_to_delete)

        # Commit tất cả các thay đổi
        session.commit()


def update_brand(brand_id, brand_name=None, description=None, img=None):
    brand_to_update = session.query(Brand).filter_by(brand_id=brand_id).first()
    if brand_to_update:
        if brand_name is not None:
            if is_brand_taken(brand_name=brand_name):
                return {"status": False, "message": "Brand name is taken"}
            else:
                brand_to_update.brand_name = brand_name
        if description is not None:
            brand_to_update.description = description
        if img is not None:
            brand_to_update.img = img
        session.commit()
        return {"status": True, "message": ""}


def get_all_categories():
    try:
        categories = session.query(Category).all()
        category_list = []
        for category in categories:
            category_info = {
                "category_id": category.category_id,
                "category_name": category.category_name,
                "description": category.description,
            }
            category_list.append(category_info)
        return category_list
    except SQLAlchemyError as e:
        print(f"Error: {str(e)}")
        return None
    finally:
        session.close()


def get_category(category_id):
    try:
        category = (
            session.query(Category).filter(Category.category_id == category_id).first()
        )
        if category:
            category_info = {
                "category_id": category.category_id,
                "category_name": category.category_name,
                "description": category.description,
            }
            return category_info
        else:
            return None
    except SQLAlchemyError as e:
        print(f"Error: {str(e)}")
        return None
    finally:
        session.close()


def add_new_product(
    product_name,
    image,
    price,
    quantity,
    brand_id,
    description,
    category_id,
    discount_percentage=None,
    start_date=None,
    end_date=None,
):
    # Tạo sản phẩm mới
    if is_product_taken(product_name=product_name):
        messgae = f"Tên sản phẩm đã tồn tại. Vui lòng chọn tên sản phẩm khác."
        return {"status": False, "messgae": messgae}
    else:
        new_product = Product(
            product_name=product_name,
            image=image,
            price=price,
            quantity=quantity,
            brand_id=brand_id,
            category_id=category_id,
            description=description,
        )

        # Thêm sản phẩm mới vào session
        session.add(new_product)
        session.commit()  # Commit để lấy product_id của sản phẩm mới

        # Nếu có thông tin giảm giá, tạo bản ghi giảm giá mới
        if discount_percentage and start_date and end_date:
            # Chuyển đổi start_date và end_date thành đối tượng datetime
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")

            new_discount = Discount(
                product_id=new_product.product_id,
                discount_percentage=discount_percentage,
                start_date=start_date,
                end_date=end_date,
            )

            # Thêm bản ghi giảm giá mới vào session
            session.add(new_discount)
            session.commit()

        return {"status": True, "messgae": ""}
