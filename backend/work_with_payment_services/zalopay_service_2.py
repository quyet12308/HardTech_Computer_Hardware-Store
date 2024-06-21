from time import time
from datetime import datetime
import json, hmac, hashlib, urllib.request, urllib.parse, random

config = {
    "app_id": 2553,
    "key1": "PcY4iZIKFCIdgZvA6ueMcMHHUbRLYjPL",
    "key2": "kLtgPl8HHhfvMuDHPwKfgfsY4Ydm9eIz",
    "endpoint": "https://sb-openapi.zalopay.vn/v2/create",
}
transID = random.randrange(1000000)
order = {
    "app_id": config["app_id"],
    "app_trans_id": "{:%y%m%d}_{}".format(
        datetime.today(), transID
    ),  # mã giao dich có định dạng yyMMdd_xxxx
    "app_user": "user123",
    "app_time": int(round(time() * 1000)),  # miliseconds
    "embed_data": json.dumps({}),
    "item": json.dumps([{}]),
    "amount": 50000,
    "description": "đơn hàng của nhóm 10" + str(transID),
    "bank_code": "zalopayapp",
}

# app_id|app_trans_id|app_user|amount|app_time|embed_data|item
data = "{}|{}|{}|{}|{}|{}|{}".format(
    order["app_id"],
    order["app_trans_id"],
    order["app_user"],
    order["amount"],
    order["app_time"],
    order["embed_data"],
    order["item"],
)

order["mac"] = hmac.new(
    config["key1"].encode(), data.encode(), hashlib.sha256
).hexdigest()

response = urllib.request.urlopen(
    url=config["endpoint"], data=urllib.parse.urlencode(order).encode()
)
result = json.loads(response.read())

for k, v in result.items():
    print("{}: {}".format(k, v))


def handle_callback():
    # Giả lập phản hồi thanh toán tự động thành công
    callback_data = {
        "return_code": 1,
        "return_message": "Success",
        "order_id": "demo_order_id",
        "app_id": config["app_id"],
        "app_trans_id": order["app_trans_id"],
        "mac": hmac.new(
            config["key2"].encode(),
            json.dumps(
                {
                    "return_code": 1,
                    "return_message": "Success",
                    "order_id": "demo_order_id",
                    "app_id": config["app_id"],
                    "app_trans_id": order["app_trans_id"],
                }
            ).encode(),
            hashlib.sha256,
        ).hexdigest(),
    }
    return json.dumps(callback_data)


# Giả lập gọi hàm xử lý phản hồi
callback_response = handle_callback()
print("Callback Response:", callback_response)
