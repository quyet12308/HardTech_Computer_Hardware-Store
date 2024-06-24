import httpx


async def verify_hcaptcha(token: str, HCAPTCHA_SECRET_KEY: str) -> bool:
    url = "https://hcaptcha.com/siteverify"
    data = {"secret": HCAPTCHA_SECRET_KEY, "response": token}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=data)
        result = response.json()
    return result.get("success", False)
