import hmac
import hashlib
import json
import time
import requests


class MomoPayment:
    def __init__(self, partner_code, access_key, secret_key):
        self.partner_code = partner_code
        self.access_key = access_key
        self.secret_key = secret_key

    def create_payment_url(self, amount, ipn_url, order_id, order_info, redirect_url):

        order_id = int(order_id) + 12
        order_id = f"order{order_id}"
        print(type(order_id))
        amount = int(amount)
        extra_data = ""
        request_type = "captureWallet"
        request_id = self.partner_code + str(int(time.time() * 1000))

        raw_signature = f"accessKey={self.access_key}&amount={amount}&extraData={extra_data}&ipnUrl={ipn_url}&orderId={order_id}&orderInfo={order_info}&partnerCode={self.partner_code}&redirectUrl={redirect_url}&requestId={request_id}&requestType={request_type}"

        signature = hmac.new(
            self.secret_key.encode("utf-8"),
            raw_signature.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()

        request_body = {
            "partnerCode": self.partner_code,
            "accessKey": self.access_key,
            "requestId": request_id,
            "amount": amount,
            "orderId": order_id,
            "orderInfo": order_info,
            "redirectUrl": redirect_url,
            "ipnUrl": ipn_url,
            "extraData": extra_data,
            "requestType": request_type,
            "signature": signature,
            "lang": "vi",
        }
        print(request_body)
        try:
            response = requests.post(
                "https://test-payment.momo.vn/v2/gateway/api/create",
                data=json.dumps(request_body),
                headers={
                    "Content-Type": "application/json",
                    "Content-Length": str(len(json.dumps(request_body))),
                },
            )
            response.raise_for_status()
            return response.json().get("payUrl"), order_id
        except requests.exceptions.RequestException as e:
            raise Exception(f"MoMo payment failed: {str(e)}")


# Hàm để sử dụng
def create_momo_payment_url(amount, ipn_url, order_id, order_info, redirect_url):
    partner_code = "MOMO"
    access_key = "F8BBA842ECF85"
    secret_key = "K951B6PE1waDMi640xX08PD3vg6EkVlz"

    momo_payment = MomoPayment(partner_code, access_key, secret_key)

    try:
        payment_url, checksum = momo_payment.create_payment_url(
            amount=amount,
            ipn_url=ipn_url,
            order_id=order_id,
            order_info=order_info,
            redirect_url=redirect_url,
        )
        return {
            "status": True,
            "message": {"payment_url": payment_url, "check_sum": checksum},
        }
    except Exception as e:
        print(e)
        return {"status": False, "message": ""}
