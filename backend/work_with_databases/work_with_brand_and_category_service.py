from Database_initialization_and_structure import *

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

    existing_category = (
        session.query(Category).filter_by(category_name=category_name).first()
    )

    return existing_category is not None


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


def query_category_by_name(category_name):
    try:
        # Tạo engine để kết nối đến CSDL
        engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
        Session = sessionmaker(bind=engine)
        session = Session()

        # Truy vấn danh mục dựa trên tên danh mục
        category = (
            session.query(Category).filter_by(category_name=category_name).first()
        )
        session.close()
        if category:

            return {"status": True, "messgae": category}
        else:
            message = "Category not found."
            return {"status": False, "messgae": message}

    except SQLAlchemyError as e:
        message = f"An error occurred: {str(e)}"
        return {"status": False, "messgae": message}


# def get_unique_category_and_brand_names():
#     # Tạo engine để kết nối đến CSDL
#     engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     category_names = session.query(Category.category_name).distinct().all()
#     brand_names = session.query(Brand.brand_name).distinct().all()

#     category_names = [name[0] for name in category_names]
#     brand_names = [name[0] for name in brand_names]

#     # return category_names, brand_names
#     return {"category_names": category_names, "brand_names": brand_names}


def get_unique_category_and_brand_names():
    # Tạo engine để kết nối đến CSDL
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    categories = (
        session.query(Category.category_id, Category.category_name).distinct().all()
    )
    brands = session.query(Brand.brand_id, Brand.brand_name).distinct().all()

    category_list = [
        {"id": category_id, "name": category_name}
        for category_id, category_name in categories
    ]
    brand_list = [
        {"id": brand_id, "name": brand_name} for brand_id, brand_name in brands
    ]

    return {"categories": category_list, "brands": brand_list}
