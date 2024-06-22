import hashlib
import hmac
import urllib.parse


class Vnpay:
    requestData = {}
    responseData = {}

    def get_payment_url(self, vnpay_payment_url, secret_key):
        inputData = sorted(self.requestData.items())
        queryString = ""
        hasData = ""
        seq = 0
        for key, val in inputData:
            if seq == 1:
                queryString = (
                    queryString + "&" + key + "=" + urllib.parse.quote_plus(str(val))
                )
            else:
                seq = 1
                queryString = key + "=" + urllib.parse.quote_plus(str(val))

        hashValue = self.__hmacsha512(secret_key, queryString)
        return vnpay_payment_url + "?" + queryString + "&vnp_SecureHash=" + hashValue

    def validate_response(self, secret_key):
        vnp_SecureHash = self.responseData["vnp_SecureHash"]
        # Remove hash params
        if "vnp_SecureHash" in self.responseData.keys():
            self.responseData.pop("vnp_SecureHash")

        if "vnp_SecureHashType" in self.responseData.keys():
            self.responseData.pop("vnp_SecureHashType")

        inputData = sorted(self.responseData.items())
        hasData = ""
        seq = 0
        for key, val in inputData:
            if str(key).startswith("vnp_"):
                if seq == 1:
                    hasData = (
                        hasData
                        + "&"
                        + str(key)
                        + "="
                        + urllib.parse.quote_plus(str(val))
                    )
                else:
                    seq = 1
                    hasData = str(key) + "=" + urllib.parse.quote_plus(str(val))
        hashValue = self.__hmacsha512(secret_key, hasData)

        return vnp_SecureHash == hashValue

    @staticmethod
    def __hmacsha512(key, data):
        byteKey = key.encode("utf-8")
        byteData = data.encode("utf-8")
        return hmac.new(byteKey, byteData, hashlib.sha512).hexdigest()


# Ví dụ sử dụng
vnpay = Vnpay()
vnpay.requestData = {
    "vnp_Version": "2.1.0",
    "vnp_Command": "pay",
    "vnp_TmnCode": "4YJ7C2ZE",
    "vnp_Amount": "1000000",
    "vnp_CurrCode": "VND",
    "vnp_TxnRef": "123456789",
    "vnp_OrderInfo": "Test order",
    "vnp_OrderType": "other",
    "vnp_Locale": "vn",
    "vnp_ReturnUrl": "https://your-return-url.com",
    "vnp_IpAddr": "127.0.0.1",
}

# vnpay_payment_url = "https://sandbox.vnpayment.vn/paymentv2/vpcpay.html"
# secret_key = "5P125QEMH1XPV04GU2OVCDWTVYN95M2K"

# payment_url = vnpay.get_payment_url(vnpay_payment_url, secret_key)
# print(payment_url)
