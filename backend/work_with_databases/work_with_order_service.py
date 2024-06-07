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


def compress_order_items(dict_order_item: dict, compressed_items: list):

    return compressed_items.append(dict_order_item)


def create_order(user_id, order_details):
    """
    Thêm một đơn hàng mới vào cơ sở dữ liệu.

    Args:
        user_id (int): ID của người dùng tạo đơn hàng.
        order_details (list of dict): Danh sách các chi tiết đơn hàng, mỗi chi tiết là một dict có các keys:
                                      - product_id (int)
                                      - qty (int)
                                      - order_price (numeric)
    """
    try:
        engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
        Session = sessionmaker(bind=engine)
        session = Session()
        # Tính tổng giá của đơn hàng
        total_price = sum(item["qty"] * item["order_price"] for item in order_details)
        order_status = "already paid"
        # Tạo đối tượng Order
        new_order = Order(
            user_id=user_id, order_status=order_status, total_price=total_price
        )
        session.add(new_order)
        session.commit()  # Lưu để lấy order_id

        # Tạo các đối tượng OrderDetail
        for item in order_details:
            new_order_detail = OrderDetail(
                order_id=new_order.order_id,
                product_id=item["product_id"],
                qty=item["qty"],
                order_price=item["order_price"],
            )
            session.add(new_order_detail)

        # Lưu các chi tiết đơn hàng
        session.commit()
        return {"status": True, "message": "Đơn hàng được thêm thành công!"}
    except Exception as e:
        session.rollback()
        return {"status": False, "message": f"Có lỗi xảy ra: {e}"}
    finally:
        session.close()


def update_order_status(order_id, new_status):
    """
    Cập nhật trạng thái của một đơn đặt hàng.

    Parameters:
    - order_id (int): ID của đơn đặt hàng cần cập nhật.
    - new_status (str): Trạng thái mới cho đơn đặt hàng.

    Returns:
    - order (Order): Đối tượng Order đã được cập nhật.
    """
    try:
        engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
        Session = sessionmaker(bind=engine)
        session = Session()
        # Tìm order theo order_id
        order = session.query(Order).filter_by(order_id=order_id).one_or_none()

        if order is None:
            print(f"Không tìm thấy đơn đặt hàng với ID: {order_id}")
            return {
                "status": False,
                "message": "Có lỗi xảy ra: Không tìm thấy đơn hàng id {}".format(
                    order_id
                ),
            }

        # Cập nhật trạng thái của order
        order.order_status = new_status
        session.commit()

        print(
            f"Đã cập nhật trạng thái của đơn đặt hàng ID: {order_id} thành {new_status}"
        )
        return {
            "status": True,
            "message": "Đơn hàng được cập nhật trạng thái thành công!",
        }

    except Exception as e:
        session.rollback()
        print(f"Có lỗi xảy ra khi cập nhật trạng thái đơn đặt hàng: {e}")
        return {"status": False, "messgae": f"Có lỗi xảy ra: {e}"}

    finally:
        session.close()


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
