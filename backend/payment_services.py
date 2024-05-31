import requests

headers = {
    "Content-Type": "application/json",
    # "Authorization": "Bearer access_token$sandbox$x9364yqdjxssx8pb$698d5f034e86a664f48a3eea70079de2",
    "Authorization": "Basic AagNCkpM0282tL9fF7OwKcjo8IoHchNQb2SAlxtWfPHeRZ2ricbbv5cjydCMgOdrZr4OT9Rr68BtlOV9:EJ3Aj2GXoiqlsOCmG5jzwt55pAaKH470ENXiR8Q9AndWZWpukvMUBIX8vPCWxMTCfAOSEds5ED7tJgMd",
}

response = requests.get(
    "https://api-m.sandbox.paypal.com/v2/payments/authorizations/83PKG4TRLBLCA",
    headers=headers,
)
# In mã phản hồi HTTP
print(f"HTTP Response Code: {response.status_code}")

# In chi tiết lỗi
print(f"Error Message: {response.text}")
