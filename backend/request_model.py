from pydantic import BaseModel
from typing import Optional


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


class ShowDetailedProductsRequest(BaseModel):
    product_id: str


class ShowUserInforRequest(BaseModel):
    token_login_session: str


class EditUserInformationRequest(BaseModel):
    token_login_session: str
    username: str
    fullname: str
    address: str
    phone_number: str
    image: str


class DeleteAccountRequest(BaseModel):
    token_login_session: str


class AddProducttoCartRequest(BaseModel):
    token_login_session: str
    product_id: str
    quantity: int


class UpdateCartItemQuantityRequest(BaseModel):
    token_login_session: str
    product_id: str
    quantity: str


class RemoveProductFromCartRequest(BaseModel):
    token_login_session: str
    product_id: str


class SearchProductsByKeywordRequest(BaseModel):
    keyword: str


class GetCartInforRequest(BaseModel):
    token_login_session: str


class FilterProductsHomepageRequest(BaseModel):
    category_name: str
    brand_name: str


class CreateOrderRequest(BaseModel):
    token_login_session: str
    list_order_items: list


class GetOrderDetailPreviewRequest(BaseModel):
    token_login_session: str
    order_id: int


class AddNewProductRequest(BaseModel):
    token_login_session: str
    product_name: str
    description: str
    price: float
    quantity: int
    category_id: int
    brand_id: int
    image: str
    discount_percentage: Optional[int] = None
    discount_startdate: Optional[str] = None
    discount_enddate: Optional[str] = None


class EditProductRequest(BaseModel):
    token_login_session: str
    product_id: str
    product_name: str
    price: float
    description: str
    category_id: int
    brand_id: int
    quantity: int
    image: str


class UpdateOrderStatusRequest(BaseModel):
    token_login_session: str
    new_order_status: str
    order_id: str


class PaymentForOrderRequest(BaseModel):
    token_login_session: str
    new_order_status: str
    order_id: str


class CreateUrlForPaymentRequest(BaseModel):
    token_login_session: str
    order_id: str
    user_name: str
    phone_number: str
    address: str
    note: str
    payment_method: str
    redirecturl: str


class UpdateOrderStatusWhenUserPaymentSuccessRequest(BaseModel):
    token_login_session: str
    checksum: str
    payment_method: str


class AdminHomepageRequest(BaseModel):
    token_login_session: str
    timeframe: str


class AdminProductManagementPreviewRequest(BaseModel):
    token_login_session: str


class AdminProductManagementDeleteProductRequest(BaseModel):
    token_login_session: str
    product_id: str


class AdminAddNewBrandProductManagementRequest(BaseModel):
    token_login_session: str
    brand_name: str
    description: str
    img: str


class AdmiDeleteBrandProductManagementRequest(BaseModel):
    token_login_session: str
    brand_id: str


class AdmiEditBrandProductManagementRequest(BaseModel):
    token_login_session: str
    brand_id: str
    brand_name: Optional[str]
    brand_img: Optional[str]
    brand_description: Optional[str]


class AdmiGetBrandDetailProductManagementRequest(BaseModel):
    token_login_session: str
    brand_id: str


class AdminAddNewCatagoryProductManagementRequest(BaseModel):
    token_login_session: str
    catagory_name: str
    catagory_description: str


class AdminEditCatagoryProductManagementRequest(BaseModel):
    token_login_session: str
    catagory_id: int
    catagory_name: str
    catagory_description: str


class AdminDeleteCatagoryProductManagementRequest(BaseModel):
    token_login_session: str
    catagory_id: str


class AdminGetACatagoryProductManagementRequest(BaseModel):
    token_login_session: str
    catagory_id: str
