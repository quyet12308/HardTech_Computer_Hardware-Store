// import * as module from './module.js';

// let url_api_get_cart_infor = module.url_api_get_cart_infor;
// let post_method = module.method_post;

// let cart_product_content_container = document.querySelector("#cart_product_content_container")
// let login_session_token =  sessionStorage.getItem('tokek_for_login_session')

// document.addEventListener('DOMContentLoaded', async () => {
//     let data = {
//         token_login_session:login_session_token
//     }
//     let response = await module.request_data_to_server({ url: url_api_get_cart_infor, data: data, method: post_method });
//     if (response.status) {
//         let cart_infors = response.message
//         let list_product_html = ``
//         let total_price = 0
//         for (let product_infor of cart_infors ){
//             let price = parseInt(product_infor.price)
//             let quantity_product = parseInt(product_infor.quantity)
//             let price_string = module.formatNumber(parseInt(product_infor.price))
//             let product_html = `
//                 <div class="cart__form">
//                     <div class="cart__content">
//                         <a href="#" class="show_product_detail" data_id_product="${product_infor.id_product}">
//                             <div class="cart__content-main">
//                                 <input type="checkbox" name="" class = "cart__check">
//                                 <img src="${product_infor.image}" class="cart__content-img" alt="">
//                             <div class="cart__content-name"> ${product_infor.product_name}</div>
//                         </div>
//                         </a>
//                             <div class="cart__content-price"> ${price_string} đ</div>
//                             <div class="cart__quantity-input">
//                                 <button class="btn-minus">-</button>
//                                 <input type="text" class="quantity-value" value="${product_infor.quantity}" pattern="[0-9]*" inputmode="numeric">
//                                 <button class="btn-plus">+</button>
//                               </div>
//                             <div class="cart__content-delete">Xóa</div>
//                     </div> 
//                 </div>
//             `
//             // total_price = total_price + (price * quantity_product)
//             // list_product_html = list_product_html + product_html
//         }
//         let price_value = document.querySelector()
//         let cart_content_html = `
//             <div class="cart__form">
//                     <div class="cart__category">
//                         <input type="checkbox" name="" id="cart__check-all">
//                         <div class="cart__category-name">Sản phẩm</div>
//                         <div class="cart__category-price">Giá</div>
//                         <div class="cart__category-ticket">Số lượng</div>
//                         <div class="cart__category-operate">Thao tác</div>
//                     </div>
//                 </div>
                
//                 <!-- thông tin tour trong giỏ hàng -->
//                 ${list_product_html}
//                 <div class="cart__form">
//                     <div class="cart__cast">
//                         <div class="cart__cast-amount">
//                             <span>Số sản phẩm trong giỏ hàng:</span>
//                             <div class="cart__cast-amount-num">${cart_infors.length}</div>
//                         </div>
//                         <div class="cart__price">
//                             <span>Tổng thanh toán:</span> 
//                             <div class="cart__price-sum">${module.formatNumber(total_price)}đ</div>
//                         </div>
//                         <a href="#" id="payment_btn"><div class="cart__cast-pay-btn btn">Đặt Hàng</div></a>
//                     </div>
//                 </div>
//             </div>
//         `
//         cart_product_content_container.innerHTML = cart_content_html

//         document.querySelectorAll('.show_product_detail').forEach(button => {
//             button.addEventListener('click', function(event) {
//                 event.preventDefault(); // Prevent default anchor behavior
//                 let productId = this.getAttribute('data_id_product');
//                 // redirectToProductDetail(productId);
//                 window.location.href = `${module.url_base_front_hosting}/preview.html?id=${productId}`
//             });
//         });

//         const masterCheckbox = document.getElementById('cart__check-all');
//         const itemCheckboxes = document.querySelectorAll('.cart__check');

//         if (masterCheckbox) {
//             masterCheckbox.addEventListener('change', function() {
//                 itemCheckboxes.forEach(function(checkbox) {
//                     checkbox.checked = masterCheckbox.checked;
//                 });
//             });
//         }

//         const btnMinus = document.querySelectorAll('.btn-minus');
//         const btnPlus = document.querySelectorAll('.btn-plus');
//         const quantityValues = document.querySelectorAll('.quantity-value');

//         btnMinus.forEach(btn => {
//             btn.addEventListener('click', () => {
//                 const quantityValue = btn.parentNode.querySelector('.quantity-value');
//                 let value = parseInt(quantityValue.value);
//                 if (value > 1) {
//                     quantityValue.value = value - 1;
//                 }
//             });
//         });

//         btnPlus.forEach(btn => {
//             btn.addEventListener('click', () => {
//                 const quantityValue = btn.parentNode.querySelector('.quantity-value');
//                 let value = parseInt(quantityValue.value);
//                 quantityValue.value = value + 1;
//             });
//         });



//     } else {
//         alert('Có lỗi xảy ra' + response.message);
//     }
// });

import * as module from './module.js';

let url_api_get_cart_infor = module.url_api_get_cart_infor;
let post_method = module.method_post;
let delete_method = module.method_delete;
let url_api_remove_product_from_cart = module.url_api_remove_product_from_cart;
let url_api_create_unpaid_orders = module.url_api_create_unpaid_orders;

let cart_product_content_container = document.querySelector("#cart_product_content_container");
let login_session_token = sessionStorage.getItem('tokek_for_login_session');

document.addEventListener('DOMContentLoaded', async () => {
    let data = {
        token_login_session: login_session_token
    };
    let response = await module.request_data_to_server({ url: url_api_get_cart_infor, data: data, method: post_method });
    if (response.status) {
        let cart_infors = response.message;
        let list_product_html = ``;

        for (let product_infor of cart_infors) {
            let price_string = module.formatNumber(parseInt(product_infor.price));
            let product_html = `
                <div class="cart__form" data-product-id="${product_infor.id_product}">
                    <div class="cart__content">
                        <a href="#"  >
                            <div class="cart__content-main">
                                <input type="checkbox" name="" class="cart__check">
                                <img src="${product_infor.image}" class="cart__content-img show_product_detail" alt="" data_id_product="${product_infor.id_product}">
                                <div class="cart__content-name"> ${product_infor.product_name}</div>
                            </div>
                        </a>
                        <div class="cart__content-price">${price_string} đ</div>
                        <div class="cart__quantity-input">
                            <button class="btn-minus">-</button>
                            <input type="text" class="quantity-value" value="${product_infor.quantity}" pattern="[0-9]*" inputmode="numeric">
                            <button class="btn-plus">+</button>
                        </div>
                        <div class="cart__content-delete">Xóa</div>
                    </div>
                </div>
            `;
            list_product_html += product_html;
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
                        <div class="cart__price-sum">0đ</div>
                    </div>
                    <a href="#" id="payment_btn"><div class="cart__cast-pay-btn btn">Đặt Hàng</div></a>
                </div>
            </div>
        `;
        cart_product_content_container.innerHTML = cart_content_html;

        const calculateTotalPrice = () => {
            let total_price = 0;
            document.querySelectorAll('.cart__content').forEach(content => {
                const checkbox = content.querySelector('.cart__check');
                if (checkbox.checked) {
                    const price = parseInt(content.querySelector('.cart__content-price').textContent.replace(/[^0-9]/g, ''));
                    const quantity = parseInt(content.querySelector('.quantity-value').value);
                    total_price += price * quantity;
                }
            });
            document.querySelector('.cart__price-sum').textContent = `${module.formatNumber(total_price)}đ`;
        };

        document.querySelectorAll('.show_product_detail').forEach(button => {
            button.addEventListener('click', function(event) {
                event.preventDefault();
                let productId = this.getAttribute('data_id_product');
                window.location.href = `${module.url_base_front_hosting}/preview.html?id=${productId}`;
            });
        });

        const masterCheckbox = document.getElementById('cart__check-all');
        const itemCheckboxes = document.querySelectorAll('.cart__check');

        if (masterCheckbox) {
            masterCheckbox.addEventListener('change', function() {
                itemCheckboxes.forEach(function(checkbox) {
                    checkbox.checked = masterCheckbox.checked;
                });
                calculateTotalPrice();
            });
        }

        itemCheckboxes.forEach(checkbox => {
            checkbox.addEventListener('change', calculateTotalPrice);
        });

        document.querySelectorAll('.btn-minus').forEach(btn => {
            btn.addEventListener('click', () => {
                const quantityValue = btn.parentNode.querySelector('.quantity-value');
                let value = parseInt(quantityValue.value);
                if (value > 1) {
                    quantityValue.value = value - 1;
                    calculateTotalPrice();
                }
            });
        });

        document.querySelectorAll('.btn-plus').forEach(btn => {
            btn.addEventListener('click', () => {
                const quantityValue = btn.parentNode.querySelector('.quantity-value');
                let value = parseInt(quantityValue.value);
                quantityValue.value = value + 1;
                calculateTotalPrice();
            });
        });

        document.querySelectorAll('.cart__content-delete').forEach(button => {
            button.addEventListener('click', async () => {
                let result = confirm('Bạn có chắc chắn muốn xóa sản phẩm này khỏi giỏ hàng?');
                if (result) {
                    const productElement = button.closest('.cart__form');
                    const productId = productElement.getAttribute('data-product-id');
                    let data = {
                        token_login_session: login_session_token,
                        product_id: productId
                    };
                    let response = await module.request_data_to_server({ url: url_api_remove_product_from_cart, data: data, method: delete_method });
                    if (!response.status) {
                        alert('Xóa sản phẩm thất bại: ' + response.message);
                    } else {
                        alert(response.message);
                        productElement.remove();
                        calculateTotalPrice();
                    }
                }
            });
        });

        document.getElementById('payment_btn').addEventListener('click', async (event) => {
            event.preventDefault();
            let selectedProducts = [];
            document.querySelectorAll('.cart__content').forEach(content => {
                const checkbox = content.querySelector('.cart__check');
                if (checkbox.checked) {
                    const productId = content.closest('.cart__form').getAttribute('data-product-id');
                    const quantity = parseInt(content.querySelector('.quantity-value').value);
                    const product_price = parseInt(content.querySelector('.cart__content-price').textContent.replace(/[^0-9]/g, ''));
                    selectedProducts.push({ product_id: productId, qty: quantity, order_price: product_price });
                }
            });

            if (selectedProducts.length === 0) {
                alert('Vui lòng chọn ít nhất một sản phẩm để đặt hàng.');
                return;
            }else{
                let data = {
                    token_login_session: login_session_token,
                    list_order_items: selectedProducts
                };
                let response = await module.request_data_to_server({ url: url_api_create_unpaid_orders, data: data, method: post_method });
                if (response.status) {
                    window.location.href = `${module.url_base_front_hosting}/order.html?id=${response.message}`;
                } else {
                    alert(response.message);
                }
            }

            
        });
    } else {
        alert('Có lỗi xảy ra: ' + response.message);
    }
});


