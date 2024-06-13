import * as module from './module.js';

let url_api_get_cart_infor = module.url_api_get_cart_infor;
let post_method = module.method_post;

let cart_product_content_container = document.querySelector("#cart_product_content_container")
let login_session_token =  sessionStorage.getItem('tokek_for_login_session')

document.addEventListener('DOMContentLoaded', async () => {
    let data = {
        token_login_session:login_session_token
    }
    let response = await module.request_data_to_server({ url: url_api_get_cart_infor, data: data, method: post_method });
    if (response.status) {
        let cart_infors = response.message
        let list_product_html = ``
        let total_price = 0
        for (let product_infor of cart_infors ){
            let price = parseInt(product_infor.price)
            let price_string = module.formatNumber(parseInt(product_infor.price))
            let product_html = `
                <div class="cart__form">
                    <div class="cart__content">
                        <a href="#" class="show_product_detail" data_id_product="${product_infor.id_product}">
                            <div class="cart__content-main">
                                <input type="checkbox" name="" class = "cart__check">
                                <img src="${product_infor.image}" class="cart__content-img" alt="">
                            <div class="cart__content-name"> ${product_infor.product_name}</div>
                        </div>
                        </a>
                            <div class="cart__content-price"> ${price_string} đ</div>
                            <div class="cart__quantity-input">
                                <button class="btn-minus">-</button>
                                <input type="text" class="quantity-value" value="${product_infor.quantity}" pattern="[0-9]*" inputmode="numeric">
                                <button class="btn-plus">+</button>
                              </div>
                            <div class="cart__content-delete">Xóa</div>
                    </div> 
                </div>
            `
            total_price = total_price + price
            list_product_html = list_product_html + product_html
        }
        let cart_content_html = `
            <div class="cart__form">
                    <div class="cart__category">
                        <input type="checkbox" name="" id="cart__check-all">
                        <div class="cart__category-name">Sản phẩm</div>
                        <div class="cart__category-price">Giá</div>
                        <div class="cart__category-ticket">Số lượng</div>
                        <div class="cart__category-operate">Thao tác</div>
                    </div>
                </div>
                
                <!-- thông tin tour trong giỏ hàng -->
                ${list_product_html}
                <div class="cart__form">
                    <div class="cart__cast">
                        <div class="cart__cast-amount">
                            <span>Số sản phẩm trong giỏ hàng:</span>
                            <div class="cart__cast-amount-num">${cart_infors.length}</div>
                        </div>
                        <div class="cart__price">
                            <span>Tổng thanh toán:</span> 
                            <div class="cart__price-sum">${module.formatNumber(total_price)}đ</div>
                        </div>
                        <a href="#" id="payment_btn"><div class="cart__cast-pay-btn btn">Đặt Hàng</div></a>
                    </div>
                </div>
            </div>
        `
        cart_product_content_container.innerHTML = cart_content_html

        document.querySelectorAll('.show_product_detail').forEach(button => {
            button.addEventListener('click', function(event) {
                event.preventDefault(); // Prevent default anchor behavior
                let productId = this.getAttribute('data_id_product');
                // redirectToProductDetail(productId);
                window.location.href = `${module.url_base_front_hosting}/preview.html?id=${productId}`
            });
        });

        const masterCheckbox = document.getElementById('cart__check-all');
        const itemCheckboxes = document.querySelectorAll('.cart__check');

        if (masterCheckbox) {
            masterCheckbox.addEventListener('change', function() {
                itemCheckboxes.forEach(function(checkbox) {
                    checkbox.checked = masterCheckbox.checked;
                });
            });
        }

        const btnMinus = document.querySelectorAll('.btn-minus');
        const btnPlus = document.querySelectorAll('.btn-plus');
        const quantityValues = document.querySelectorAll('.quantity-value');

        btnMinus.forEach(btn => {
            btn.addEventListener('click', () => {
                const quantityValue = btn.parentNode.querySelector('.quantity-value');
                let value = parseInt(quantityValue.value);
                if (value > 1) {
                    quantityValue.value = value - 1;
                }
            });
        });

        btnPlus.forEach(btn => {
            btn.addEventListener('click', () => {
                const quantityValue = btn.parentNode.querySelector('.quantity-value');
                let value = parseInt(quantityValue.value);
                quantityValue.value = value + 1;
            });
        });

        quantityValues.forEach(input => {
            input.addEventListener('input', () => {
                let value = parseInt(input.value);
                if (isNaN(value) || value < 1) {
                    input.value = '1';
                }
            });

            input.addEventListener('input', (event) => {
                event.target.value = event.target.value.replace(/\D/g, '');
            });
        });

    } else {
        alert('Có lỗi xảy ra' + response.message);
    }
});