import hashlib
import urllib.parse
import requests
from datetime import datetime


def create_vnpay_payment_url(order_id, amount, return_url, vnpay_config):
    vnpay_params = {
        "vnp_Version": "2.1.0",
        "vnp_Command": "pay",
        "vnp_TmnCode": vnpay_config["vnp_TmnCode"],
        "vnp_Amount": str(amount * 100),  # Quy đổi sang đơn vị VND nhỏ nhất
        "vnp_CurrCode": "VND",
        "vnp_TxnRef": order_id,
        "vnp_OrderInfo": "Thanh toan don hang {}".format(order_id),
        "vnp_OrderType": "other",
        "vnp_Locale": "vn",
        "vnp_ReturnUrl": return_url,
        "vnp_IpAddr": "127.0.0.1",  # IP của người dùng
        "vnp_CreateDate": datetime.now().strftime("%Y%m%d%H%M%S"),
    }

    # Sắp xếp các tham số theo thứ tự từ điển
    sorted_vnpay_params = sorted(vnpay_params.items())

    # Tạo query string
    query_string = "&".join(
        [
            "{}={}".format(k, urllib.parse.quote_plus(str(v)))
            for k, v in sorted_vnpay_params
        ]
    )

    # Tạo URL
    hash_data = query_string
    secure_hash = hashlib.sha256(
        (vnpay_config["vnp_HashSecret"] + hash_data).encode("utf-8")
    ).hexdigest()
    payment_url = (
        vnpay_config["vnp_Url"]
        + "?"
        + query_string
        + "&vnp_SecureHashType=SHA256&vnp_SecureHash="
        + secure_hash
    )

    return payment_url


# Cấu hình VNPAY
vnpay_config = {
    "vnp_TmnCode": "1T1ZDPPG",
    "vnp_HashSecret": "EKFCVOAIWKHETSKIDMWSRBZLSDYPWOKC",
    "vnp_Url": "https://sandbox.vnpayment.vn/paymentv2/vpcpay.html",
}

# Thông tin đơn hàng
order_id = "123456"
amount = 100000  # Số tiền cần thanh toán (VND)
return_url = "https://yourwebsite.com/return_url"

# Tạo URL thanh toán
payment_url = create_vnpay_payment_url(order_id, amount, return_url, vnpay_config)
print(payment_url)
