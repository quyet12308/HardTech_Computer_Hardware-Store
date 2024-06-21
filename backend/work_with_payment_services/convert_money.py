import requests

# do mạng lag khi connect tới server nước ngoài nên có lẽ sẽ đặt tỷ giá luôn ko dùng api nữa vì gọi mỗi cái api thôi đã tốn mất gần 10s
ty_so_doi_doai = 0.00003929  # 1000d = 0.04 usd


def convert_money_from_vnd_to_usd(amount_vnd):
    amount_vnd = float(amount_vnd)
    return round((amount_vnd * ty_so_doi_doai), 2)


def get_exchange_rate(api_key, from_currency, to_currency):
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Error fetching exchange rate data")

    data = response.json()

    if from_currency != "USD":
        raise Exception("Free tier only supports USD as base currency")

    if to_currency not in data["rates"]:
        raise Exception(f"Conversion rate for {to_currency} not found")

    return data["rates"][to_currency]


def currency_converter(api_key, from_currency, to_currency, amount):
    if from_currency == "USD":
        rate = get_exchange_rate(api_key, from_currency, to_currency)
        converted_amount = amount * rate
    else:
        # Chuyển đổi từ from_currency sang USD, sau đó từ USD sang to_currency
        rate_to_usd = get_exchange_rate(api_key, "USD", from_currency)
        amount_in_usd = amount / rate_to_usd
        rate_to_target = get_exchange_rate(api_key, "USD", to_currency)
        converted_amount = amount_in_usd * rate_to_target

    return converted_amount


# Ví dụ sử dụng
# api_key = "2b4a1eca79904dfeaaf3f43ff56d0854"  # Thay thế bằng API key của bạn
# from_currency = "VND"  # Tiền tệ gốc (ví dụ: VND)
# to_currency = "USD"  # Tiền tệ đích (ví dụ: USD)
# amount = 1000000  # Số tiền cần quy đổi

# try:
#     converted_amount = currency_converter(api_key, from_currency, to_currency, amount)
#     print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
# except Exception as e:
#     print(f"Error: {e}")

# a = convert_money_from_vnd_to_usd(amount_vnd=1000)
# print(a)
