from Database_initialization_and_structure import *

##################################################################
########## interact with the products table in database ##########
##################################################################


def is_product_taken(product_name):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    existing_product = (
        session.query(Product).filter_by(product_name=product_name).first()
    )

    return existing_product is not None


def add_product(
    product_name, price, description, category_id, brand_id, quantity, image
):
    if is_product_taken(product_name=product_name):
        messgae = f"Tên sản phẩm đã tồn tại. Vui lòng chọn tên sản phẩm khác."
        return {"status": False, "messgae": messgae}
    else:
        # Tạo engine và phiên làm việc
        engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
        Session = sessionmaker(bind=engine)
        session = Session()

        # Tạo đối tượng sản phẩm mới
        product = Product(
            product_name=product_name,
            price=price,
            description=description,
            category_id=category_id,
            brand_id=brand_id,
            quantity=quantity,
            image=image,
        )

        # Thêm sản phẩm vào phiên làm việc
        session.add(product)

        # Commit thay đổi
        session.commit()

        message = "Đã thêm sản phẩm thành công."
        return {"status": True, "message": message}


def edit_product_data(
    product_id,
    new_product_name=None,
    new_price=None,
    new_description=None,
    new_category_id=None,
    new_brand_id=None,
    new_quantity=None,
    new_image=None,
):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Lấy đối tượng sản phẩm cần chỉnh sửa
    product = session.query(Product).filter_by(product_id=product_id).first()

    if not product:
        message = f"Không tìm thấy sản phẩm với ID {product_id}."
        return {"status": False, "message": message}

    # Cập nhật thông tin của sản phẩm
    if new_product_name is not None:
        product.product_name = new_product_name
    if new_price is not None:
        product.price = new_price
    if new_description is not None:
        product.description = new_description
    if new_category_id is not None:
        product.category_id = new_category_id
    if new_brand_id is not None:
        product.brand_id = new_brand_id
    if new_quantity is not None:
        product.quantity = new_quantity
    if new_image is not None:
        product.image = new_image

    # Commit thay đổi
    session.commit()

    message = f"Đã chỉnh sửa thông tin sản phẩm với ID {product_id}."
    return {"status": True, "message": message}


def delete_product(product_id):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Lấy đối tượng sản phẩm cần xóa
    product = session.query(Product).filter_by(product_id=product_id).first()

    if not product:
        message = f"Không tìm thấy sản phẩm với ID {product_id}."
        return {"status": False, "message": message}

    # Xóa sản phẩm khỏi phiên làm việc
    session.delete(product)

    # Commit thay đổi
    session.commit()

    message = f"Đã xóa sản phẩm với ID {product_id}."
    return {"status": True, "message": message}


def get_product_details(product_id=None, product_name=None):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(Product, Category, Brand).join(Category).join(Brand)

    if product_id is not None:
        query = query.filter(Product.product_id == product_id)
    elif product_name is not None:
        query = query.filter(Product.product_name == product_name)
    else:
        message = "Vui lòng cung cấp ID hoặc tên sản phẩm."
        return {"status": False, "message": message}

    result = query.first()

    if not result:
        message = "Không tìm thấy sản phẩm."
        return {"status": False, "message": message}

    product, category, brand = result

    product_details = {
        "product_id": product.product_id,
        "product_name": product.product_name,
        "price": product.price,
        "description": product.description,
        "category": {
            "category_id": category.category_id,
            "category_name": category.category_name,
        },
        "brand": {"brand_id": brand.brand_id, "brand_name": brand.brand_name},
        "quantity": product.quantity,
        "image": product.image,
        "created_at": product.created_at,
        "updated_at": product.updated_at,
    }

    return {"status": True, "product_details": product_details}


def get_product_overview():
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    products = session.query(Product).all()
    overview = []

    for product in products:
        product_data = {
            "product_name": product.product_name,
            "image": product.image,
            "price": product.price,
            "created_at": product.created_at,
            "updated_at": product.updated_at,
            "discount": None,
        }

        discount = (
            session.query(Discount).filter_by(product_id=product.product_id).first()
        )
        if discount:
            product_data["discount"] = discount.discount_percentage

        overview.append(product_data)

    session.close()

    return overview


###################################################################################
########## interact with the discount  table in database ##########################
###################################################################################


def add_discount_to_product(product_id, discount_percentage, start_date, end_date):
    try:
        # Tạo kết nối đến cơ sở dữ liệu
        engine = create_engine("sqlite:///your_database.db")
        Base.metadata.create_all(engine)

        # Tạo một giảm giá cho sản phẩm
        discount = Discount(
            product_id=product_id,
            discount_percentage=discount_percentage,
            start_date=start_date,
            end_date=end_date,
        )

        # Thêm giảm giá vào sản phẩm
        Session = sessionmaker(bind=engine)
        session = Session()
        product = session.query(Product).get(product_id)  # Lấy sản phẩm theo product_id
        product.discounts.append(discount)

        # Lưu các thay đổi vào cơ sở dữ liệu
        session.commit()
        session.close()

        message = "Thêm giảm giá thành công cho sản phẩm."
        return {"status": True, "message": message}
    except Exception as e:
        message = f"Lỗi trong quá trình thêm giảm giá: {str(e)}"
        return {"status": False, "message": message}
