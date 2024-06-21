import json, hmac, hashlib, urllib.request, urllib.parse, random
from datetime import datetime
from time import time


config = {
    "app_id": 2553,
    "key1": "PcY4iZIKFCIdgZvA6ueMcMHHUbRLYjPL",
    "key2": "kLtgPl8HHhfvMuDHPwKfgfsY4Ydm9eIz",
    "endpoint": "https://sb-openapi.zalopay.vn/v2/create",
}


def format_number(number: int):
    number = number + 1
    print(type(number))
    if number < 1_000_000:
        return f"{number:07d}"  # Định dạng số với ít nhất 7 chữ số, bổ sung các số 0 đằng trước nếu cần
    else:
        return str(number)


def create_zalopay_order(
    amount: int,
    description: str,
    redirect_url: str,
    order_id: int,
    user_id: int,
    phone_number: int,
    email: str,
    user_name: str = None,
    full_name: str = None,
):
    order_id = int(order_id)
    amount = int(amount)
    # transID = format_number(number=order_id)
    transID = order_id + 14
    embed_data = {"redirecturl": redirect_url}
    items = []

    order = {
        "app_id": config["app_id"],
        "app_trans_id": "{:%y%m%d}_{}".format(datetime.today(), transID),
        # "app_user": f"{user_id}/{user_name}/{full_name}/{phone_number}/{email}",
        "app_user": f"user123",
        "app_time": int(round(time() * 1000)),
        "embed_data": json.dumps(embed_data),
        "item": json.dumps(items),
        "amount": amount,
        "description": description + str(transID),
        "bank_code": "zalopayapp",
    }

    data_str = "{}|{}|{}|{}|{}|{}|{}".format(
        order["app_id"],
        order["app_trans_id"],
        order["app_user"],
        order["amount"],
        order["app_time"],
        order["embed_data"],
        order["item"],
    )

    order["mac"] = hmac.new(
        config["key1"].encode(), data_str.encode(), hashlib.sha256
    ).hexdigest()
    print(order)
    response = urllib.request.urlopen(
        url=config["endpoint"], data=urllib.parse.urlencode(order).encode()
    )
    result = json.loads(response.read())
    if result["return_code"] == 1:
        return {"result": result, "checksum": order["app_trans_id"]}
    else:
        print(result)
        return None


# a = format_number(number="2")
# print(a)

# a = create_zalopay_order(
#     amount=20000,
#     description="Khách hàng Đỗ Thị Phương Anh thanh toán cho đơn hàng id 3 của shop Hardtech6",
#     email="quyet12306@gmail.com",
#     full_name="Tran Dang Quyet",
#     order_id=2,
#     phone_number="123456789",
#     redirect_url="http://127.0.0.1:5500/in_bill.html",
#     user_id=4,
#     user_name="user2",
# )
# print(a)
