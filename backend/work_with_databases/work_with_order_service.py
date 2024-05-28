from Database_initialization_and_structure import *


###################################################################################
########## interact with the order and order_detail table in database #############
###################################################################################


def compress_order_items(product_ids, quantities, unit_prices):
    compressed_items = []
    if len(product_ids) == len(quantities) and len(quantities) == len(unit_prices):
        for i in range(len(product_ids)):
            compressed_item = {
                "product_id": product_ids[i],
                "quantity": quantities[i],
                "unit_price": unit_prices[i],
            }
            compressed_items.append(compressed_item)
        return {"status": True, "message": compressed_items}
    else:
        message = f"Số lượng của các thông số truyền vào không bằng nhau"
        return {"status": False, "message": message}


def add_order(
    user_id, order_status, total_price, shipping_address, payment_method, order_items
):
    if order_items["status"] == False:
        return {"status": False, "message": order_items["message"]}
    else:
        # Tạo engine và phiên làm việc
        engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
        Session = sessionmaker(bind=engine)
        session = Session()

        # Tạo đối tượng đơn hàng mới
        order = Order(
            user_id=user_id,
            order_status=order_status,
            total_price=total_price,
            shipping_address=shipping_address,
            payment_method=payment_method,
        )

        # Thêm đơn hàng vào phiên làm việc
        session.add(order)

        # Commit thay đổi để lấy order_id mới được tạo
        session.commit()
        order_item_datas = order_items["message"]
        # Lặp qua các mục trong đơn hàng và tạo đối tượng chi tiết đơn hàng
        for item in order_item_datas:
            product_id = int(item["product_id"])
            quantity = int(item["quantity"])
            unit_price = int(item["unit_price"])

            # Tạo đối tượng chi tiết đơn hàng mới
            order_detail = OrderDetail(
                order_id=order.order_id,
                product_id=product_id,
                quantity=quantity,
                unit_price=unit_price,
            )

            # Thêm chi tiết đơn hàng vào phiên làm việc
            session.add(order_detail)

        # Commit thay đổi cuối cùng
        session.commit()

        message = "Đã thêm đơn hàng thành công."
        return {"status": True, "message": message}


def edit_order(
    order_id,
    user_id=None,
    order_status=None,
    total_price=None,
    shipping_address=None,
    payment_method=None,
    order_items=None,
):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Tìm đơn hàng cần chỉnh sửa
    order = session.query(Order).get(order_id)

    if not order:
        return {"status": False, "message": "Đơn hàng không tồn tại."}

    # Cập nhật thông tin đơn hàng
    if user_id is not None:
        order.user_id = user_id
    if order_status is not None:
        order.order_status = order_status
    if total_price is not None:
        order.total_price = total_price
    if shipping_address is not None:
        order.shipping_address = shipping_address
    if payment_method is not None:
        order.payment_method = payment_method

    # Thêm lại chi tiết đơn hàng mới
    if order_items is not None:
        # Xóa chi tiết đơn hàng cũ
        session.query(OrderDetail).filter(OrderDetail.order_id == order_id).delete()
        order_item_datas = order_items["message"]
        for item in order_item_datas:
            product_id = int(item["product_id"])
            quantity = int(item["quantity"])
            unit_price = int(item["unit_price"])

            order_detail = OrderDetail(
                order_id=order_id,
                product_id=product_id,
                quantity=quantity,
                unit_price=unit_price,
            )

            session.add(order_detail)

    # Commit thay đổi cuối cùng
    session.commit()

    message = "Đã chỉnh sửa đơn hàng thành công."
    return {"status": True, "message": message}


def delete_order(order_id):
    # Tạo engine và phiên làm việc
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Tìm đơn hàng theo order_id
    order = session.query(Order).filter(Order.order_id == order_id).first()

    if order:
        # Xóa các chi tiết đơn hàng liên quan
        session.query(OrderDetail).filter(OrderDetail.order_id == order_id).delete()

        # Xóa đơn hàng
        session.delete(order)
        session.commit()

        message = "Đã xóa đơn hàng thành công."
        return {"status": True, "message": message}
    else:
        message = "Không tìm thấy đơn hàng."
        return {"status": False, "message": message}


def add_order_statuses(status_list):
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    message = ""
    for status in status_list:
        existing_status = session.query(OrderStatus).filter_by(status=status).first()
        if existing_status:
            session.close()
            return {"status": False, "message": f"Trạng thái '{status}' đã tồn tại."}

        new_status = OrderStatus(status=status)
        session.add(new_status)

    session.commit()
    session.close()
    return {"status": True, "message": "Thêm trạng thái đơn hàng thành công."}
