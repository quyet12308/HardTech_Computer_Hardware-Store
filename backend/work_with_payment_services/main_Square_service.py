import uuid
from square.client import Client


def create_square_payment(amount, currency, source_id, customer_id=None, note=None):
    # Tạo client
    client = Client(
        access_token="EAAAl3_jGrL3M1C4WQZTMfKwaq9GAw1HDCrjpo8EbMB0_54tDNVFVW0UZsTVnfDm",  # Thay thế bằng mã thông báo truy cập của bạn
        environment="sandbox",  # Thay đổi thành 'production' khi triển khai thực tế
    )

    # Cấu hình thông tin thanh toán
    payments_api = client.payments
    body = {
        "source_id": source_id,  # Thẻ nguồn ID, thường là 'nonce' từ Square payment form
        "idempotency_key": str(
            uuid.uuid4()
        ),  # Mã định danh để tránh trùng lặp giao dịch
        "amount_money": {
            "amount": amount,  # Số tiền thanh toán
            "currency": currency,  # Đơn vị tiền tệ, ví dụ 'USD'
        },
        "customer_id": customer_id,  # ID khách hàng, nếu có
        "note": note,  # Ghi chú cho giao dịch, nếu có
    }
    print(body)

    try:
        result = payments_api.create_payment(body)
        if result.is_success():
            print(result.body)
            return result.body
        elif result.is_error():
            print(result.errors)
            return result.errors
    except Exception as e:
        print(f"Exception when calling PaymentsApi->create_payment: {e}")
        return None


# Ví dụ sử dụng
if __name__ == "__main__":
    # Thay thế với các thông tin của bạn
    amount = 2000  # Số tiền thanh toán, ví dụ $20.00
    currency = "USD"
    source_id = "cnon:card-nonce-ok"  # Nonce dùng để test từ Square payment form
    customer_id = None
    note = "Tạo đơn hàng"

    result = create_square_payment(amount, currency, source_id, customer_id, note)
    print(result)
