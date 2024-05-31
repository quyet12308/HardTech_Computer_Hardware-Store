from Database_initialization_and_structure import *
from sqlalchemy.orm.exc import NoResultFound

##################################################################
########## interact with the user table in database ##############
##################################################################


def is_admin_user(user_id):
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()
    user = session.query(User).filter(User.user_id == user_id).first()
    if user and user.is_admin:
        return True
    return False


def get_user_id_by_username(username):
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Truy vấn để tìm người dùng theo tên người dùng
    user = session.query(User).filter_by(username=username).first()

    if user is not None:
        return {"status": True, "message": user.user_id}
    else:
        return {"status": False, "message": ""}


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
    username,
    password,
    email,
    fullname=None,
    phone_number=None,
    address=None,
    img=None,
    is_admin=False,
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


def creat_new_data_for_update_user(
    username=None,
    fullname=None,
    phone_number=None,
    address=None,
    img=None,
    password=None,
):
    new_data = {}

    if username is not None:
        check_username = is_username_taken(username=username)
        if check_username:
            message = (
                f"Tên người dùng '{username}' đã được sử dụng, vui lòng chọn tên khác."
            )
            return {"status": False, "message": message}
        else:
            new_data["username"] = username

    if fullname is not None:
        new_data["fullname"] = fullname
    if phone_number is not None:
        new_data["phone_number"] = phone_number
    if address is not None:
        new_data["address"] = address
    if img is not None:
        new_data["img"] = img
    if password is not None:
        new_data["password"] = password

    return {"status": True, "message": new_data}


# update user
def update_user(user_id=None, email=None, new_data=None):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()
    if user_id is not None:
        # Tìm người dùng dựa trên user_id
        user = session.query(User).filter_by(user_id=user_id).first()
    else:
        if email is not None:
            user = session.query(User).filter_by(email=email).first()
        else:
            message = f"Cần truyền vào ít nhất 1 trong 2 thông tin user_id hoặc email để thực hiện truy vấn"
            return {"status": False, "message": message}
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


def get_user(user_id=None, email=None):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Tìm người dùng dựa trên user_id hoặc email
    if user_id:
        user = session.query(User).filter_by(user_id=user_id).first()
        identifier = user_id
    elif email:
        user = session.query(User).filter_by(email=email).first()
        identifier = email
    else:
        return {"status": False, "message": "Vui lòng cung cấp user_id hoặc email"}

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
            "password": user.password,
        }
        return {"status": True, "message": user_info}
    else:
        message = f"Không tìm thấy người dùng với {identifier}."
        return {"status": False, "message": message}


###################################################################################
########## interact with the token (login_session) table in database ##############
###################################################################################


def add_login_session(user_id, token_value, expiration_date):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Tạo đối tượng Token mới
    new_token = Token(
        user_id=user_id, token_value=token_value, expiration_date=expiration_date
    )

    # Thêm đối tượng Token mới vào phiên làm việc và commit thay đổi
    session.add(new_token)
    session.commit()
    session.close()

    messgae = "Thêm phiên đăng nhập thành công"
    return {"status": True, "messgae": messgae}


def get_user_id_from_token(token_value):
    # Tạo session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Lấy thông tin token từ database
        token = session.query(Token).filter(Token.token_value == token_value).one()

        # Kiểm tra nếu token đã hết hạn
        if token.expiration_date <= datetime.now():
            raise Exception("Mã đã hết hạn")

        return {"status": True, "message": token.user_id}

    except NoResultFound:
        raise Exception("Mã không tồn tại")

    except Exception as e:
        raise Exception(str(e))

    finally:
        session.close()


###################################################################################
########## interact with the authentication_codes table in database ###############
###################################################################################


def add_authentication_code(email, code, expiration_time):
    try:
        engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
        Session = sessionmaker(bind=engine)
        session = Session()

        existing_code = session.query(AuthenticationCode).filter_by(email=email).first()

        if existing_code:
            existing_code.code = code
            existing_code.expiration_time = expiration_time
            session.commit()
            message = "Cập nhật code xác thực thành công"
        else:
            new_code = AuthenticationCode(
                email=email, code=code, expiration_time=expiration_time
            )
            session.add(new_code)
            session.commit()
            message = "Thêm code xác thực thành công"

        return {"status": True, "message": message}
    except Exception as e:
        return {"status": False, "message": str(e)}


def query_authentication_code_by_email(email):
    try:
        engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
        Session = sessionmaker(bind=engine)
        session = Session()
        code = (
            session.query(AuthenticationCode)
            .filter_by(email=email)
            .order_by(AuthenticationCode.expiration_time.desc())
            .first()
        )
        if code:
            return {"status": True, "message": code}
        else:
            return {"status": False, "message": "Authentication code not found."}
    except Exception as e:
        return {"status": False, "message": str(e)}
