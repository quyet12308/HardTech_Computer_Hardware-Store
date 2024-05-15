from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import (
    CORSMiddleware,
)

app = FastAPI()  # khởi tạo app fastapi

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #  chỉ định các nguồn mà bạn muốn chấp nhận yêu cầu từ server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("api/login")
async def login(request_data: dict):
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", port=8030, workers=5, reload=True)
