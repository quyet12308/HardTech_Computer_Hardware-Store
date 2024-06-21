import requests
from unidecode import unidecode

# # from convert_money import *
from urllib.parse import urlparse, parse_qs

# # ty_so_doi_doai = 0.00003929  # 1000d = 0.04 usd


def remove_vietnamese_accents(text):
    return unidecode(text)


# Ví dụ sử dụng
# input_text = "phương anh mua hàng"
# output_text = remove_vietnamese_accents(input_text)
# print(output_text)  # Kết quả: "phuong anh mua hang"


def convert_money_from_vnd_to_usd(amount_vnd):
    ty_so_doi_doai = 0.00003929  # 1000d = 0.04 usd
    return round((amount_vnd * ty_so_doi_doai), 2)


def get_token_from_url(url):
    # Phân tích URL
    parsed_url = urlparse(url)
    # Trích xuất các tham số truy vấn
    query_params = parse_qs(parsed_url.query)
    # Lấy giá trị của token
    token = query_params.get("token")
    # Kiểm tra nếu token tồn tại và trả về giá trị của nó
    if token:
        return token[0]
    else:
        return None


# URL cần trích xuất token
# url = "https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token=EC-50F76549Y8402431P"

# # Gọi hàm và in kết quả
# token = get_token_from_url(url)
# print("Token:", token)


class PayPalPayment:
    def __init__(self, client_id, secret, api_base):
        self.client_id = client_id
        self.secret = secret
        self.api_base = api_base

    def get_access_token(self):
        response = requests.post(
            f"{self.api_base}/v1/oauth2/token",
            headers={"Accept": "application/json", "Accept-Language": "en_US"},
            data={"grant_type": "client_credentials"},
            auth=(self.client_id, self.secret),
        )
        response.raise_for_status()
        return response.json()["access_token"]

    def create_payment_url(
        self,
        amount,
        return_url,
        cancel_url,
        currency="USD",
        description="Payment description",
    ):
        amount = float(amount)
        payment_data = {
            "intent": "sale",
            "payer": {"payment_method": "paypal"},
            "transactions": [
                {
                    "amount": {"total": str(amount), "currency": currency},
                    "description": description,
                }
            ],
            "redirect_urls": {
                "return_url": return_url,
                "cancel_url": cancel_url,
            },
        }
        print(payment_data)

        access_token = self.get_access_token()
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        response = requests.post(
            f"{self.api_base}/v1/payments/payment", json=payment_data, headers=headers
        )
        response.raise_for_status()
        for link in response.json()["links"]:
            if link["rel"] == "approval_url":
                # return link["href"]
                return link["href"], get_token_from_url(url=link["href"])
        return None


# Hàm để sử dụng
def create_paypal_payment_url(
    amount, return_url, cancel_url, description="Payment description"
):
    client_id = "AagNCkpM0282tL9fF7OwKcjo8IoHchNQb2SAlxtWfPHeRZ2ricbbv5cjydCMgOdrZr4OT9Rr68BtlOV9"
    secret = "EJ3Aj2GXoiqlsOCmG5jzwt55pAaKH470ENXiR8Q9AndWZWpukvMUBIX8vPCWxMTCfAOSEds5ED7tJgMd"
    api_base = "https://api.sandbox.paypal.com"

    paypal_payment = PayPalPayment(client_id, secret, api_base)

    try:
        payment_url, checksum = paypal_payment.create_payment_url(
            amount=amount,
            return_url=return_url,
            cancel_url=cancel_url,
            description=description,
        )

        if payment_url and checksum:
            return {
                "status": True,
                "message": {"payment_url": payment_url, "check_sum": checksum},
            }
        else:
            return {"status": False, "message": "Unable to create payment URL"}
    except Exception as e:
        print(e)
        return {"status": False, "message": str(e)}


# Example usage
# if __name__ == "__main__":
#     payment_url = create_paypal_payment_url(
#         amount=convert_money_from_vnd_to_usd(amount_vnd=200000),
#         # amount="10",
#         return_url="http://127.0.0.1:5500/in_bill.html",
#         cancel_url="http://localhost:8000/cancel-payment/",
#         description="Phương anh mua hàng",
#     )
#     print("Payment URL:", payment_url)

# import requests


# class PayPalPayment:
#     def __init__(self, client_id, secret, api_base):
#         self.client_id = client_id
#         self.secret = secret
#         self.api_base = api_base

#     def get_access_token(self):
#         response = requests.post(
#             f"{self.api_base}/v1/oauth2/token",
#             headers={"Accept": "application/json", "Accept-Language": "en_US"},
#             data={"grant_type": "client_credentials"},
#             auth=(self.client_id, self.secret),
#         )
#         response.raise_for_status()
#         return response.json()["access_token"]

#     def create_payment_url(
#         self,
#         amount,
#         return_url,
#         cancel_url,
#         currency="USD",
#         description="Payment description",
#     ):
#         payment_data = {
#             "intent": "sale",
#             "payer": {"payment_method": "paypal"},
#             "transactions": [
#                 {
#                     "amount": {"total": amount, "currency": currency},
#                     "description": description,
#                 }
#             ],
#             "redirect_urls": {
#                 "return_url": return_url,
#                 "cancel_url": cancel_url,
#             },
#         }
#         print(payment_data)

#         access_token = self.get_access_token()
#         headers = {
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {access_token}",
#         }
#         response = requests.post(
#             f"{self.api_base}/v1/payments/payment", json=payment_data, headers=headers
#         )
#         response.raise_for_status()
#         for link in response.json()["links"]:
#             if link["rel"] == "approval_url":
#                 return link["href"]
#         return None


# # Hàm để sử dụng
# def create_paypal_payment_url(
#     amount, return_url, cancel_url, description="Payment description"
# ):
#     client_id = "AagNCkpM0282tL9fF7OwKcjo8IoHchNQb2SAlxtWfPHeRZ2ricbbv5cjydCMgOdrZr4OT9Rr68BtlOV9"
#     secret = "EJ3Aj2GXoiqlsOCmG5jzwt55pAaKH470ENXiR8Q9AndWZWpukvMUBIX8vPCWxMTCfAOSEds5ED7tJgMd"
#     api_base = "https://api.sandbox.paypal.com"

#     paypal_payment = PayPalPayment(client_id, secret, api_base)

#     try:
#         payment_url = paypal_payment.create_payment_url(
#             amount=amount,
#             return_url=return_url,
#             cancel_url=cancel_url,
#             description=description,
#         )
#         return payment_url
#     except Exception as e:
#         print(e)
#         return None


# # Example usage
# if __name__ == "__main__":
#     payment_url = create_paypal_payment_url(
#         amount="10.00",
#         return_url="http://127.0.0.1:5500/in_bill.html",
#         cancel_url="http://localhost:8000/cancel-payment/",
#         description="Phương anh mua hàng",
#     )
#     print("Payment URL:", payment_url)
