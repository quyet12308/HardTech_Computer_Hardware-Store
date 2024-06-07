import hashlib
import hmac
import json
import requests
import uuid
from datetime import datetime

# Thông tin từ MoMo
endpoint = "https://test-payment.momo.vn/v2/gateway/api/create"
partnerCode = "MOMOXNXXXX20210528"
accessKey = "F8BBA842ECF85"
secretKey = "K951B6PE1waDMi640xX08PD3vg6EkVlz"
orderInfo = "Thanh toán đơn hàng"
redirectUrl = "https://webhook.site/redirect"
ipnUrl = "https://webhook.site/ipn"
amount = "10000"
orderId = str(uuid.uuid4())
requestId = str(uuid.uuid4())
requestType = "captureWallet"
extraData = ""  # Bạn có thể truyền thêm dữ liệu nếu cần thiết

# Tạo raw signature
raw_signature = f"accessKey={accessKey}&amount={amount}&extraData={extraData}&ipnUrl={ipnUrl}&orderId={orderId}&orderInfo={orderInfo}&partnerCode={partnerCode}&redirectUrl={redirectUrl}&requestId={requestId}&requestType={requestType}"

# Mã hóa signature bằng Hmac SHA256
signature = hmac.new(
    bytes(secretKey, "utf-8"), bytes(raw_signature, "utf-8"), hashlib.sha256
).hexdigest()

# Tạo payload gửi đến MoMo
data = {
    "partnerCode": partnerCode,
    "partnerName": "Test",
    "storeId": "MomoTestStore",
    "requestId": requestId,
    "amount": amount,
    "orderId": orderId,
    "orderInfo": orderInfo,
    "redirectUrl": redirectUrl,
    "ipnUrl": ipnUrl,
    "lang": "vi",
    "extraData": extraData,
    "requestType": requestType,
    "signature": signature,
}

# Gửi yêu cầu POST đến MoMo
response = requests.post(endpoint, json=data)

# Kiểm tra kết quả
if response.status_code == 200:
    print("Giao dịch tạo thành công!")
    print(response.json())
else:
    print("Có lỗi xảy ra!")
    print(response.text)
