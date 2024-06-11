import hmac
import hashlib
import json
import time
import requests


class MomoPayment:
    def __init__(self):
        self.partner_code = "MOMO"
        self.access_key = "F8BBA842ECF85"
        self.secret_key = "K951B6PE1waDMi640xX08PD3vg6EkVlz"

    def create_payment(self, amount, ipn_url, order_id, order_info, redirect_url):
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
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"MoMo payment failed: {str(e)}")

    def verify_momo_payment(self, report):
        data = f"{report['partnerCode']}{report['orderId']}{report['requestId']}{report['amount']}{report['orderInfo']}{report['orderType']}{report['transId']}{report['resultCode']}{report['message']}{report['payType']}{report['responseTime']}{report['extraData']}"
        generated_signature = hmac.new(
            self.secret_key.encode("utf-8"), data.encode("utf-8"), hashlib.sha256
        ).hexdigest()

        return generated_signature == report["signature"]


# Example usage
if __name__ == "__main__":
    momo_payment = MomoPayment()

    try:
        response = momo_payment.create_payment(
            amount=10000,
            ipn_url="https://webhook.site/your-ipn-url",
            order_id="order123456",
            order_info="Test order",
            redirect_url="https://your-redirect-url.com",
        )
        print("Payment created:", response)
    except Exception as e:
        print(e)

    # Example report for verification
    report = {
        "partnerCode": "MOMO",
        "orderId": "order123456",
        "requestId": "MOMO1618984750000",
        "amount": 10000,
        "orderInfo": "Test order",
        "orderType": "momo_wallet",
        "transId": "2305139496",
        "resultCode": 0,
        "message": "Thành công",
        "payType": "qr",
        "responseTime": 1618984750000,
        "extraData": "",
        "signature": "generated_signature_from_momo",
    }

    is_valid = momo_payment.verify_momo_payment(report)
    print("Is the report valid?", is_valid)
