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
from base_codes.get_token import generate_token
from base_codes.gettime import *
from setting import *
from base_codes.string_python_en import responses

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

class RegisterVerificationCodeRequest(BaseModel):
    email:str

class RegisterCreateAccountRequest(BaseModel):
    email:str
    username:str
    password:str




@app.post("/api/login")
async def login(login_data: LoginRequest):
    username = login_data.username
    password = login_data.password

    check_user_exists = get_user_id_by_username(username=username)
    if check_user_exists["status"]:
        get_user_infor_using_userid = get_user(user_id=check_user_exists["message"])
        get_password_in_db = get_user_infor_using_userid["message"]["password"]
        check_password = verify_password(
            hex_string=get_password_in_db, password=password
        )
        if check_password:
            token_login_session = generate_token()
            result_login_session = add_login_session(
                token_value=token_login_session,
                user_id=check_user_exists["message"],
                expiration_date=convert_to_datetime(
                    time_string=add_time_to_datetime(
                        hours=LOGIN_SESSION_EFFECTIVE_PERIOD
                    )["message"]
                ),
            )
            if result_login_session["status"]:
                return {
                    "response": {
                        "message": responses["dang_nhap_thanh_cong"],
                        "status": True,
                        "token": token_login_session,
                        "avata_img": get_user_infor_using_userid["message"]["img"],
                    }
                }
        else:
            return {"response": {"message": responses["sai_mat_khau"], "status": False}}
    else:
        return {
            "response": {
                "message": responses["tai_khoan_chua_duoc_dang_ky"],
                "status": False,
            }
        }

# register
@app.post("/api/register/send-verification-email")
async def send_verification_email(register_data:RegisterVerificationCodeRequest):
    email = register_data.email

    

@app.post("/api/register/create-account")





if __name__ == "__main__":
    uvicorn.run("main:app", port=8030, workers=5, reload=True)
