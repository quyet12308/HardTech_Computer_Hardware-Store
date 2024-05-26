from fastapi import FastAPI
from fastapi import Depends, HTTPException, status
from pydantic import BaseModel
from typing import Dict
import uvicorn
from fastapi.middleware.cors import (
    CORSMiddleware,
)
from work_with_databases.Database_initialization_and_structure import *
from work_with_databases.work_with_user_service import *
from base_codes.hash_function import *
from base_codes.get_token import generate_token
from base_codes.gettime import *
from setting import *
from base_codes.string_python_en import responses
from base_codes.get_code import generate_random_6_digit_number
from email_with_python.send_emails_using_oulook_server import *
from base_codes.security_info import *

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
    email: str
    username: str


class RegisterCreateAccountRequest(BaseModel):
    email: str
    username: str
    password: str
    code: str


class ForgotPasswordForgotPasswordRequest(BaseModel):
    email: str


class ForgotPasswordResetPasswordRequest(BaseModel):
    email: str
    new_password: str
    code: str


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
async def register_send_verification_email(
    register_data: RegisterVerificationCodeRequest,
):
    email = register_data.email
    username = register_data.username
    if email:
        check_exists_user_by_email = get_user(
            email=email
        )  # truy xuất dữ liệu bằng email cho chức năng đăng ký
        if check_exists_user_by_email["status"]:
            return {
                "response": {
                    "message": responses["email_da_duoc_dang_ky"],
                    "status": False,
                }
            }
        else:
            check_username = is_username_taken(
                username=username
            )  # lấy thông tin người dùng
            if check_username:
                return {
                    "response": {
                        "message": responses["user_da_ton_tai"],
                        "status": False,
                    }
                }
            else:
                # send confirm email
                code_randum = generate_random_6_digit_number()

                send_email_confirm_registration(
                    username=username,
                    code=code_randum,
                    password=passwords["outlook"],
                    to_email=email,
                    email=emails["outlook"],
                    minutes=WAITING_TIME_FOR_CODE_IN_EMAIL,
                )  # gửi email
                add_authentication_code(
                    code=code_randum,
                    email=email,
                    expiration_time=convert_to_datetime(
                        time_string=add_time_to_datetime(
                            minutes=WAITING_TIME_FOR_CODE_IN_EMAIL
                        )["message"]
                    ),
                )  # lưu data vào catcha

                return {
                    "response": {
                        "message": responses["check_email_to_get_code"],
                        "status": True,
                    }
                }
                # return json.dumps(a)
    else:
        return {"response": {"message": responses["co_loi_xay_ra"], "status": False}}


@app.post("/api/register/create-account")
async def register_create_account(request_data: RegisterCreateAccountRequest):
    if request_data:
        password = request_data.password
        email = request_data.email
        code = request_data.code
        username = request_data.username

        check_code_verification = query_authentication_code_by_email(
            email=email
        )  # hàm check code catcha
        if check_code_verification["status"]:
            check_time = check_expired_time(
                input_time=check_code_verification["message"].expiration_time
            )  # true nếu tạo và truy cập trong khoảng 3 phút
            if check_time:
                if code == check_code_verification["message"].code:
                    add_user(
                        email=email,
                        password=hash_password(password=password),
                        username=username,
                    )  # lưu thông tin
                    return {
                        "response": {
                            "message": responses["dang_ky_thanh_cong"],
                            "status": True,
                        }
                    }
                else:
                    return {
                        "response": {"message": responses["sai_code"], "status": False}
                    }
            else:
                return {
                    "response": {
                        "message": responses["code_bi_qua_thoi_gian"],
                        "status": False,
                    }
                }
        else:
            {
                "response": {
                    "message": responses["khong_tim_thay_email_dang_ky_code"],
                    "status": False,
                }
            }
    else:
        return {"response": {"message": responses["co_loi_xay_ra"], "status": False}}


@app.post("/api/forgot-password/forgot-password")
async def forgot_password(request_data: ForgotPasswordForgotPasswordRequest):
    if request_data:
        email = request_data.email
        check_exists_user_by_email = get_user(email=email)
        if check_exists_user_by_email["status"]:
            code = (
                generate_random_6_digit_number()
            )  # tạo code để xác nhận cho chức năng quên mật khẩu
            username = check_exists_user_by_email["message"]["username"]
            add_authentication_code(
                code=code,
                email=email,
                expiration_time=convert_to_datetime(
                    time_string=add_time_to_datetime(
                        minutes=WAITING_TIME_FOR_CODE_IN_EMAIL
                    )["message"]
                ),
            )  # lưu data vào catcha
            send_email_forgot_password(
                code=code,
                password=passwords["outlook"],
                to_email=email,
                username=username,
                email=emails["outlook"],
                minutes=WAITING_TIME_FOR_CODE_IN_EMAIL,
            )  # giử email quên mật khẩu
            return {
                "response": {
                    "message": responses["check_email_to_get_code"],
                    "status": True,
                }
            }

        else:
            return {
                "response": {
                    "message": responses["email_chua_duoc_dang_ky"],
                    "status": False,
                }
            }


@app.post("/api/forgot-password/reset-password")
async def forgot_password_reset_password(
    request_data: ForgotPasswordResetPasswordRequest,
):
    if request_data:
        new_password = request_data.new_password
        email = request_data.email
        code = request_data.code

        check_code_verification = query_authentication_code_by_email(email=email)

        if check_code_verification["status"]:
            check_time = check_expired_time(
                input_time=check_code_verification["message"].expiration_time
            )
            if check_time:
                if code == check_code_verification["message"].code:
                    new_hash_password = hash_password(password=new_password)
                    new_user_data = creat_new_data_for_update_user(
                        password=new_hash_password
                    )
                    update_user(
                        new_data=new_user_data["message"],
                        email=email,
                    )
                    # update_user_by_email(email=email,new_password=new_password,new_username=username1)
                    return {
                        "response": {
                            "message": responses["cap_nhat_mat_khau_moi_thanh_cong"],
                            "status": True,
                        }
                    }
                else:
                    return {
                        "response": {"message": responses["sai_code"], "status": False}
                    }
            else:
                return {
                    "response": {
                        "message": responses["code_bi_qua_thoi_gian"],
                        "status": False,
                    }
                }


@app.get("/api/homepage/list-products")
async def get_list_products_for_homepage():
    list_product = get_product_overview()
    return {
        "response": {
            "message": {"list_products": list_product},
            "status": True,
        }
    }


if __name__ == "__main__":
    uvicorn.run("main:app", port=8030, reload=True)
