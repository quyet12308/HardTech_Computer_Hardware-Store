import hmac
import hashlib
import base64
import time
import json
from urllib.parse import urlencode
import uuid

class SquarePayment:
    def __init__(self, access_token, environment='sandbox'):
        self.access_token = access_token
        self.environment = environment
        self.base_url = 'https://connect.squareupsandbox.com' if environment == 'sandbox' else 'https://connect.squareup.com'
        self.merchant_key = 'YOUR_MERCHANT_KEY'  # Thay thế bằng Merchant Key của bạn
        self.merchant_secret_key = 'sandbox-sq0csb-oDwu7LFAJ_VnvAT2qZb90KEoDmKa7ibO1L8aXRqsleI'  # Thay thế bằng Merchant Secret Key của bạn

    def create_payment_url(self, amount, currency, description, return_url, invoice_no):
        time_now = int(time.time())

        parameters = {
            'merchantKey': self.merchant_key,
            'time': time_now,
            'invoice_no': invoice_no,
            'amount': amount,
            'description': description,
            'return_url': return_url
        }

        http_query = self.build_http_query(parameters)
        message = f"POST\n{self.base_url}/v2/payments\n{time_now}\n{http_query}"
        signature = self.build_signature(message, self.merchant_secret_key)
        base_encode = base64.b64encode(json.dumps(parameters).encode()).decode()

        http_build = {
            'baseEncode': base_encode,
            'signature': signature,
        }

        direct_url = f"{self.base_url}/v2/checkout?{self.build_http_query(http_build)}"
        return direct_url

    def build_http_query(self, data):
        ordered_data = dict(sorted(data.items()))
        return urlencode(ordered_data)

    def build_signature(self, data, secret):
        token = hmac.new(secret.encode(), data.encode(), hashlib.sha256).digest()
        return base64.b64encode(token).decode()

# Ví dụ sử dụng
if __name__ == "__main__":
    payment = SquarePayment(access_token='YOUR_ACCESS_TOKEN')
    amount = 2000  # Số tiền thanh toán, ví dụ $20.00
    currency = "USD"
    description = "Sample Item"
    return_url = "https://your-website.com/return-url"
    invoice_no = str(uuid.uuid4())  # Tạo số hóa đơn duy nhất

    payment_url = payment.create_payment_url(amount, currency, description, return_url, invoice_no)
    print(payment_url)
