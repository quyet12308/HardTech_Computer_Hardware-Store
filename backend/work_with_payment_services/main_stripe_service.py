import requests


def convert_money_from_vnd_to_usd(amount_vnd):
    ty_so_doi_doai = 0.00003929  # 1000d = 0.04 usd
    return round((amount_vnd * ty_so_doi_doai), 2)


class StripePayment:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def create_payment_url(
        self,
        amount,
        success_url,
        cancel_url,
        order_id,
        currency="usd",
        product_name="T-shirt",
    ):
        amount = int(amount)
        session_data = {
            "payment_method_types[]": "card",
            "line_items[0][price_data][currency]": currency,
            "line_items[0][price_data][product_data][name]": product_name,
            "line_items[0][price_data][unit_amount]": amount,
            "line_items[0][quantity]": 1,
            "mode": "payment",
            "success_url": f"{success_url}?status=1&stripe_payid=stripe_payid{order_id}",
            "cancel_url": cancel_url,
        }
        print(session_data)

        response = requests.post(
            "https://api.stripe.com/v1/checkout/sessions",
            headers={
                "Authorization": f"Bearer {self.secret_key}",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data=session_data,
        )
        response.raise_for_status()
        return response.json().get("url"), f"stripe_payid{order_id}"


# Hàm để sử dụng
def create_stripe_payment_url(
    amount,
    success_url,
    cancel_url,
    order_id,
    product_name="T-shirt",
):
    secret_key = "sk_test_51PMgnECyfyIhbE2iLBWhnlDVnz1MqTUJFaQHohSNxx9F0Bx13dI0a0j2sXVhbdMQr6RktjHQGZ1Gg6eNd8rKW4hx00LSoN67hj"

    stripe_payment = StripePayment(secret_key)

    try:
        payment_url, checksum = stripe_payment.create_payment_url(
            amount=amount,
            success_url=success_url,
            cancel_url=cancel_url,
            product_name=product_name,
            order_id=order_id,
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
#     payment_url = create_stripe_payment_url(
#         amount=(convert_money_from_vnd_to_usd(200000) * 100),  # Amount in cents
#         # amount=1000,  # Amount in cents
#         success_url="http://127.0.0.1:5500/in_bill.html",
#         cancel_url="http://127.0.0.1:5500/cancel_payment.html",
#         order_id=1,
#         product_name="Phương anh mua hàng",
#     )
#     print("Payment URL:", payment_url)

# import requests


# class StripePayment:
#     def __init__(self, secret_key):
#         self.secret_key = secret_key

#     def create_payment_url(
#         self, amount, success_url, cancel_url, currency="usd", product_name="T-shirt"
#     ):
#         session_data = {
#             "payment_method_types[]": "card",
#             "line_items[0][price_data][currency]": currency,
#             "line_items[0][price_data][product_data][name]": product_name,
#             "line_items[0][price_data][unit_amount]": amount,
#             "line_items[0][quantity]": 1,
#             "mode": "payment",
#             "success_url": success_url,
#             "cancel_url": cancel_url,
#         }
#         print(session_data)

#         response = requests.post(
#             "https://api.stripe.com/v1/checkout/sessions",
#             headers={
#                 "Authorization": f"Bearer {self.secret_key}",
#                 "Content-Type": "application/x-www-form-urlencoded",
#             },
#             data=session_data,
#         )
#         response.raise_for_status()
#         return response.json().get("url")


# # Hàm để sử dụng
# def create_stripe_payment_url(amount, success_url, cancel_url, product_name="T-shirt"):
#     secret_key = "sk_test_51PMgnECyfyIhbE2iLBWhnlDVnz1MqTUJFaQHohSNxx9F0Bx13dI0a0j2sXVhbdMQr6RktjHQGZ1Gg6eNd8rKW4hx00LSoN67hj"

#     stripe_payment = StripePayment(secret_key)

#     try:
#         payment_url = stripe_payment.create_payment_url(
#             amount=amount,
#             success_url=success_url,
#             cancel_url=cancel_url,
#             product_name=product_name,
#         )
#         return payment_url
#     except Exception as e:
#         print(e)
#         return None


# # Example usage
# if __name__ == "__main__":
#     payment_url = create_stripe_payment_url(
#         amount=1000,  # Amount in cents
#         success_url="http://localhost:8000/success",
#         cancel_url="http://localhost:8000/cancel",
#     )
#     print("Payment URL:", payment_url)
