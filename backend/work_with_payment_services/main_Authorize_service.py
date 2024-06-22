import requests
import uuid
import xml.etree.ElementTree as ET


# Hàm tạo URL thanh toán
def create_authorize_net_payment_url(api_login_id, transaction_key, amount, return_url):
    # Tạo unique transaction ID
    transaction_id = str(uuid.uuid4())

    # Tạo payload XML
    payload = f"""
    <createTransactionRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
        <merchantAuthentication>
            <name>{api_login_id}</name>
            <transactionKey>{transaction_key}</transactionKey>
        </merchantAuthentication>
        <transactionRequest>
            <transactionType>authCaptureTransaction</transactionType>
            <amount>{amount}</amount>
            <payment>
                <creditCard>
                    <cardNumber>4111111111111111</cardNumber>
                    <expirationDate>2025-12</expirationDate>
                    <cardCode>123</cardCode>
                </creditCard>
            </payment>
            <order>
                <invoiceNumber>{transaction_id}</invoiceNumber>
                <description>Sample Transaction</description>
            </order>
            <customer>
                <id>{transaction_id}</id>
            </customer>
            <transactionSettings>
                <setting>
                    <settingName>duplicateWindow</settingName>
                    <settingValue>0</settingValue>
                </setting>
            </transactionSettings>
            <retail>
                <marketType>0</marketType>
                <deviceType>1</deviceType>
            </retail>
        </transactionRequest>
    </createTransactionRequest>
    """

    headers = {"Content-Type": "application/xml"}

    # Gửi yêu cầu POST tới Authorize.Net
    response = requests.post(
        "https://apitest.authorize.net/xml/v1/request.api",
        data=payload,
        headers=headers,
    )

    # Phân tích XML response
    tree = ET.ElementTree(ET.fromstring(response.text))
    root = tree.getroot()

    # Lấy transactionResponse và kết quả trả về
    transaction_response = root.find(".//transactionResponse")
    if (
        transaction_response is not None
        and transaction_response.find("responseCode").text == "1"
    ):
        auth_code = transaction_response.find("authCode").text
        return f"{return_url}?transaction_id={transaction_id}&auth_code={auth_code}"
    else:
        error_code = (
            transaction_response.find("errors").find("error").find("errorCode").text
        )
        error_text = (
            transaction_response.find("errors").find("error").find("errorText").text
        )
        raise Exception(
            f"Transaction failed with error code {error_code}: {error_text}"
        )


# Sử dụng hàm
api_login_id = "bizdev05"
transaction_key = "4kJd237rZu59qAZd"
amount = "10.00"
return_url = "http://127.0.0.1:5500/in_bill.html"

try:
    payment_url = create_authorize_net_payment_url(
        api_login_id, transaction_key, amount, return_url
    )
    print(f"Payment URL: {payment_url}")
except Exception as e:
    print(f"Error: {e}")
