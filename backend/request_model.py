from pydantic import BaseModel


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
    quantity: str


class UpdateCartItemQuantityRequest(BaseModel):
    token_login_session: str
    product_id: str
    quantity: str


class RemoveProductFromCartRequest(BaseModel):
    token_login_session: str
    product_id: str


class SearchProductsByKeywordRequest(BaseModel):
    keyword: str
