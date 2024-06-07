import requests
from requests.auth import HTTPBasicAuth


def get_access_token(client_id, secret):
    url = "https://api.sandbox.paypal.com/v1/oauth2/token"
    headers = {"Accept": "application/json", "Accept-Language": "en_US"}
    data = {"grant_type": "client_credentials"}
    response = requests.post(
        url, headers=headers, data=data, auth=HTTPBasicAuth(client_id, secret)
    )
    response.raise_for_status()
    return response.json()["access_token"]


def create_payment(access_token, return_url, cancel_url):
    url = "https://api.sandbox.paypal.com/v1/payments/payment"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    payload = {
        "intent": "sale",
        "redirect_urls": {"return_url": return_url, "cancel_url": cancel_url},
        "payer": {"payment_method": "paypal"},
        "transactions": [
            {
                "amount": {"total": "10.00", "currency": "USD"},
                "description": "This is the payment transaction description.",
            }
        ],
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()


def execute_payment(access_token, payment_id, payer_id):
    url = f"https://api.sandbox.paypal.com/v1/payments/payment/{payment_id}/execute"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    payload = {"payer_id": payer_id}
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()


access_token = "A21AAKNWs9AoX3wBPymXHjMZZOSpWXY1de1iJ6MeFDkm0WfK_PLuflpS4u9MMcLuMi3yVpV0aKx47EY4cvhUWQFFxOYezbm4w"
return_url = "http://localhost:5000/payment/execute"
cancel_url = "http://localhost:5000/payment/cancel"

payment_id = "83PKG4TRLBLCA"
payer_id = "PAYID-MZN6WJQ3RR15121BW562260A"
# execution_response = execute_payment(access_token, payment_id, payer_id)
# print(execution_response)
payment = create_payment(access_token, return_url, cancel_url)
print(payment)

# client_id = (
#     "AagNCkpM0282tL9fF7OwKcjo8IoHchNQb2SAlxtWfPHeRZ2ricbbv5cjydCMgOdrZr4OT9Rr68BtlOV9"
# )
# secret = (
#     "EJ3Aj2GXoiqlsOCmG5jzwt55pAaKH470ENXiR8Q9AndWZWpukvMUBIX8vPCWxMTCfAOSEds5ED7tJgMd"
# )
# access_token = get_access_token(client_id, secret)
# print(f"Access Token: {access_token}")
