import stripe

# Thiết lập khóa bí mật (Secret Key)
stripe.api_key = "sk_test_51PMgnECyfyIhbE2iLBWhnlDVnz1MqTUJFaQHohSNxx9F0Bx13dI0a0j2sXVhbdMQr6RktjHQGZ1Gg6eNd8rKW4hx00LSoN67hj"


def thanh_toan(amount, currency, source, description):
    try:
        # Tạo một đối tượng thanh toán (Charge)
        charge = stripe.Charge.create(
            amount=amount,  # Số tiền tính bằng cent
            currency=currency,
            source=source,  # Token nguồn từ phía client
            description=description,
        )
        return charge
    except stripe.error.StripeError as e:
        print(f"Error occurred: {e.user_message}")
        return None


# Gọi hàm thanh toán
charge = thanh_toan(
    amount=5000,  # $50.00
    currency="usd",
    source="tok_visa",  # Token nguồn ví dụ
    description="Thanh toán cho sản phẩm XYZ",
)

if charge:
    print("Thanh toán thành công!")
    print(charge)
else:
    print("Thanh toán thất bại.")
