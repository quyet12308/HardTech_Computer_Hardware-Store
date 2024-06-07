import requests

# Cung cấp Secret Key của bạn
stripe_secret_key = "sk_test_51PMgnECyfyIhbE2iLBWhnlDVnz1MqTUJFaQHohSNxx9F0Bx13dI0a0j2sXVhbdMQr6RktjHQGZ1Gg6eNd8rKW4hx00LSoN67hj"


def create_payment_intent(amount, currency):
    url = "https://api.stripe.com/v1/payment_intents"
    headers = {
        "Authorization": "Bearer " + stripe_secret_key,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"amount": amount, "currency": currency, "payment_method_types[]": "card"}
    response = requests.post(url, headers=headers, data=data)
    payment_intent = response.json()
    return payment_intent


def confirm_payment_intent(payment_intent_id):
    url = f"https://api.stripe.com/v1/payment_intents/{payment_intent_id}/confirm"
    headers = {
        "Authorization": "Bearer " + stripe_secret_key,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {}
    response = requests.post(url, headers=headers, data=data)
    payment_intent = response.json()
    return payment_intent


# Tạo một payment intent
payment_intent = create_payment_intent(1000, "usd")
print("Payment Intent:", payment_intent)

# Xác nhận payment intent
confirmed_payment_intent = confirm_payment_intent(payment_intent["id"])
print("Confirmed Payment Intent:", confirmed_payment_intent)
