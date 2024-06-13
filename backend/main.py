from fastapi import FastAPI
from fastapi import Depends, HTTPException, status
from pydantic import BaseModel
from typing import Dict
import uvicorn
from fastapi.middleware.cors import (
    CORSMiddleware,
)
from Database_initialization_and_structure import *
from work_with_databases.work_with_user_and_sesion_service import *
from work_with_databases.work_with_products_and_discount_service import *
from work_with_databases.work_with_comment_and_ranking_service import *
from work_with_databases.work_with_cart_service import *
from work_with_databases.work_with_brand_and_category_service import *
from work_with_databases.work_with_order_service import *
from work_with_databases.admin_services_homepage import *
from work_with_databases.admin_services_product_management import *
from base_codes.hash_function import *
from base_codes.get_token import generate_token
from base_codes.gettime import *
from setting import *
from base_codes.string_python_en import responses
from base_codes.get_code import generate_random_6_digit_number

# from email_with_python.send_emails_using_oulook_server import *
from email_with_python.check_send_email_using_gmail_server import *
from base_codes.security_info import *
from request_model import *

app = FastAPI()  # khởi tạo app fastapi


# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #  chỉ định các nguồn mà bạn muốn chấp nhận yêu cầu từ server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def hello_backend():
    return "hello backend"


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
                        "is_admin": is_admin_user(user_id=check_user_exists["message"]),
                        "user_name": get_user_infor_using_userid["message"]["username"],
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
                    password=passwords["gmail_application_password"],
                    to_email=email,
                    email=emails["gmail"],
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
                password=passwords["gmail_application_password"],
                to_email=email,
                username=username,
                email=emails["gmail"],
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


# api show product in hompage
@app.get("/api/homepage/hompage_layout")
async def hompage_layout():
    list_products = {}
    list_product_newest = get_product_overview(
        order_by="created_at",
        limit=10,
        reverse=True,
    )
    list_products["newest"] = list_product_newest
    for i in range(len(PRODUCT_TYPES_ON_HOMEPAGE)):
        list_products[f"product_type_{i}"] = get_product_overview(
            category_name=PRODUCT_TYPES_ON_HOMEPAGE[i],
            limit=10,
            reverse=True,
        )

    categories_and_brands = get_unique_category_and_brand_names()
    return {
        "response": {
            "message": {
                "list_products": list_products,
                "categories_and_brands": categories_and_brands,
            },
            "status": True,
        }
    }


# api show product detail
@app.post("/api/homepage/show-detailed-products")
async def show_detailed_products(
    request_data: ShowDetailedProductsRequest,
):
    if request_data:
        product_id = request_data.product_id

        product_detail = get_product_detail(product_id=product_id)

        if product_detail is None:
            return {
                "response": {
                    "message": product_detail,
                    "status": False,
                }
            }
        else:
            return {
                "response": {
                    "message": product_detail,
                    "status": True,
                }
            }


# api show user ifor
@app.post("/api/userpage/show-user-infor")
async def show_user_infor(request_data: ShowUserInforRequest):
    token_login_session = request_data.token_login_session

    check_login_session = get_user_id_from_token(token_value=token_login_session)

    if check_login_session["status"]:
        user_id = check_login_session["message"]
        user_infor = get_user(user_id=user_id)
        user_comments = get_user_comments(user_id=user_id, limit=5)
        return {
            "response": {
                "message": {"user_infor": user_infor, "user_comments": user_comments},
                "status": True,
            }
        }
    else:
        return {
            "response": {
                "message": responses["phien_dang_nhap_het_han"],
                "status": False,
            }
        }


# edit user infor
@app.put("/api/userpage/edit-user-information")
async def edit_user_information(request_data: EditUserInformationRequest):
    if request_data:
        token_login_session = request_data.token_login_session
        username = request_data.username
        fullname = request_data.fullname
        address = request_data.address
        phone_number = request_data.phone_number
        image = request_data.image

        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            creat_new_data = creat_new_data_for_update_user(
                phone_number=phone_number,
                address=address,
                fullname=fullname,
                img=image,
                username=username,
            )
            if creat_new_data["status"]:
                new_data = creat_new_data["message"]
                updateuser = update_user(new_data=new_data, user_id=user_id)
                if updateuser["status"]:
                    return {
                        "response": {
                            "message": responses["sua_thong_tin_thanh_cong"],
                            "status": True,
                        }
                    }
                else:
                    print(f"{updateuser['message']}")
                    return {
                        "response": {
                            "message": responses["co_loi_xay_ra"],
                            "status": False,
                        }
                    }
            else:
                print(f"{updateuser['message']}")
                return {
                    "response": {
                        "message": updateuser["message"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }


# Delete the account
@app.delete("/api/userpage/delete-account")
async def delete_account(request_data: DeleteAccountRequest):
    if request_data:
        token_login_session = request_data.token_login_session
        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            deleteuser = delete_user(user_id=user_id)
            if deleteuser["status"]:
                return {
                    "response": {
                        "message": responses["xoa_tai_khoan_thanh_cong"],
                        "status": True,
                    }
                }
            else:
                print(f"{deleteuser['message']}")
                return {
                    "response": {
                        "message": responses["co_loi_xay_ra"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }


# add to cart
@app.post("/api/cartpage/add-product-to-cart")
async def add_product_to_cart(request_data: AddProducttoCartRequest):
    if request_data:
        token_login_session = request_data.token_login_session
        product_id = request_data.product_id
        quantity = request_data.quantity

        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            addtocart = add_to_cart(
                quantity=quantity, product_id=product_id, user_id=user_id
            )
            if addtocart["status"]:
                return {
                    "response": {
                        "message": responses[
                            "da_them_san_pham_vao_gio_hang_thanh_cong"
                        ],
                        "status": True,
                    }
                }
            else:

                return {
                    "response": {
                        "message": responses["co_loi_xay_ra"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }


@app.post("/api/cartpage/get_cart_infor")
async def get_cart_infor_with_user_id(request_data: GetCartInforRequest):
    if request_data:
        token_login_session = request_data.token_login_session
        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            get_cart_infor_request = get_cart_info(user_id=user_id)
            if get_cart_infor_request:
                return {
                    "response": {
                        "message": get_cart_infor_request,
                        "status": True,
                    }
                }
            else:

                return {
                    "response": {
                        "message": responses["co_loi_xay_ra"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }


# edit cart quantity
@app.put("/api/cartpage/update-cart-item-quantity")
async def update_cart_item_quantity1(request_data: UpdateCartItemQuantityRequest):
    if request_data:
        token_login_session = request_data.token_login_session
        product_id = request_data.product_id
        quantity = request_data.quantity

        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            updatecartitemquantity = update_cart_item_quantity(
                quantity=quantity, product_id=product_id, user_id=user_id
            )
            if updatecartitemquantity["status"]:
                return {
                    "response": {
                        "message": responses[
                            "da_cap_nhat_so_luong_san_pham_trong_gio_hang_thanh_cong"
                        ],
                        "status": True,
                    }
                }
            else:

                return {
                    "response": {
                        "message": responses["co_loi_xay_ra"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }


# delete product in cart
@app.delete("/api/cartpage/remove-product-from-cart")
async def remove_product_from_cart1(request_data: RemoveProductFromCartRequest):
    if request_data:
        token_login_session = request_data.token_login_session
        product_id = request_data.product_id

        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            removeproductfromcart = remove_product_from_cart(
                product_id=product_id, user_id=user_id
            )
            if removeproductfromcart["status"]:
                return {
                    "response": {
                        "message": responses[
                            "da_xoa_san_pham_khoi_gio_hang_thanh_cong"
                        ],
                        "status": True,
                    }
                }
            else:
                print(f"{removeproductfromcart['message']}")
                return {
                    "response": {
                        "message": responses["co_loi_xay_ra"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }


@app.post("/api/search-products-by-keyword")
async def search_products_by_keyword(request_data: SearchProductsByKeywordRequest):
    if request_data:
        keyword = request_data.keyword
        products = search_products(keyword=keyword)

        if products:
            products_list = []
            for product in products:
                product_dict = product.__dict__
                product_dict.pop(
                    "_sa_instance_state"
                )  # Loại bỏ thuộc tính không cần thiết
                products_list.append(product_dict)

            return {
                "response": {
                    "message": products_list,
                    "status": True,
                }
            }
        else:
            return {
                "response": {
                    "message": responses["khong_tim_thay_san_pham"],
                    "status": False,
                }
            }
    else:
        return {
            "response": {
                "message": responses["du_lieu_yeu_cau_khong_hop_le"],
                "status": False,
            }
        }


# filter product
@app.post("/api/filter-products-homepage")
async def filter_products_homepage(request_data: FilterProductsHomepageRequest):
    if request_data:
        category_name = request_data.category_name
        brand_name = request_data.brand_name
        products = filter_products(category_name=category_name, brand_name=brand_name)
        if products:
            return {
                "response": {
                    "status": True,
                    "message": [product.__dict__ for product in products],
                }
            }
        else:
            return {
                "response": {
                    "status": False,
                    "message": responses["khong_tim_thay_san_pham"],
                }
            }


# oder
@app.post("/api/place-order")
async def place_order(request_data: CreateOrderRequest):
    token_login_session = request_data.token_login_session
    user_id = request_data.user_id
    list_order_items = request_data.list_order_items

    # order_id = place_order(user_id, products)

    # return {"response": {"order_id": order_id, "message": "Order placed successfully"}}


##############################################################################
############################## admin management ##############################
##############################################################################


@app.post("/api/admin/admin-homepage")
async def admin_homepage(request_data: AdminHomepageRequest):
    if request_data:
        token_login_session = request_data.token_login_session
        timeframe: str = request_data.timeframe
        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            is_admin = is_admin_user(user_id=user_id)
            if is_admin:
                data_4_parameter = get_statistics(timeframe=timeframe)
                data_lineChart = get_data_for_lineChart_by_period(period=timeframe)
                data_pieChart = get_data_for_pieChart_by_period(period=timeframe)
                data_barChart = get_data_for_barChart_data_by_period(
                    time_period=timeframe
                )

                if (
                    data_4_parameter is not None
                    and data_barChart is not None
                    and data_lineChart is not None
                    and data_pieChart is not None
                ):
                    return {
                        "response": {
                            "status": True,
                            "message": {
                                "data_4_parameter": data_4_parameter,
                                "data_lineChart": data_lineChart,
                                "data_pieChart": data_pieChart,
                                "data_barChart": data_barChart,
                            },
                        }
                    }

                else:

                    return {
                        "response": {
                            "message": responses["co_loi_xay_ra"],
                            "status": False,
                        }
                    }
            else:
                return {
                    "response": {
                        "message": responses["tai_khoan_khong_co_quyen_nay"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }

    else:
        return {
            "response": {
                "message": responses["du_lieu_yeu_cau_khong_hop_le"],
                "status": False,
            }
        }


##############################################################################
############################## admin product management ######################
##############################################################################


@app.post("/api/admin/admin_product_management_preview")
async def admin_product_management_preview(
    request_data: AdminProductManagementPreviewRequest,
):
    if request_data:
        token_login_session = request_data.token_login_session
        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            is_admin = is_admin_user(user_id=user_id)
            if is_admin:
                all_product = get_all_products_admin_product_management()
                # print(all_product)
                if all_product:
                    return {
                        "response": {
                            "message": all_product,
                            "status": True,
                        }
                    }
                else:
                    return {
                        "response": {
                            "message": responses["co_loi_xay_ra"],
                            "status": False,
                        }
                    }
            else:
                return {
                    "response": {
                        "message": responses["tai_khoan_khong_co_quyen_nay"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }

    else:
        return {
            "response": {
                "message": responses["du_lieu_yeu_cau_khong_hop_le"],
                "status": False,
            }
        }


@app.delete("/api/admin/delete_product")
async def delete_product_admin_product_management(
    request_data: AdminProductManagementDeleteProductRequest,
):
    if request_data:
        token_login_session = request_data.token_login_session
        product_id = request_data.product_id
        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            is_admin = is_admin_user(user_id=user_id)
            if is_admin:
                check_delete_product = delete_product(product_id=product_id)
                if check_delete_product["status"]:
                    return {
                        "response": {
                            "message": responses["da_xoa_san_pham_thanh_cong"],
                            "status": True,
                        }
                    }
                else:
                    print(check_delete_product["message"])
                    return {
                        "response": {
                            "message": responses["co_loi_xay_ra"],
                            "status": False,
                        }
                    }
            else:
                return {
                    "response": {
                        "message": responses["tai_khoan_khong_co_quyen_nay"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }

    else:
        return {
            "response": {
                "message": responses["du_lieu_yeu_cau_khong_hop_le"],
                "status": False,
            }
        }


@app.get("/api/admin/get_brands_and_catagories")
async def get_brands_and_catagories_product_management():
    brands_and_catagories = get_unique_category_and_brand_names()
    if brands_and_catagories:
        # print(brands_and_catagories)
        return {
            "response": {
                "message": brands_and_catagories,
                "status": True,
            }
        }
    else:
        return {
            "response": {
                "message": responses["co_loi_xay_ra"],
                "status": False,
            }
        }


# api add product
@app.post("/api/admin/add-new-product")
async def add_new_product_admin_product_management(request_data: AddNewProductRequest):

    if request_data:
        token_login_session = request_data.token_login_session
        product_name: str = request_data.product_name
        price: float = request_data.price
        description: str = request_data.description
        category_id: int = request_data.category_id
        brand_id: int = request_data.brand_id
        quantity: int = request_data.quantity
        image: str = request_data.image
        discount_enddate = request_data.discount_enddate
        discount_percentage = request_data.discount_percentage
        discount_startdate = request_data.discount_startdate

        # check admin
        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            is_admin = is_admin_user(user_id=user_id)
            if is_admin:
                addproduct = add_new_product(
                    product_name=product_name,
                    image=image,
                    brand_id=brand_id,
                    category_id=category_id,
                    description=description,
                    price=price,
                    discount_percentage=discount_percentage,
                    end_date=discount_enddate,
                    start_date=discount_startdate,
                    quantity=quantity,
                )
                if addproduct["status"]:
                    return {
                        "response": {
                            "status": True,
                            "message": responses["da_them_san_pham_thanh_cong"],
                        }
                    }
                else:
                    return {
                        "response": {
                            "status": False,
                            "message": responses["ten_san_pham_da_ton_tai"],
                        }
                    }
            else:
                return {
                    "response": {
                        "message": responses["tai_khoan_khong_co_quyen_nay"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }

    else:
        return {
            "response": {
                "message": responses["du_lieu_yeu_cau_khong_hop_le"],
                "status": False,
            }
        }


@app.get("/api/admin/get_product_detail")
async def get_product_detail_admin_product_management():
    return


@app.get("/api/admin/get_all_brands_admin_brand_management")
async def get_all_brands_admin_brand_management():
    data = get_all_brands()
    if data is not None:
        return {
            "response": {
                "status": True,
                "message": data,
            }
        }
    else:
        {
            "response": {
                "status": False,
                "message": responses["co_loi_xay_ra"],
            }
        }


@app.post("/api/admin/add_new_brand")
async def add_new_brand_product_management(
    request_data: AdminAddNewBrandProductManagementRequest,
):
    if request_data:
        token_login_session = request_data.token_login_session
        brand_name: str = request_data.brand_name
        description = request_data.description
        img = request_data.img
        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            is_admin = is_admin_user(user_id=user_id)
            if is_admin:
                check_add_brand_product_management = add_brand_product_management(
                    img=img, brand_name=brand_name, description=description
                )
                if check_add_brand_product_management["status"]:
                    return {
                        "response": {
                            "message": responses["da_them_brand_thanh_cong"],
                            "status": True,
                        }
                    }
                else:
                    print(check_add_brand_product_management["message"])
                    return {
                        "response": {
                            "message": check_add_brand_product_management["message"],
                            "status": False,
                        }
                    }
            else:
                return {
                    "response": {
                        "message": responses["tai_khoan_khong_co_quyen_nay"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }
    else:
        return {
            "response": {
                "message": responses["du_lieu_yeu_cau_khong_hop_le"],
                "status": False,
            }
        }


@app.post("/api/admin/get_brand_detail")
async def get_brand_detail_admin_product_managetmant(
    request_data: AdmiGetBrandDetailProductManagementRequest,
):
    if request_data:
        token_login_session = request_data.token_login_session
        brand_id: str = request_data.brand_id
        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            is_admin = is_admin_user(user_id=user_id)
            if is_admin:
                brand_detail = get_brand_details(brand_id=brand_id)
                if brand_detail:

                    return {
                        "response": {
                            "message": brand_detail,
                            "status": True,
                        }
                    }
                else:
                    raise HTTPException(status_code=404, detail="Brand not found")

            else:
                return {
                    "response": {
                        "message": responses["tai_khoan_khong_co_quyen_nay"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }
    else:
        return {
            "response": {
                "message": responses["du_lieu_yeu_cau_khong_hop_le"],
                "status": False,
            }
        }


# delete brand
@app.delete("/api/admin/delete_brand")
async def delete_brand_product_management(
    request_data: AdmiDeleteBrandProductManagementRequest,
):
    if request_data:
        token_login_session = request_data.token_login_session
        brand_id: str = request_data.brand_id
        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            is_admin = is_admin_user(user_id=user_id)
            if is_admin:
                delete_brand_product_management_with_id(brand_id=brand_id)
                return {
                    "response": {
                        "message": responses["da_xoa_brand_thanh_cong"],
                        "status": True,
                    }
                }

            else:
                return {
                    "response": {
                        "message": responses["tai_khoan_khong_co_quyen_nay"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }
    else:
        return {
            "response": {
                "message": responses["du_lieu_yeu_cau_khong_hop_le"],
                "status": False,
            }
        }


@app.put("/api/admin/edit_brand")
async def edit_brand_admin_product_management(
    request_data: AdmiEditBrandProductManagementRequest,
):
    if request_data:
        token_login_session = request_data.token_login_session
        brand_id: str = request_data.brand_id
        brand_name = request_data.brand_name
        brand_img = request_data.brand_img
        brand_description = request_data.brand_description
        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            is_admin = is_admin_user(user_id=user_id)
            if is_admin:
                check_update_brand = update_brand(
                    brand_id=brand_id,
                    brand_name=brand_name,
                    description=brand_description,
                    img=brand_img,
                )
                if check_update_brand["status"]:
                    return {
                        "response": {
                            "message": responses["da_cap_nhat_brand_thanh_cong"],
                            "status": True,
                        }
                    }
                else:
                    return {
                        "response": {
                            "message": check_update_brand["message"],
                            "status": False,
                        }
                    }

            else:
                return {
                    "response": {
                        "message": responses["tai_khoan_khong_co_quyen_nay"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }
    else:
        return {
            "response": {
                "message": responses["du_lieu_yeu_cau_khong_hop_le"],
                "status": False,
            }
        }


@app.get("/api/admin/get_all_categories")
async def get_all_categories_admin_prodcut_management():
    all_categories = get_all_categories()
    if all_categories:

        return {
            "response": {
                "message": all_categories,
                "status": True,
            }
        }
    else:
        return {
            "response": {
                "message": responses["co_loi_xay_ra"],
                "status": False,
            }
        }


@app.post("/api/admin/get_a_category")
async def get_a_categoryadmin_prodcut_management(
    request_data: AdminGetACatagoryProductManagementRequest,
):
    if request_data:
        token_login_session = request_data.token_login_session
        catagory_id = request_data.catagory_id
        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            is_admin = is_admin_user(user_id=user_id)
            if is_admin:
                category = get_category(category_id=catagory_id)
                if category:
                    return {
                        "response": {
                            "message": category,
                            "status": True,
                        }
                    }
                else:
                    return {
                        "response": {
                            "message": responses["co_loi_xay_ra"],
                            "status": False,
                        }
                    }

            else:
                return {
                    "response": {
                        "message": responses["tai_khoan_khong_co_quyen_nay"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }
    else:
        return {
            "response": {
                "message": responses["du_lieu_yeu_cau_khong_hop_le"],
                "status": False,
            }
        }


@app.post("/api/admin/add_new_category")
async def add_new_category_admin_product_management(
    request_data: AdminAddNewCatagoryProductManagementRequest,
):
    if request_data:
        token_login_session = request_data.token_login_session
        catagory_name = request_data.catagory_name
        catagory_description = request_data.catagory_description
        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            is_admin = is_admin_user(user_id=user_id)
            if is_admin:
                check_add_category = add_category(
                    category_name=catagory_name, description=catagory_description
                )
                if check_add_category["status"]:
                    return {
                        "response": {
                            "message": responses["da_them_the_loai_thanh_cong"],
                            "status": True,
                        }
                    }
                else:
                    return {
                        "response": {
                            "message": check_add_category["message"],
                            "status": False,
                        }
                    }

            else:
                return {
                    "response": {
                        "message": responses["tai_khoan_khong_co_quyen_nay"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }
    else:
        return {
            "response": {
                "message": responses["du_lieu_yeu_cau_khong_hop_le"],
                "status": False,
            }
        }


@app.put("/api/admin/edit_category")
async def edit_category_admin_product_management(
    request_data: AdminEditCatagoryProductManagementRequest,
):
    print(request_data)
    if request_data:
        token_login_session = request_data.token_login_session
        catagory_id = request_data.catagory_id
        catagory_name = request_data.catagory_name
        catagory_description = request_data.catagory_description
        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            is_admin = is_admin_user(user_id=user_id)
            if is_admin:
                check_edit_category = edit_category_data(
                    category_id=catagory_id,
                    new_category_name=catagory_name,
                    new_description=catagory_description,
                )
                if check_edit_category["status"]:
                    return {
                        "response": {
                            "message": responses["da_cap_nhat_the_loai_thanh_cong"],
                            "status": True,
                        }
                    }
                else:
                    return {
                        "response": {
                            "message": check_edit_category["message"],
                            "status": False,
                        }
                    }

            else:
                return {
                    "response": {
                        "message": responses["tai_khoan_khong_co_quyen_nay"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }
    else:
        return {
            "response": {
                "message": responses["du_lieu_yeu_cau_khong_hop_le"],
                "status": False,
            }
        }


@app.delete("/api/admin/delete_category")
async def delete_category_admin_product_management(
    request_data: AdminDeleteCatagoryProductManagementRequest,
):
    if request_data:
        token_login_session = request_data.token_login_session
        catagory_id = request_data.catagory_id
        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            is_admin = is_admin_user(user_id=user_id)
            if is_admin:
                delete_catagory_product_management_with_id(category_id=catagory_id)

                return {
                    "response": {
                        "message": responses["da_xoa_the_loai_thanh_cong"],
                        "status": True,
                    }
                }

            else:
                return {
                    "response": {
                        "message": responses["tai_khoan_khong_co_quyen_nay"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }
    else:
        return {
            "response": {
                "message": responses["du_lieu_yeu_cau_khong_hop_le"],
                "status": False,
            }
        }


# edit product
@app.put("/api/admin/edit-product")
async def edit_product(request_data: EditProductRequest):
    if request_data:
        token_login_session = request_data.token_login_session
        product_id: str = request_data.product_id
        product_name: str = request_data.product_name
        price: float = request_data.price
        description: str = request_data.description
        category_id: int = request_data.category_id
        brand_id: int = request_data.brand_id
        quantity: int = request_data.quantity
        image: str = request_data.image

        # check admin
        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            is_admin = is_admin_user(user_id=user_id)
            if is_admin:
                editproductdata = edit_product_data(
                    product_id=product_id,
                    new_brand_id=brand_id,
                    new_category_id=category_id,
                    new_description=description,
                    new_image=image,
                    new_price=price,
                    new_product_name=product_name,
                    new_quantity=quantity,
                )
                if editproductdata["status"]:
                    return {
                        "response": {
                            "status": True,
                            "message": responses["sua_thong_tin_san_pham_thanh_cong"],
                        }
                    }
                else:
                    print(f"Lỗi {editproductdata['message']}")
                    return {
                        "response": {
                            "status": False,
                            "message": responses["co_loi_xay_ra"],
                        }
                    }
            else:
                return {
                    "response": {
                        "message": responses["tai_khoan_khong_co_quyen_nay"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }
    else:
        return {
            "response": {
                "message": responses["du_lieu_yeu_cau_khong_hop_le"],
                "status": False,
            }
        }


##############################################################################
############################## admin order management ########################
##############################################################################


@app.put("/api/admin/update-order-status-product")
async def edit_product(request_data: UpdateOrderStatusRequest):
    if request_data:
        token_login_session = request_data.token_login_session
        new_order_status = request_data.new_order_status
        order_id = request_data.order_id

        # check admin
        check_login_session = get_user_id_from_token(token_value=token_login_session)

        if check_login_session["status"]:
            user_id = check_login_session["message"]
            is_admin = is_admin_user(user_id=user_id)
            if is_admin:
                updateorderstatus = update_order_status(
                    order_id=order_id, new_status=new_order_status
                )
                if updateorderstatus["status"]:
                    return {
                        "response": {
                            "status": True,
                            "message": responses[
                                "cap_nhat_trang_thai_don_hang_thanh_cong"
                            ],
                        }
                    }
                else:
                    print(f"Lỗi {updateorderstatus['message']}")
                    return {
                        "response": {
                            "status": False,
                            "message": responses["co_loi_xay_ra"],
                        }
                    }
            else:
                return {
                    "response": {
                        "message": responses["tai_khoan_khong_co_quyen_nay"],
                        "status": False,
                    }
                }
        else:
            return {
                "response": {
                    "message": responses["phien_dang_nhap_het_han"],
                    "status": False,
                }
            }
    else:
        return {
            "response": {
                "message": responses["du_lieu_yeu_cau_khong_hop_le"],
                "status": False,
            }
        }


# show all product in admin page
# @app.get("/api/")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8030, reload=True)
