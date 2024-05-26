from Database_initialization_and_structure import *

###################################################################################
########## interact with the cart and cart_item table in database #################
###################################################################################


def add_to_cart(user_id, product_id, quantity):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Kiểm tra xem giỏ hàng của người dùng đã tồn tại hay chưa
    cart = session.query(Cart).filter(Cart.user_id == user_id).first()

    if not cart:
        # Tạo giỏ hàng mới nếu chưa tồn tại
        cart = Cart(user_id=user_id, total=0)
        session.add(cart)
        session.commit()

    # Kiểm tra xem sản phẩm đã tồn tại trong giỏ hàng chưa
    cart_item = (
        session.query(CartItem)
        .filter(CartItem.cart_id == cart.id, CartItem.product_id == product_id)
        .first()
    )

    if cart_item:
        # Nếu sản phẩm đã tồn tại trong giỏ hàng, cập nhật số lượng
        cart_item.quantity += quantity
    else:
        # Nếu sản phẩm chưa tồn tại trong giỏ hàng, tạo mới
        cart_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
        session.add(cart_item)

    # Cập nhật tổng số lượng sản phẩm trong giỏ hàng
    cart.total += quantity

    session.commit()

    message = "Đã thêm sản phẩm vào giỏ hàng thành công."
    return {"status": True, "message": message}
