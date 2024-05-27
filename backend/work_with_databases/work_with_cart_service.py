from Database_initialization_and_structure import *

###################################################################################
########## interact with the cart and cart_item table in database #################
###################################################################################


def add_to_cart(user_id, product_id, quantity):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    cart = session.query(Cart).filter_by(user_id=user_id).first()
    if cart is None:
        # Nếu chưa tồn tại, tạo mới giỏ hàng cho người dùng
        user = session.query(User).get(user_id)
        cart = Cart(user=user)
        session.add(cart)
        session.commit()

    # Kiểm tra xem sản phẩm đã tồn tại trong giỏ hàng chưa
    cart_item = (
        session.query(CartItem)
        .filter_by(cart_id=cart.id, product_id=product_id)
        .first()
    )
    if cart_item is None:
        # Nếu chưa tồn tại, tạo mới cart item
        product = session.query(Product).get(product_id)
        cart_item = CartItem(cart=cart, product=product, quantity=quantity)
        session.add(cart_item)
    else:
        # Nếu đã tồn tại, cập nhật số lượng
        cart_item.quantity += quantity

    # Cập nhật thời gian cập nhật của giỏ hàng và cart item
    cart.updated_at = datetime.now()
    cart_item.updated_at = datetime.now()

    session.commit()

    message = "Đã thêm sản phẩm vào giỏ hàng thành công."
    return {"status": True, "message": message}


def update_cart_item_quantity(user_id, product_id, quantity):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    cart = session.query(Cart).filter_by(user_id=user_id).first()
    if cart is None:
        # Nếu chưa tồn tại, tạo mới giỏ hàng cho người dùng
        user = session.query(User).get(user_id)
        cart = Cart(user=user)
        session.add(cart)
        session.commit()

    # Kiểm tra xem sản phẩm đã tồn tại trong giỏ hàng chưa
    cart_item = (
        session.query(CartItem)
        .filter_by(cart_id=cart.id, product_id=product_id)
        .first()
    )
    if cart_item is None:
        # Nếu chưa tồn tại, tạo mới cart item
        product = session.query(Product).get(product_id)
        cart_item = CartItem(cart=cart, product=product, quantity=quantity)
        session.add(cart_item)
    else:
        # Nếu đã tồn tại, cập nhật số lượng
        cart_item.quantity = quantity

    # Cập nhật thời gian cập nhật của giỏ hàng và cart item
    cart.updated_at = datetime.now()
    cart_item.updated_at = datetime.now()

    session.commit()

    message = "Đã cập nhật số lượng sản phẩm trong giỏ hàng thành công."
    return {"status": True, "message": message}


def remove_product_from_cart(user_id, product_id):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    cart = session.query(Cart).filter_by(user_id=user_id).first()
    if cart is None:
        # Giỏ hàng không tồn tại
        message = "Giỏ hàng không tồn tại."
        return {"status": False, "message": message}

    # Kiểm tra xem sản phẩm có tồn tại trong giỏ hàng không
    cart_item = (
        session.query(CartItem)
        .filter_by(cart_id=cart.id, product_id=product_id)
        .first()
    )
    if cart_item is None:
        # Sản phẩm không tồn tại trong giỏ hàng
        message = "Sản phẩm không tồn tại trong giỏ hàng."
        return {"status": False, "message": message}

    # Xóa sản phẩm khỏi giỏ hàng
    session.delete(cart_item)

    # Cập nhật thời gian cập nhật của giỏ hàng
    cart.updated_at = datetime.now()

    session.commit()

    message = "Đã xóa sản phẩm khỏi giỏ hàng thành công."
    return {"status": True, "message": message}
