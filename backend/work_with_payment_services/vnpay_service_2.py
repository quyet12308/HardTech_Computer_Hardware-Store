import hashlib
import hmac
import random
import string
import urllib.parse
import datetime
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

app = FastAPI()


class VNPayConfig:
    # vnp_PayUrl = "https://sandbox.vnpayment.vn/paymentv2/vpcpay.html"
    # vnp_ReturnUrl = "http://localhost:8000/payment/success/"
    # vnp_TmnCode = "JA7DXVX3"
    # secretKey = "HH642VNWNWCBE6LX3GOLA7EWERLYLYUS"
    # vnp_ApiUrl = "https://sandbox.vnpayment.vn/merchant_webapi/api/transaction"

    vnp_PayUrl = "https://sandbox.vnpayment.vn/paymentv2/vpcpay.html"
    vnp_ReturnUrl = "http://localhost:8000/payment/success/"
    vnp_TmnCode = "4YJ7C2ZE"
    secretKey = "5P125QEMH1XPV04GU2OVCDWTVYN95M2K"
    vnp_ApiUrl = "https://sandbox.vnpayment.vn/merchant_webapi/api/transaction"

    @staticmethod
    def md5(message):
        try:
            digest = hashlib.md5(message.encode("utf-8")).hexdigest()
        except Exception as ex:
            digest = ""
        return digest

    @staticmethod
    def sha256(message):
        try:
            digest = hashlib.sha256(message.encode("utf-8")).hexdigest()
        except Exception as ex:
            digest = ""
        return digest

    @staticmethod
    def hash_all_fields(fields):
        sorted_field_names = sorted(fields.keys())
        sb = []
        for field_name in sorted_field_names:
            field_value = fields[field_name]
            if field_value:
                sb.append(f"{field_name}={field_value}")
        data = "&".join(sb)
        return VNPayConfig.hmac_sha512(VNPayConfig.secretKey, data)

    @staticmethod
    def hmac_sha512(key, data):
        try:
            if key is None or data is None:
                raise ValueError("Key or data should not be None")
            hmac_key_bytes = key.encode("utf-8")
            data_bytes = data.encode("utf-8")
            result = hmac.new(hmac_key_bytes, data_bytes, hashlib.sha512).hexdigest()
            return result
        except Exception as ex:
            return ""

    @staticmethod
    def get_ip_address(request: Request):
        try:
            ip_address = request.headers.get("X-Forwarded-For")
            if ip_address is None:
                ip_address = request.client.host
        except Exception as e:
            ip_address = f"Invalid IP: {str(e)}"
        return ip_address

    @staticmethod
    def get_random_number(length):
        chars = string.digits
        rnd = random.SystemRandom()
        return "".join(rnd.choice(chars) for _ in range(length))

    @staticmethod
    def create_payment_url(amount, order_id, ip_addr):
        vnp_Url = VNPayConfig.vnp_PayUrl
        vnp_Returnurl = VNPayConfig.vnp_ReturnUrl
        vnp_TmnCode = VNPayConfig.vnp_TmnCode

        inputData = {
            "vnp_Version": "2.1.0",
            "vnp_Command": "pay",
            "vnp_TmnCode": vnp_TmnCode,
            "vnp_Amount": str(amount * 100),  # Số tiền cần thanh toán (đơn vị: VND)
            "vnp_CurrCode": "VND",
            "vnp_TxnRef": order_id,  # Mã hóa đơn
            "vnp_OrderInfo": f"Thanh toan don hang {order_id}",
            "vnp_OrderType": "other",
            "vnp_Locale": "vn",
            "vnp_ReturnUrl": vnp_Returnurl,
            "vnp_IpAddr": ip_addr,
            "vnp_CreateDate": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
        }

        inputData["vnp_SecureHash"] = VNPayConfig.hash_all_fields(inputData)
        query_string = urllib.parse.urlencode(inputData)
        payment_url = f"{vnp_Url}?{query_string}"
        return payment_url


@app.get("/create_payment")
async def create_payment(request: Request):
    amount = 1000000  # Số tiền cần thanh toán
    order_id = VNPayConfig.get_random_number(8)
    ip_addr = VNPayConfig.get_ip_address(request)
    payment_url = VNPayConfig.create_payment_url(amount, order_id, ip_addr)
    return RedirectResponse(payment_url)


@app.get("/payment/success")
async def payment_success(request: Request):
    vnp_response = dict(request.query_params)
    secure_hash = vnp_response.get("vnp_SecureHash")
    input_data = {k: v for k, v in vnp_response.items() if k != "vnp_SecureHash"}
    if VNPayConfig.hash_all_fields(input_data) == secure_hash:
        # Payment is verified
        return "Payment successful and verified"
    else:
        return "Payment verification failed"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("vnpay_service_2:app", port=8000, reload=True)
