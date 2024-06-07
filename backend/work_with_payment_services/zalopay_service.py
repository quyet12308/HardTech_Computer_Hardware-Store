import requests
import hashlib
import hmac
import time
import json

# Cấu hình thông tin ZaloPay của bạn
app_id = "2553"
key1 = "PcY4iZIKFCIdgZvA6ueMcMHHUbRLYjPL"
key2 = "kLtgPl8HHhfvMuDHPwKfgfsY4Ydm9eIz"
endpoint = "https://sb-openapi.zalopay.vn/v2/create"

# Thông tin đơn hàng
order_id = "unique_order_id"
amount = 100000  # số tiền thanh toán (đơn vị: VND)
description = "Thanh toán đơn hàng {}".format(order_id)
callback_url = "https://yourwebsite.com/callback"

# Tạo timestamp
timestamp = str(int(time.time() * 1000))

# Tạo dữ liệu yêu cầu
data = {
    "app_id": app_id,
    "app_trans_id": "{}_{}".format(app_id, order_id),
    "app_user": "demo_user",
    "amount": amount,
    "app_time": timestamp,
    "item": json.dumps(
        [
            {
                "itemid": "001",
                "itemname": "Product 1",
                "itemprice": amount,
                "itemquantity": 1,
            }
        ]
    ),
    "embed_data": json.dumps({"promotioninfo": "", "merchantinfo": "extra info"}),
    "description": description,
    "bank_code": "zalopayapp",
    "callback_url": callback_url,
}

# Tạo signature
data_string = "|".join(
    [
        data["app_id"],
        data["app_trans_id"],
        str(data["app_user"]),
        str(data["amount"]),
        str(data["app_time"]),
        str(data["embed_data"]),
        str(data["item"]),
    ]
)
h = hmac.new(key1.encode(), data_string.encode(), hashlib.sha256)
data["mac"] = h.hexdigest()

# Gửi yêu cầu tạo đơn hàng
response = requests.post(endpoint, json=data)
result = response.json()

if result["return_code"] == 1:  # Nếu tạo đơn hàng thành công
    # Chuyển hướng khách hàng tới URL thanh toán của ZaloPay
    order_url = result["order_url"]
    print("Redirect khách hàng tới URL:", order_url)
else:
    print("Lỗi:", result["return_message"])
