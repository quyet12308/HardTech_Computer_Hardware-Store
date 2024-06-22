from work_with_payment_services.main_momo_service import *
from work_with_payment_services.main_paypal_service import *
from work_with_payment_services.main_stripe_service import *
from work_with_payment_services.main_vnpay_service import *
from work_with_payment_services.main_zalopay_service import *
from work_with_payment_services.main_9pay_service import *
from work_with_payment_services.convert_money import *


def create_url_for_payment(
    payment_method: str,
    amount: int,
    description: str,
    redirect_url: str,
    order_id: int,
    user_id: int,
    user_name: str,
    phone_number: int,
    email: str = None,
    full_name: str = None,
):
    if payment_method == "zalopay":

        order_url = create_zalopay_order(
            amount=amount,
            description=description,
            email=email,
            full_name=full_name,
            order_id=order_id,
            phone_number=phone_number,
            redirect_url=redirect_url,
            user_id=user_id,
            user_name=user_name,
        )
        if order_url:
            return {
                "status": True,
                "message": {
                    "order_url": order_url["result"]["order_url"],
                    "check_sum": order_url["checksum"],
                },
            }
        else:
            return {"status": False, "message": ""}
    elif payment_method == "momo":
        payment_url = create_momo_payment_url(
            amount=amount,
            ipn_url="https://webhook.site/your-ipn-url",
            order_id=order_id,
            order_info=description,
            redirect_url=redirect_url,
        )
        if payment_url["status"]:
            return {
                "status": True,
                "message": {
                    "order_url": payment_url["message"]["payment_url"],
                    "check_sum": payment_url["message"]["check_sum"],
                },
            }
        else:
            return {"status": False, "message": ""}

    elif payment_method == "paypal":
        payment_url = create_paypal_payment_url(
            amount=convert_money_from_vnd_to_usd(amount_vnd=amount),
            cancel_url="http://127.0.0.1:5500/cancel_payment.html",
            return_url=redirect_url,
            description=description,
        )
        if payment_url["status"]:
            return {
                "status": True,
                "message": {
                    "order_url": payment_url["message"]["payment_url"],
                    "check_sum": payment_url["message"]["check_sum"],
                },
            }
        else:
            return {"status": False, "message": ""}
    elif payment_method == "stripe":
        payment_url = create_stripe_payment_url(
            amount=(convert_money_from_vnd_to_usd(amount_vnd=amount) * 100),
            success_url=redirect_url,
            cancel_url="http://127.0.0.1:5500/cancel_payment.html",
            order_id=order_id,
            product_name=description,
        )
        if payment_url["status"]:
            return {
                "status": True,
                "message": {
                    "order_url": payment_url["message"]["payment_url"],
                    "check_sum": payment_url["message"]["check_sum"],
                },
            }
        else:
            return {"status": False, "message": ""}
    elif payment_method == "9pay":
        payment_url = create_nine_payment_url(
            amount=int(amount),
            description=str(description),
            invoice_no=int(order_id),
            return_url=str(redirect_url),
        )
        if payment_url["status"]:
            return {
                "status": True,
                "message": {
                    "order_url": payment_url["message"]["payment_url"],
                    "check_sum": payment_url["message"]["check_sum"],
                },
            }
        else:
            return {"status": False, "message": ""}
    else:
        return {"status": False, "message": "No support this payment method"}
