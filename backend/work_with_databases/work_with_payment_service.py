from Database_initialization_and_structure import *

###################################################################################
########## interact with the payment_details table in database ####################
###################################################################################


def add_payment(order_id, amount, provider, status):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Kiểm tra xem đơn hàng đã tồn tại hay chưa
    order = session.query(Order).filter(Order.order_id == order_id).first()

    if not order:
        # Nếu đơn hàng không tồn tại, trả về thông báo lỗi
        message = "Đơn hàng không tồn tại."
        return {"status": False, "message": message}

    # Tạo một payment detail mới
    payment_detail = PaymentDetail(
        order_id=order_id, amount=float(amount), provider=provider, status=status
    )
    session.add(payment_detail)
    session.commit()

    message = "Đã thêm thanh toán thành công."
    return {"status": True, "message": message}


def edit_payment(payment_id, amount=None, provider=None, status=None):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Kiểm tra xem thanh toán có tồn tại hay không
    payment = (
        session.query(PaymentDetail).filter(PaymentDetail.id == payment_id).first()
    )

    if not payment:
        # Nếu thanh toán không tồn tại, trả về thông báo lỗi
        message = "Thanh toán không tồn tại."
        return {"status": False, "message": message}

    # Cập nhật thông tin thanh toán nếu tham số được truyền vào
    if amount is not None:
        payment.amount = float(amount)
    if provider is not None:
        payment.provider = provider
    if status is not None:
        payment.status = status

    session.commit()

    message = "Đã sửa thông tin thanh toán thành công."
    return {"status": True, "message": message}


def delete_payment(payment_id):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Kiểm tra xem thanh toán có tồn tại hay không
    payment = (
        session.query(PaymentDetail).filter(PaymentDetail.id == payment_id).first()
    )

    if not payment:
        # Nếu thanh toán không tồn tại, trả về thông báo lỗi
        message = "Thanh toán không tồn tại."
        return {"status": False, "message": message}

    # Xóa thanh toán
    session.delete(payment)
    session.commit()

    message = "Đã xóa thông tin thanh toán thành công."
    return {"status": True, "message": message}
