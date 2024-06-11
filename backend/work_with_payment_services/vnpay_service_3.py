from fastapi import FastAPI, Request, Query
from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime
import hashlib
import urllib.parse

app = FastAPI()

# Cấu hình VnPay
vnp_PayUrl = "https://sandbox.vnpayment.vn/paymentv2/vpcpay.html"
vnp_ReturnUrl = "http://localhost:8000/payment/success/"
vnp_TmnCode = "JA7DXVX3"
secretKey = "HH642VNWNWCBE6LX3GOLA7EWERLYLYUS"
vnp_ApiUrl = "https://sandbox.vnpayment.vn/merchant_webapi/api/transaction"


class VnPaymentRequestModel(BaseModel):
    amount: int
    created_date: datetime
    order_id: str


class VnPayLibrary:
    def __init__(self):
        self.request_data = {}
        self.response_data = {}

    def add_request_data(self, key, value):
        self.request_data[key] = value

    def add_response_data(self, key, value):
        self.response_data[key] = value

    def create_request_url(self, base_url, hash_secret):
        query_string = "&".join(
            f"{key}={urllib.parse.quote_plus(str(value))}"
            for key, value in sorted(self.request_data.items())
        )
        hash_value = hashlib.sha256(
            (query_string + hash_secret).encode("utf-8")
        ).hexdigest()
        return f"{base_url}?{query_string}&vnp_SecureHash={hash_value}"

    def get_response_data(self, key):
        return self.response_data.get(key)

    def validate_signature(self, received_hash, hash_secret):
        query_string = "&".join(
            f"{key}={urllib.parse.quote_plus(str(value))}"
            for key, value in sorted(self.response_data.items())
            if key != "vnp_SecureHash"
        )
        calculated_hash = hashlib.sha256(
            (query_string + hash_secret).encode("utf-8")
        ).hexdigest()
        return calculated_hash == received_hash


class VnPayService:
    def __init__(self, pay_url, return_url, tmn_code, secret_key):
        self.pay_url = pay_url
        self.return_url = return_url
        self.tmn_code = tmn_code
        self.secret_key = secret_key

    def create_payment_url(self, model: VnPaymentRequestModel, client_ip: str):
        tick = str(datetime.now().timestamp()).replace(".", "")

        vnpay = VnPayLibrary()
        vnpay.add_request_data("vnp_Version", "2.1.0")
        vnpay.add_request_data("vnp_Command", "pay")
        vnpay.add_request_data("vnp_TmnCode", self.tmn_code)
        vnpay.add_request_data("vnp_Amount", str(model.amount * 100))
        vnpay.add_request_data(
            "vnp_CreateDate", model.created_date.strftime("%Y%m%d%H%M%S")
        )
        vnpay.add_request_data("vnp_CurrCode", "VND")
        vnpay.add_request_data("vnp_IpAddr", client_ip)
        vnpay.add_request_data("vnp_Locale", "vn")
        vnpay.add_request_data(
            "vnp_OrderInfo", f"Thanh toán cho đơn hàng: {model.order_id}"
        )
        vnpay.add_request_data("vnp_OrderType", "other")
        vnpay.add_request_data("vnp_ReturnUrl", self.return_url)
        vnpay.add_request_data("vnp_TxnRef", tick)

        payment_url = vnpay.create_request_url(self.pay_url, self.secret_key)
        return payment_url

    def payment_execute(self, collections: Dict[str, str]):
        vnpay = VnPayLibrary()
        for key, value in collections.items():
            if key.startswith("vnp_"):
                vnpay.add_response_data(key, value)

        vnp_order_id = int(vnpay.get_response_data("vnp_TxnRef"))
        vnp_transaction_id = int(vnpay.get_response_data("vnp_TransactionNo"))
        vnp_secure_hash = collections.get("vnp_SecureHash")
        vnp_response_code = vnpay.get_response_data("vnp_ResponseCode")
        vnp_order_info = vnpay.get_response_data("vnp_OrderInfo")

        check_signature = vnpay.validate_signature(vnp_secure_hash, self.secret_key)
        if not check_signature:
            return {"success": False}

        return {
            "success": True,
            "payment_method": "VnPay",
            "order_description": vnp_order_info,
            "order_id": str(vnp_order_id),
            "transaction_id": str(vnp_transaction_id),
            "token": vnp_secure_hash,
            "vnpay_response_code": vnp_response_code,
        }


vn_pay_service = VnPayService(vnp_PayUrl, vnp_ReturnUrl, vnp_TmnCode, secretKey)


@app.post("/create_payment_url")
async def create_payment_url(request: Request, model: VnPaymentRequestModel):
    client_ip = request.client.host
    payment_url = vn_pay_service.create_payment_url(model, client_ip)
    return {"payment_url": payment_url}


@app.get("/payment_execute")
async def payment_execute(vnp_SecureHash: Optional[str] = Query(None), **kwargs):
    result = vn_pay_service.payment_execute(kwargs)
    return result


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("vnpay_service_3:app", port=8001, reload=True)
