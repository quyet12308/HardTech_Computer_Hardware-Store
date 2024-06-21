from Database_initialization_and_structure import *
from decimal import Decimal
from sqlalchemy.orm import joinedload


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


# def create_order(user_id, order_details):
#     """
#     Thêm một đơn hàng mới vào cơ sở dữ liệu.

#     Args:
#         user_id (int): ID của người dùng tạo đơn hàng.
#         order_details (list of dict): Danh sách các chi tiết đơn hàng, mỗi chi tiết là một dict có các keys:
#                                       - product_id (int)
#                                       - qty (int)
#                                       - order_price (numeric)
#     """
#     try:
#         engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
#         Session = sessionmaker(bind=engine)
#         session = Session()
#         # Tính tổng giá của đơn hàng
#         total_price = sum(item["qty"] * item["order_price"] for item in order_details)
#         order_status = "unpaid"
#         # Tạo đối tượng Order
#         new_order = Order(
#             user_id=user_id, order_status=order_status, total_price=total_price
#         )
#         session.add(new_order)
#         session.commit()  # Lưu để lấy order_id

#         # Tạo các đối tượng OrderDetail
#         for item in order_details:
#             new_order_detail = OrderDetail(
#                 order_id=new_order.order_id,
#                 product_id=item["product_id"],
#                 qty=item["qty"],
#                 order_price=item["order_price"],
#             )
#             session.add(new_order_detail)

#         # Lưu các chi tiết đơn hàng
#         session.commit()
#         return {"status": True, "message": "Đơn hàng được thêm thành công!"}
#     except Exception as e:
#         session.rollback()
#         return {"status": False, "message": f"Có lỗi xảy ra: {e}"}
#     finally:
#         session.close()


def create_order(user_id: int, order_details: list):
    """
    Thêm một đơn hàng mới vào cơ sở dữ liệu.

    Args:
        user_id (int): ID của người dùng tạo đơn hàng.
        order_details (list of dict): Danh sách các chi tiết đơn hàng, mỗi chi tiết là một dict có các keys:
                                      - product_id (int)
                                      - qty (int)
                                      - order_price (numeric)

    Returns:
        dict: Trạng thái và thông báo, kèm theo order_id nếu tạo thành công.
    """
    try:
        engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
        Session = sessionmaker(bind=engine)
        session = Session()
        # Tính tổng giá của đơn hàng
        total_price = sum(item["qty"] * item["order_price"] for item in order_details)
        order_status = "unpaid"
        # Tạo đối tượng Order
        new_order = Order(
            user_id=user_id,
            order_status=order_status,
            total_price=Decimal(total_price),
            order_note="",
            order_address="",
            checksum="",
        )
        session.add(new_order)
        session.commit()  # Lưu để lấy order_id

        # Tạo các đối tượng OrderDetail
        for item in order_details:
            new_order_detail = OrderDetail(
                order_id=new_order.order_id,
                product_id=item["product_id"],
                qty=item["qty"],
                order_price=Decimal(item["order_price"]),
            )
            session.add(new_order_detail)

            # Lưu các chi tiết đơn hàng
        session.commit()
        return {
            "status": True,
            "message": "Đơn hàng được thêm thành công!",
            "order_id": new_order.order_id,
        }
    except Exception as e:
        session.rollback()
        return {"status": False, "message": f"Có lỗi xảy ra: {e}"}


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


def update_order_after_payment_success(
    order_id, order_status=None, order_note=None, order_address=None, checksum=None
):
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        # Tìm đơn hàng theo order_id
        order = session.query(Order).filter_by(order_id=order_id).one_or_none()

        if order is None:
            return {
                "status": False,
                "message": f"Order with id {order_id} does not exist.",
            }

        # Cập nhật thông tin nếu giá trị không phải None
        if order_status is not None:
            order.order_status = order_status

        if order_note is not None:
            order.order_note = order_note

        if order_address is not None:
            order.order_address = order_address
        if checksum is not None:
            order.checksum = checksum

        # Lưu thay đổi vào cơ sở dữ liệu
        session.commit()

        return {
            "status": True,
            "message": f"Order {order_id} has been updated successfully.",
        }
    except Exception as e:
        session.rollback()
        return {"status": False, "message": f"An error occurred: {e}"}
    finally:
        session.close()


def update_order_status_using_checksum(checksum, new_status):
    try:
        engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
        Session = sessionmaker(bind=engine)
        session = Session()
        # Tìm đơn hàng theo checksum
        order = session.query(Order).filter_by(checksum=checksum).one_or_none()

        if order is None:
            return {
                "status": False,
                "message": f"Order with checksum {checksum} does not exist.",
            }

        # Cập nhật order_status
        order.order_status = new_status

        # Lưu thay đổi vào cơ sở dữ liệu
        session.commit()

        return {
            "status": True,
            "message": f"Order status for checksum {checksum} has been updated to {new_status}.",
        }
    except Exception as e:
        session.rollback()
        return {"status": False, "message": f"An error occurred: {e}"}
    finally:
        session.close()


def get_order_id_by_checksum(checksum):
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        # Tìm đơn hàng theo checksum
        order = session.query(Order).filter_by(checksum=checksum).one_or_none()

        if order is None:
            return {
                "status": False,
                "message": f"Order with checksum {checksum} does not exist.",
            }

        # Trả về order_id
        return {"status": True, "message": order.order_id}
    except Exception as e:
        return {"status": False, "message": f"An error occurred: {e}"}
    finally:
        session.close()


def get_order_info_by_checksum(checksum):
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        # Truy vấn đơn hàng theo checksum và tải kèm các thông tin liên quan
        order = (
            session.query(Order)
            .filter_by(checksum=checksum)
            .options(
                joinedload(Order.user),
                joinedload(Order.order_details).joinedload(OrderDetail.product),
            )
            .one_or_none()
        )

        if order is None:
            return {
                "status": False,
                "message": f"Order with checksum {checksum} does not exist.",
            }

        # Lấy thông tin người dùng
        user_info = {
            "fullname": order.user.fullname,
            "order_address": order.order_address,
            "order_note": order.order_note,
            "order_total_price": order.total_price,
        }

        # Lấy thông tin chi tiết đơn hàng
        order_details = []
        for detail in order.order_details:
            product = (
                session.query(Product).filter_by(product_id=detail.product_id).one()
            )
            order_details.append(
                {
                    "product_name": product.product_name,
                    "qty": detail.qty,
                    "order_price": detail.order_price,
                }
            )

        # Tạo kết quả
        result = {"user_info": user_info, "order_details": order_details}

        return {"status": True, "message": result}
    except Exception as e:
        return {"status": False, "message": f"An error occurred: {e}"}
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


# def get_order_details( order_id: int):
#     engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     # Truy vấn lấy đơn hàng với order_id
#     order = session.query(Order).filter(Order.order_id == order_id).first()
#     if not order:
#         return None

#     # Lấy thông tin chi tiết của đơn hàng
#     order_details = session.query(OrderDetail).filter(OrderDetail.order_id == order_id).all()

#     # Tạo dictionary chứa thông tin đơn hàng và chi tiết đơn hàng
#     order_info = {
#         "order_id": order.order_id,
#         "user_id": order.user_id,
#         "order_date": order.order_date,
#         "total_price": order.total_price,
#         "order_status": order.order_status,
#         "order_details": []
#     }

#     for detail in order_details:
#         order_info["order_details"].append({
#             "order_detail_id": detail.order_detail_id,
#             "product_id": detail.product_id,
#             "qty": detail.qty,
#             "order_price": detail.order_price
#         })

#     return order_info


def get_order_details(order_id: int):
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Truy vấn lấy đơn hàng với order_id và tải thêm thông tin user và order_details
    order = (
        session.query(Order)
        .options(joinedload(Order.user), joinedload(Order.order_details))
        .filter(Order.order_id == order_id)
        .first()
    )

    if not order:
        return None

    # Tạo dictionary chứa thông tin đơn hàng và chi tiết đơn hàng
    order_info = {
        "order_id": order.order_id,
        "user_id": order.user_id,
        "order_date": order.order_date,
        "total_price": order.total_price,
        "order_status": order.order_status,
        "user": {
            "fullname": order.user.fullname,
            "email": order.user.email,
            "phone_number": order.user.phone_number,
            "address": order.user.address,
        },
        "order_details": [],
    }

    for detail in order.order_details:
        product = (
            session.query(Product)
            .filter(Product.product_id == detail.product_id)
            .first()
        )
        order_info["order_details"].append(
            {
                "order_detail_id": detail.order_detail_id,
                "product_id": detail.product_id,
                "product_name": product.product_name if product else None,
                "product_image": product.image if product else None,
                "qty": detail.qty,
                "order_price": detail.order_price,
            }
        )

    return order_info


def get_order_details_2(order_id):
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()
    # Truy vấn đơn hàng
    order = session.query(Order).filter(Order.order_id == order_id).first()

    if not order:
        return {"error": "Order not found"}

    # Truy vấn chi tiết đơn hàng
    order_details = (
        session.query(OrderDetail, Product)
        .join(Product, OrderDetail.product_id == Product.product_id)
        .filter(OrderDetail.order_id == order_id)
        .all()
    )

    # Tổng hợp thông tin sản phẩm và tổng giá tiền
    products_info = []
    total_price = 0

    for detail, product in order_details:
        product_info = {
            "product_name": product.product_name,
            "quantity": detail.qty,
            "unit_price": detail.order_price,
        }
        products_info.append(product_info)
        total_price += detail.qty * detail.order_price

    # Trả lại kết quả
    result = {"products": products_info, "total_price": total_price}

    return result
