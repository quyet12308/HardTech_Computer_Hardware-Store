from Database_initialization_and_structure import *

from sqlalchemy import create_engine, func, extract
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import calendar
from setting import *

# Kết nối đến cơ sở dữ liệu SQLite
DATABASE_URL = (
    f"sqlite:///{DATA_BASE_PATH}"  # Thay thế bằng đường dẫn tới cơ sở dữ liệu của bạn
)
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def get_statistics(timeframe: str):
    # Lấy thời gian hiện tại
    now = datetime.now()

    # Xác định khoảng thời gian bắt đầu và kết thúc dựa trên tham số 'timeframe'
    if timeframe == "week":
        start_date = now - timedelta(days=now.weekday())  # Ngày đầu tuần
        end_date = start_date + timedelta(days=6)  # Ngày cuối tuần
    elif timeframe == "month":
        start_date = now.replace(day=1)  # Ngày đầu tháng
        end_date = now.replace(
            day=calendar.monthrange(now.year, now.month)[1]
        )  # Ngày cuối tháng
    elif timeframe == "quarter":
        quarter = (now.month - 1) // 3 + 1
        start_date = datetime(now.year, 3 * (quarter - 1) + 1, 1)  # Ngày đầu quý
        end_date = datetime(
            now.year, 3 * quarter, calendar.monthrange(now.year, 3 * quarter)[1]
        )  # Ngày cuối quý
    else:
        raise ValueError(
            "Invalid timeframe. Please choose from 'week', 'month', or 'quarter'."
        )

    # Truy vấn số lượng user mới đăng ký
    new_users = (
        session.query(User)
        .filter(User.created_at.between(start_date, end_date))
        .count()
    )

    # Truy vấn số lượng đơn đặt hàng mới
    new_orders = (
        session.query(Order)
        .filter(Order.order_date.between(start_date, end_date))
        .count()
    )

    # Truy vấn tổng doanh thu
    total_revenue = (
        session.query(func.sum(Order.total_price))
        .filter(Order.order_date.between(start_date, end_date))
        .scalar()
    )

    # Truy vấn số lượng sản phẩm mới nhập vào kho
    new_products = (
        session.query(Product)
        .filter(Product.created_at.between(start_date, end_date))
        .count()
    )

    return {
        "new_users": new_users,
        "new_orders": new_orders,
        "total_revenue": total_revenue,
        "new_products": new_products,
    }


def get_data_for_lineChart_by_period(period: str):
    now = datetime.now()

    if period == "week":
        start_date = now - timedelta(weeks=1)
    elif period == "month":
        start_date = now - timedelta(days=30)
    elif period == "quarter":
        start_date = now - timedelta(days=90)
    else:
        raise ValueError("Invalid period. Must be 'week', 'month', or 'quarter'.")

    # Truy vấn doanh thu và đơn hàng theo khoảng thời gian
    revenue_query = (
        session.query(
            extract("month", Order.order_date).label("month"),
            func.sum(Order.total_price).label("total_revenue"),
        )
        .filter(Order.order_date >= start_date)
        .group_by(extract("month", Order.order_date))
        .all()
    )

    order_query = (
        session.query(
            extract("month", Order.order_date).label("month"),
            func.count(Order.order_id).label("total_orders"),
        )
        .filter(Order.order_date >= start_date)
        .group_by(extract("month", Order.order_date))
        .all()
    )

    # Định dạng dữ liệu để sử dụng trong biểu đồ
    revenue_data = {item.month: item.total_revenue for item in revenue_query}
    order_data = {item.month: item.total_orders for item in order_query}

    chart_labels = list(revenue_data.keys())
    revenue_values = list(revenue_data.values())
    order_values = list(order_data.values())

    chart_data = {
        "labels": chart_labels,
        "datasets": [
            {
                "label": "Doanh thu",
                "data": revenue_values,
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1,
                "fill": False,
            },
            {
                "label": "Đơn hàng",
                "data": order_values,
                "borderColor": "rgba(153, 102, 255, 1)",
                "borderWidth": 1,
                "fill": False,
            },
        ],
    }
    # lineChart_data_json = json.dumps(chart_data, use_decimal=True, ensure_ascii=False)

    # return lineChart_data_json
    return chart_data


def get_data_for_pieChart_by_period(period: str):
    now = datetime.now()

    if period == "week":
        start_date = now - timedelta(weeks=1)
    elif period == "month":
        start_date = now - timedelta(days=30)
    elif period == "quarter":
        start_date = now - timedelta(days=90)
    else:
        raise ValueError("Invalid period. Must be 'week', 'month', or 'quarter'.")

    # Truy vấn doanh thu và đơn hàng theo khoảng thời gian
    revenue_query = (
        session.query(
            extract("month", Order.order_date).label("month"),
            func.sum(Order.total_price).label("total_revenue"),
        )
        .filter(Order.order_date >= start_date)
        .group_by(extract("month", Order.order_date))
        .all()
    )

    order_query = (
        session.query(
            extract("month", Order.order_date).label("month"),
            func.count(Order.order_id).label("total_orders"),
        )
        .filter(Order.order_date >= start_date)
        .group_by(extract("month", Order.order_date))
        .all()
    )

    # Truy vấn số lượng sản phẩm bán chạy nhất
    product_query = (
        session.query(
            Product.product_name, func.sum(OrderDetail.qty).label("total_quantity")
        )
        .join(OrderDetail, OrderDetail.product_id == Product.product_id)
        .join(Order, OrderDetail.order_id == Order.order_id)
        .filter(Order.order_date >= start_date)
        .group_by(Product.product_name)
        .order_by(func.sum(OrderDetail.qty).desc())
        .limit(4)
        .all()
    )  # Lấy 4 sản phẩm bán chạy nhất

    # Định dạng dữ liệu để sử dụng trong biểu đồ
    revenue_data = {item.month: item.total_revenue for item in revenue_query}
    order_data = {item.month: item.total_orders for item in order_query}
    product_data = {item.product_name: item.total_quantity for item in product_query}

    product_labels = list(product_data.keys())
    product_values = list(product_data.values())

    pie_chart_data = {
        "labels": product_labels,
        "datasets": [
            {
                "data": product_values,
                "backgroundColor": [
                    "rgba(255, 99, 132, 0.2)",
                    "rgba(54, 162, 235, 0.2)",
                    "rgba(255, 206, 86, 0.2)",
                    "rgba(75, 192, 192, 0.2)",
                ],
                "borderColor": [
                    "rgba(255, 99, 132, 1)",
                    "rgba(54, 162, 235, 1)",
                    "rgba(255, 206, 86, 1)",
                    "rgba(75, 192, 192, 1)",
                ],
                "borderWidth": 1,
            }
        ],
    }

    # pie_chart_data_json = json.dumps(
    #     pie_chart_data, use_decimal=True, ensure_ascii=False
    # )

    # return pie_chart_data_json
    return pie_chart_data


def get_data_for_barChart_data_by_period(time_period: str):
    """
    Hàm lấy dữ liệu để vẽ biểu đồ theo khoảng thời gian.
    :param time_period: Khoảng thời gian ('week', 'month', 'quarter')
    :return: Dữ liệu cho biểu đồ
    """
    now = datetime.now()

    if time_period == "week":
        start_date = now - timedelta(weeks=1)
    elif time_period == "month":
        start_date = now - timedelta(days=30)
    elif time_period == "quarter":
        start_date = now - timedelta(days=90)
    else:
        raise ValueError("Time period must be 'week', 'month', or 'quarter'")

    # Truy vấn dữ liệu từ cơ sở dữ liệu theo khoảng thời gian
    results = (
        session.query(
            Product.product_name, func.sum(OrderDetail.qty).label("total_qty")
        )
        .join(OrderDetail, Product.product_id == OrderDetail.product_id)
        .join(Order, Order.order_id == OrderDetail.order_id)
        .filter(Order.order_date >= start_date)
        .group_by(Product.product_name)
        .order_by(func.sum(OrderDetail.qty).desc())
        .all()
    )

    # Chuẩn bị dữ liệu cho biểu đồ
    labels = [result.product_name for result in results]
    data = [result.total_qty for result in results]

    chart_data = {
        "labels": labels,
        "datasets": [
            {
                "label": "Số lượng sản phẩm trong kho",
                "data": data,
                "backgroundColor": [
                    "rgba(255, 99, 132, 0.2)",
                    "rgba(54, 162, 235, 0.2)",
                    "rgba(255, 206, 86, 0.2)",
                    "rgba(75, 192, 192, 0.2)",
                ],
                "borderColor": [
                    "rgba(255, 99, 132, 1)",
                    "rgba(54, 162, 235, 1)",
                    "rgba(255, 206, 86, 1)",
                    "rgba(75, 192, 192, 1)",
                ],
                "borderWidth": 1,
            }
        ],
    }

    # barChart_data_json = json.dumps(chart_data, use_decimal=True, ensure_ascii=False)

    # return barChart_data_json
    return chart_data
