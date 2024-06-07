# import requests

# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "Bearer access_token$sandbox$59drszcdbjr6qktw$e79debd0a5c6ab0c60fe6770b85eb9ec",
#     # "Authorization": "Basic AagNCkpM0282tL9fF7OwKcjo8IoHchNQb2SAlxtWfPHeRZ2ricbbv5cjydCMgOdrZr4OT9Rr68BtlOV9:EJ3Aj2GXoiqlsOCmG5jzwt55pAaKH470ENXiR8Q9AndWZWpukvMUBIX8vPCWxMTCfAOSEds5ED7tJgMd",
# }

# response = requests.get(
#     "https://api-m.sandbox.paypal.com/v2/payments/authorizations/83PKG4TRLBLCA",
#     headers=headers,
# )
# # In mã phản hồi HTTP
# print(f"HTTP Response Code: {response.status_code}")

# # In chi tiết lỗi
# print(f"Error Message: {response.text}")

# coding=utf-8
# Python 3.6

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
print(random.randrange(1000000))
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
    "description": "đơn hàng của lâm" + str(transID),
    "bank_code": "zalopayapp",
}

# app_id|app_trans_id|app_user|amount|apptime|embed_data|item
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
