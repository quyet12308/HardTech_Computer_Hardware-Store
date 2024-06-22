# import hmac
# import hashlib
# import base64
# import time
# import json
# from urllib.parse import urlencode


# class NinePayment:
#     MERCHANT_KEY = "juAOxL"
#     MERCHANT_SECRET_KEY = "3Je7RxfgIzbgbTyUX6uIa2FzhcQv1apHdap"
#     END_POINT = "https://sand-payment.9pay.vn"
#     CHECKSUM_KEY = "zlW20K17FMWpm9JhUH1PPSNDxqGLMZ97"

#     def create_payment(self, amount, description, return_url, invoice_no):
#         current_time = int(time.time())
#         invoice_no = invoice_no + 6
#         parameters = {
#             "merchantKey": self.MERCHANT_KEY,
#             "time": current_time,
#             "invoice_no": invoice_no,
#             "amount": amount,
#             "description": description,
#             "return_url": f"{return_url}?9payid=9payid{invoice_no}&status=1",
#         }
#         print(parameters)

#         http_query = self.build_http_query(parameters)
#         message = (
#             f"POST\n{self.END_POINT}/payments/create\n{current_time}\n{http_query}"
#         )
#         signature = self.build_signature(message, self.MERCHANT_SECRET_KEY)
#         base_encode = base64.b64encode(json.dumps(parameters).encode()).decode()

#         http_build = {
#             "baseEncode": base_encode,
#             "signature": signature,
#         }

#         direct_url = {
#             "payUrl": f"{self.END_POINT}/portal?{self.build_http_query(http_build)}"
#         }

#         return direct_url

#     def build_http_query(self, data):
#         ordered_data = dict(sorted(data.items()))
#         return urlencode(ordered_data)

#     def build_signature(self, data, secret):
#         token = hmac.new(secret.encode(), data.encode(), hashlib.sha256).digest()
#         return base64.b64encode(token).decode()

#     def verify_nine_payment(self, result, checksum):
#         decoded_result = self.decode_base64(result)
#         is_valid_checksum = self.verify_checksum(result, checksum)

#         return {
#             "isValidChecksum": is_valid_checksum,
#             "decodedResult": decoded_result,
#         }

#     def verify_checksum(self, result, checksum):
#         sha256_data = (
#             hmac.new(self.CHECKSUM_KEY.encode(), result.encode(), hashlib.sha256)
#             .hexdigest()
#             .upper()
#         )
#         return sha256_data == checksum

#     def decode_base64(self, base64_string):
#         return base64.b64decode(base64_string).decode("ascii")


# Ví dụ sử dụng
# nine_pay = NinePayment()
# payment_url = nine_pay.create_payment(
#     amount=20000,
#     description="Tạo đơn hàng",
#     return_url="http://127.0.0.1:5500/in_bill.html?9payid=INV6",
#     invoice_no="INV6",
# )
# print(payment_url)

import time
import base64
import hmac
import hashlib
import json
from urllib.parse import urlencode


class NinePayment:
    MERCHANT_KEY = "juAOxL"
    MERCHANT_SECRET_KEY = "3Je7RxfgIzbgbTyUX6uIa2FzhcQv1apHdap"
    END_POINT = "https://sand-payment.9pay.vn"
    CHECKSUM_KEY = "zlW20K17FMWpm9JhUH1PPSNDxqGLMZ97"

    def create_payment(self, amount, description, return_url, invoice_no):
        current_time = int(time.time())
        invoice_no = invoice_no + 6
        parameters = {
            "merchantKey": self.MERCHANT_KEY,
            "time": current_time,
            "invoice_no": str(invoice_no),
            "amount": amount,
            "description": description,
            "return_url": f"{return_url}?9payid=9payid{invoice_no}&status=1",
        }

        http_query = self.build_http_query(parameters)
        message = (
            f"POST\n{self.END_POINT}/payments/create\n{current_time}\n{http_query}"
        )
        signature = self.build_signature(message, self.MERCHANT_SECRET_KEY)
        base_encode = base64.b64encode(json.dumps(parameters).encode()).decode()

        http_build = {
            "baseEncode": base_encode,
            "signature": signature,
        }

        direct_url = {
            "payUrl": f"{self.END_POINT}/portal?{self.build_http_query(http_build)}"
        }

        checksum = f"9payid{invoice_no}"

        return direct_url, checksum

    def build_http_query(self, data):
        ordered_data = dict(sorted(data.items()))
        return urlencode(ordered_data)

    def build_signature(self, data, secret):
        token = hmac.new(secret.encode(), data.encode(), hashlib.sha256).digest()
        return base64.b64encode(token).decode()

    def verify_nine_payment(self, result, checksum):
        decoded_result = self.decode_base64(result)
        is_valid_checksum = self.verify_checksum(result, checksum)

        return {
            "isValidChecksum": is_valid_checksum,
            "decodedResult": decoded_result,
        }

    def verify_checksum(self, result, checksum):
        sha256_data = (
            hmac.new(self.CHECKSUM_KEY.encode(), result.encode(), hashlib.sha256)
            .hexdigest()
            .upper()
        )
        return sha256_data == checksum

    def decode_base64(self, base64_string):
        return base64.b64decode(base64_string).decode("ascii")


# Function to use
def create_nine_payment_url(amount, description, return_url, invoice_no):
    nine_payment = NinePayment()
    try:
        payment_url, checksum = nine_payment.create_payment(
            amount, description, return_url, invoice_no
        )
        if payment_url and checksum:
            return {
                "status": True,
                "message": {
                    "payment_url": payment_url["payUrl"],
                    "check_sum": checksum,
                },
            }
        else:
            return {"status": False, "message": "Unable to create payment URL"}
    except Exception as e:
        print(e)
        return {"status": False, "message": str(e)}


# a = create_nine_payment_url(
#     amount=200000,
#     description="Phương anh mua hàng",
#     invoice_no=2,
#     return_url="http://127.0.0.1:5500/in_bill.html",
# )
# print(a)
