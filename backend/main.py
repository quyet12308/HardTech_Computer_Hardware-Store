from fastapi import FastAPI
from fastapi import Depends, HTTPException, status
from pydantic import BaseModel
from typing import Dict
import uvicorn
from fastapi.middleware.cors import (
    CORSMiddleware,
)
from work_with_database import *
from base_codes.hash_function import *

app = FastAPI()  # khởi tạo app fastapi

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #  chỉ định các nguồn mà bạn muốn chấp nhận yêu cầu từ server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("api/login")
async def login(login_data: LoginRequest):
    username = login_data.username
    password = login_data.password

    check_user_exists = get_user_id_by_username(username=username)
    if check_user_exists["status"]:
        get_password_in_db = get_user(user_id=check_user_exists["message"]["password"])
        check_password = verify_password(
            hex_string=get_password_in_db, password=password
        )
        if check_password:
            


async def login(request_data: dict):
    if request_data:
        # print(request_data)
        # print(type(request_data))
        name_user = request_data["name"]  # nhận các tham số từ frontend
        password = request_data["pass"]

        login_check = query_database_for_login_register_by_name(
            name=name_user
        )  # truy xuất trong database bằng name truyền vào từ frontend
        login_token = generate_random_token_string(
            length=12
        )  # tạo token cho phiên đăng nhập
        if login_check:
            # id1_,name1 , email1 , password1, createdtime1 = login_check
            password1 = login_check["password"]
            email1 = login_check["email"]
            avata_img1 = login_check["avata_img"]
            # if password == password1:
            if verify_password(hex_string=password1, password=password):
                return {
                    "response": {
                        "message": responses["dang_nhap_thanh_cong"],
                        "status": True,
                        "token": login_token,
                        "email": email1,
                        "avata_img": avata_img1,
                    }
                }
            else:
                return {
                    "response": {"message": responses["sai_mat_khau"], "status": False}
                }
        else:
            return {
                "response": {
                    "message": responses["tai_khoan_chua_duoc_dang_ky"],
                    "status": False,
                }
            }


if __name__ == "__main__":
    uvicorn.run("main:app", port=8030, workers=5, reload=True)
