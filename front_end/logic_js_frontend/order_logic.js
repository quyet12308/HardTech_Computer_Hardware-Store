// import * as module from './module.js';


// let post_method = module.method_post;
// let delete_method = module.method_delete;

// let url_api_get_order_detail_preview = module.url_api_get_order_detail_preview

// let login_session_token = sessionStorage.getItem('tokek_for_login_session');
// let order_id = module.getQueryParameter('id')
// let order_products_content = document.querySelector("#order_products_content")
// let order_customer_info_content = document.querySelector("#order_customer_info_content")

// document.addEventListener('DOMContentLoaded', async () => {
//     let data = {
//         token_login_session: login_session_token,
//         order_id:  order_id
//     };
//     let response = await module.request_data_to_server({ url: url_api_get_order_detail_preview, data: data, method: post_method });
//     if (response.status) {
//         let order_infors = response.message
//         let order_details = order_infors.order_details
//         let products_content_htmls = ``
//         for (let product_infor of order_details){
//             let product_content_html = `
//                 <div class="cart__form">
//                     <div class="cart__content">
//                         <div class="cart__content-main">
//                             <img src="${product_infor.product_image}" class="cart__content-img" alt="">
//                             <div class="cart__content-name"> ${product_infor.product_name}</div>
//                         </div>
//                             <div class="order_quantity"> ${product_infor.qty} </div>
//                             <div class="cart__content-price"> ${product_infor.order_price} đ</div>
//                     </div> 
//                 </div>
//             `
//             products_content_htmls = products_content_htmls + product_content_html
//         }
        
//         let order_products_content_html = `
//             <p class="order_title">thông tin Sản phẩm</p>
//                     <div class="order__category">
//                         <div class="order__category-name">Sản phẩm</div>
//                         <div class="order__category-price">Số lượng</div>
//                         <div class="order__category-ticket">Giá</div>
//                     </div>
                
//                 ${products_content_htmls}
//         `
//         let order_user_content_html = `
//             <p class="order_title">thông tin khách hàng</p>
//                 <form id="order_information">
//                     <div class="form-group">
//                         <input type="text" id="username" class="form-control" placeholder="" required>
//                         <label for="name-input" class="form-label">Họ và Tên*</label>

//                     </div>
//                     <div class="form_group-1">
//                         <div class="form-group">
//                             <input type="text" id="number" class="form-control" pattern="[0-9]*" inputmode="numeric" placeholder="" required>
//                             <label for="name-input" class="form-label">Số Điện Thoại*</label>

//                         </div>
//                         <div class="form-group">
//                             <input type="text" id="username" class="form-control" placeholder="" required>
//                             <label for="name-input" class="form-label">Email</label>
//                         </div>
//                     </div>
//                     <div class="form-group">
//                         <input type="text" id="text" class="form-control" placeholder="" required>
//                         <label for="name-input" class="form-label">Địa Chỉ*</label>
//                     </div>
//                     <div class="form-group">
//                         <input type="text" id="username" class="form-control" placeholder="" required>
//                         <label for="name-input" class="form-label">Tỉnh/Thành Phố</label>
//                     </div>
//                     <div class="form-group">
//                         <input type="text" id="text" class="form-control" placeholder="" required>
//                         <label for="name-input" class="form-label">Quận/Huyện</label>
//                     </div>
//                     <div class="form-group">
//                         <input type="text" id="text" class="form-control" placeholder="" required>
//                         <label for="name-input" class="form-label">Xã/phường</label>
//                     </div>
//                     <div class="form-group">
//                         <input type="text" id="text" class="form-control" placeholder="" required>
//                         <label for="name-input" class="form-label">Ghi chú</label>
//                     </div>
//                 </form>
//         `
//     }
//     else{
//         alert(response.message)
//     }
// });

// import * as module from './module.js';

//         let post_method = module.method_post;
//         let delete_method = module.method_delete;

//         let url_api_get_order_detail_preview = module.url_api_get_order_detail_preview;

//         let login_session_token = sessionStorage.getItem('tokek_for_login_session');
//         let order_id = module.getQueryParameter('id');
//         let order_products_content = document.querySelector("#order_products_content");
//         let order_customer_info_content = document.querySelector("#order_customer_info_content");

//         document.addEventListener('DOMContentLoaded', async () => {
//             let data = {
//                 token_login_session: login_session_token,
//                 order_id: order_id
//             };
//             let response = await module.request_data_to_server({ url: url_api_get_order_detail_preview, data: data, method: post_method });
//             if (response.status) {
//                 let order_infors = response.message;
//                 let order_details = order_infors.order_details;
//                 let user_info = order_infors.user; // Assuming backend sends user info

//                 let products_content_htmls = order_details.map(product_infor => `
//                     <div class="cart__form">
//                         <div class="cart__content">
//                             <div class="cart__content-main">
//                                 <img src="${product_infor.product_image}" class="cart__content-img" alt="">
//                                 <div class="cart__content-name">${product_infor.product_name}</div>
//                             </div>
//                             <div class="order_quantity">${product_infor.qty}</div>
//                             <div class="cart__content-price">${product_infor.order_price} đ</div>
//                         </div> 
//                     </div>
//                 `).join('');

//                 let order_products_content_html = `
//                     <p class="order_title">Thông tin Sản phẩm</p>
//                     <div class="order__category">
//                         <div class="order__category-name">Sản phẩm</div>
//                         <div class="order__category-price">Số lượng</div>
//                         <div class="order__category-ticket">Giá</div>
//                     </div>
//                     ${products_content_htmls}
//                 `;

//                 let order_user_content_html = `
//                     <p class="order_title">Thông tin khách hàng</p>
//                     <form id="order_information">
//                         <div class="form-group">
//                             <input type="text" id="username" class="form-control" value="${user_info.fullname}" placeholder="Họ và Tên" required>
//                             <label for="username" class="form-label">Họ và Tên*</label>
//                         </div>
//                         <div class="form_group-1">
//                             <div class="form-group">
//                                 <input type="text" id="phone" class="form-control" value="${user_info.phone_number}" pattern="[0-9]*" inputmode="numeric" placeholder="Số Điện Thoại" required>
//                                 <label for="phone" class="form-label">Số Điện Thoại*</label>
//                             </div>
//                             <div class="form-group">
//                                 <input type="email" id="email" class="form-control" value="${user_info.email}" placeholder="Email" required disabled>
//                                 <label for="email" class="form-label">Email</label>
//                             </div>
//                         </div>
//                         <div class="form-group">
//                             <input type="text" id="address" class="form-control" value="${user_info.address}" placeholder="Địa Chỉ" required>
//                             <label for="address" class="form-label">Địa Chỉ*</label>
//                         </div>
//                         <div class="form-group css_select_div">
//                             <select class="css_select" id="province" name="province" title="Chọn Tỉnh Thành">
//                                 <option value="${user_info.province_id}">${user_info.province_name}</option>
//                             </select> 
//                             <select class="css_select" id="district" name="district" title="Chọn Quận Huyện">
//                                 <option value="${user_info.district_id}">${user_info.district_name}</option>
//                             </select> 
//                             <select class="css_select" id="ward" name="ward" title="Chọn Phường Xã">
//                                 <option value="${user_info.ward_id}">${user_info.ward_name}</option>
//                             </select>
//                         </div>
//                         <div class="form-group">
//                             <input type="text" id="note" class="form-control" value="${user_info.note}" placeholder="Ghi chú">
//                             <label for="note" class="form-label">Ghi chú</label>
//                         </div>
//                     </form>
//                 `;

//                 order_products_content.innerHTML = order_products_content_html;
//                 order_customer_info_content.innerHTML = order_user_content_html;

//                 // Fetch provinces
                
//             } else {
//                 alert(response.message);
//             }
//         });


// import * as module from './module.js';

// let post_method = module.method_post;
// let delete_method = module.method_delete;

// let url_api_get_order_detail_preview = module.url_api_get_order_detail_preview;

// let login_session_token = sessionStorage.getItem('tokek_for_login_session');
// let order_id = module.getQueryParameter('id');
// let order_products_content = document.querySelector("#order_products_content");
// let order_customer_info_content = document.querySelector("#order_customer_info_content");

// document.addEventListener('DOMContentLoaded', async () => {
//     let data = {
//         token_login_session: login_session_token,
//         order_id: order_id
//     };
//     let response = await module.request_data_to_server({ url: url_api_get_order_detail_preview, data: data, method: post_method });
//     if (response.status) {
//         let order_infors = response.message;
//         let order_details = order_infors.order_details;
//         let user_info = order_infors.user;

//         let products_content_htmls = order_details.map(product_infor => `
//             <div class="cart__form">
//                 <div class="cart__content">
//                     <div class="cart__content-main">
//                         <img src="${product_infor.product_image}" class="cart__content-img" alt="">
//                         <div class="cart__content-name">${product_infor.product_name}</div>
//                     </div>
//                     <div class="order_quantity">${product_infor.qty}</div>
//                     <div class="cart__content-price">${module.formatNumber(parseInt(product_infor.order_price) * parseInt(product_infor.qty))} đ</div>
//                 </div> 
//             </div>
//         `).join('');

//         let order_products_content_html = `
//             <p class="order_title">Thông tin Sản phẩm</p>
//             <div class="order__category">
//                 <div class="order__category-name">Sản phẩm</div>
//                 <div class="order__category-price">Số lượng</div>
//                 <div class="order__category-ticket">Giá</div>
//             </div>
//             ${products_content_htmls}
//         `;

//         let user_address = module.decodeAddress(user_info.address);
//         let default_province_address = user_address ? `<option value="${user_address.province}" selected disabled>${user_address.province}</option>` : `<option value="" selected disabled>Chọn tỉnh/thành phố</option>`;
//         let default_dstrict_address = user_address ? `<option value="${user_address.dstrict}" selected disabled>${user_address.dstrict}</option>` : `<option value="" selected disabled>Chọn quận/huyện</option>`;
//         let default_ward_address = user_address ? `<option value="${user_address.ward}" selected disabled>${user_address.ward}</option>` : `<option value="" selected disabled>Chọn xã/phường</option>`;
//         let default_local_address = user_address ? user_address.local : '';

//         let order_user_content_html = `
//             <p class="order_title">Thông tin khách hàng</p>
//             <form id="order_information">
//                 <div class="form-group">
//                     <input type="text" id="username" class="form-control" value="${user_info.fullname}" placeholder="Họ và Tên" required>
//                     <label for="username" class="form-label">Họ và Tên*</label>
//                 </div>
//                 <div class="form_group-1">
//                     <div class="form-group">
//                         <input type="text" id="phone" class="form-control" value="${user_info.phone_number}" pattern="[0-9]*" inputmode="numeric" placeholder="Số Điện Thoại" required>
//                         <label for="phone" class="form-label">Số Điện Thoại*</label>
//                     </div>
//                     <div class="form-group">
//                         <input type="email" id="email" class="form-control" value="${user_info.email}" placeholder="Email" required disabled>
//                         <label for="email" class="form-label">Email</label>
//                     </div>
//                 </div>
//                 <div class="form-group">
//                     <input type="text" id="address" class="form-control" value="${default_local_address}" placeholder="Địa Chỉ" required>
//                     <label for="address" class="form-label">Địa Chỉ*</label>
//                 </div>
//                 <div class="form-group css_select_div">
//                     <select class="css_select" id="province" name="province" title="Chọn Tỉnh Thành">${default_province_address}</select>
//                     <select class="css_select" id="district" name="district" title="Chọn Quận Huyện">${default_dstrict_address}</select>
//                     <select class="css_select" id="ward" name="ward" title="Chọn Phường Xã">${default_ward_address}</select>
//                 </div>
//                 <div class="form-group">
//                     <input type="text" id="note" class="form-control" value="" placeholder="Ghi chú">
//                     <label for="note" class="form-label">Ghi chú</label>
//                 </div>
//             </form>
//         `;

//         order_products_content.innerHTML = order_products_content_html;
//         order_customer_info_content.innerHTML = order_user_content_html;

//         let list_provinces = await module.get_province_list();

//         let province_select = document.querySelector("#province");
//         list_provinces.forEach(tinh => {
//             const option = document.createElement("option");
//             option.value = tinh.name;
//             option.textContent = tinh.name;
//             option.setAttribute('data-id', tinh.id);
//             province_select.appendChild(option);
//         });

//         let district_select = document.querySelector("#district");
//         province_select.addEventListener('change', async () => {
//             district_select.innerHTML = `<option value="" selected disabled>Chọn quận/huyện</option>`;
//             ward_select.innerHTML = `<option value="" selected disabled>Chọn xã/phường</option>`;
//             let selectedOption = province_select.options[province_select.selectedIndex];
//             let id_tinh = selectedOption.getAttribute('data-id');
//             let list_dstricts = await module.get_dstrict_list(id_tinh);
//             list_dstricts.forEach(huyen => {
//                 const option = document.createElement("option");
//                 option.value = huyen.name;
//                 option.textContent = huyen.name;
//                 option.setAttribute('data-id', huyen.id);
//                 district_select.appendChild(option);
//             });
//         });

//         let ward_select = document.querySelector("#ward");
//         district_select.addEventListener("change", async () => {
//             ward_select.innerHTML = `<option value="" selected disabled>Chọn xã/phường</option>`;
//             let selectedOption = district_select.options[district_select.selectedIndex];
//             let id_huyen = selectedOption.getAttribute('data-id');
//             let list_wards = await module.get_ward_list(id_huyen);
//             list_wards.forEach(xa => {
//                 const option = document.createElement("option");
//                 option.value = xa.name;
//                 option.textContent = xa.name;
//                 option.setAttribute('data-id', xa.id);
//                 ward_select.appendChild(option);
//             });
//         });
//         let order_payment_method_html = `
//             <p class="order_title">phương thức thanh toán</p>
//                 <div class="payment-options">
//                     <div class="option">
//                       <input type="radio" id="momo_payment" name="payment-method" value="option1">
//                       <label for="option1">Thanh toán bằng Momo
//                         <img src="./images/momo.png" alt="">
//                       </label>
//                     </div>
//                     <div class="option">
//                       <input type="radio" id="vnpay_payment" name="payment-method" value="option2">
//                       <label for="option2">Thanh toán bằng VNpay
//                         <img src="./images/icon-payment-vnpay.png" alt="">
//                       </label>
//                     </div>
//                     <div class="option">
//                       <input type="radio" id="stripe_payment" name="payment-method" value="option3">
//                       <label for="option3">Thanh toán bằng Stripe
//                         <img src="./images/stripe.jpg" alt="">
//                       </label>
//                     </div>
//                     <div class="option">
//                       <input type="radio" id="paypal_payment" name="payment-method" value="option3">
//                       <label for="option3">Thanh toán bằng Paypal
//                         <img src="./images/PayPal_Logo_2007.png" alt="">
//                       </label>
//                     </div>
//                     <div class="option">
//                       <input type="radio" id="zalopay_payment" name="payment-method" value="option3">
//                       <label for="option3">Thanh toán bằng Zalopay
//                         <img src="./images/zalopay.png" alt="">
//                       </label>
//                     </div>
//                   </div>
//         `
//         let order_price_html = `
//             <p class="order_title">tổng tiền thanh toán</p>
//                 <div class="order_total-price">
//                     <p class="order_total-price-title">Tổng cộng: </p>
//                     <div class="total_price">18.900.000đ</div>
//                 </div>
//         `
//         let order_btn_html = `
//             <div class="btn">thanh toán</div>
//         `
//         let order_payment_method = document.querySelector("#order_payment_method")
//         let order_price = document.querySelector("#order_price")
//         let order_button = document.querySelector("#order_button")

//         order_payment_method.innerHTML = order_payment_method_html
//         order_price.innerHTML = order_price_html
//         order_button.innerHTML = order_btn_html


//     } else {
//         alert(response.message);
//     }
// });

import * as module from './module.js';

let post_method = module.method_post;
let delete_method = module.method_delete;

let url_api_get_order_detail_preview = module.url_api_get_order_detail_preview;
let url_api_create_url_for_payment = module.url_api_create_url_for_payment;

let login_session_token = sessionStorage.getItem('tokek_for_login_session');
let order_id = module.getQueryParameter('id');
let order_products_content = document.querySelector("#order_products_content");
let order_customer_info_content = document.querySelector("#order_customer_info_content");
let order_payment_method_content = document.querySelector("#order_payment_method");
let order_price_content = document.querySelector("#order_price");
let order_button_content = document.querySelector("#order_button");

document.addEventListener('DOMContentLoaded', async () => {
    let data = {
        token_login_session: login_session_token,
        order_id: order_id
    };
    let response = await module.request_data_to_server({ url: url_api_get_order_detail_preview, data: data, method: post_method });
    if (response.status) {
        let order_infors = response.message;
        let order_details = order_infors.order_details;
        let user_info = order_infors.user;

        let total_price = order_details.reduce((sum, product_infor) => {
            return sum + (parseInt(product_infor.order_price) * parseInt(product_infor.qty));
        }, 0);

        let products_content_htmls = order_details.map(product_infor => `
            <div class="cart__form">
                <div class="cart__content">
                    <div class="cart__content-main">
                        <img src="${product_infor.product_image}" class="cart__content-img" alt="">
                        <div class="cart__content-name">${product_infor.product_name}</div>
                    </div>
                    <div class="order_quantity">${product_infor.qty}</div>
                    <div class="cart__content-price">${module.formatNumber(parseInt(product_infor.order_price) * parseInt(product_infor.qty))} đ</div>
                </div> 
            </div>
        `).join('');

        let order_products_content_html = `
            <p class="order_title">Thông tin Sản phẩm</p>
            <div class="order__category">
                <div class="order__category-name">Sản phẩm</div>
                <div class="order__category-price">Số lượng</div>
                <div class="order__category-ticket">Giá</div>
            </div>
            ${products_content_htmls}
        `;

        let user_address = module.decodeAddress(user_info.address);
        let default_province_address = user_address ? `<option value="${user_address.province}" selected disabled>${user_address.province}</option>` : `<option value="" selected disabled>Chọn tỉnh/thành phố</option>`;
        let default_dstrict_address = user_address ? `<option value="${user_address.dstrict}" selected disabled>${user_address.dstrict}</option>` : `<option value="" selected disabled>Chọn quận/huyện</option>`;
        let default_ward_address = user_address ? `<option value="${user_address.ward}" selected disabled>${user_address.ward}</option>` : `<option value="" selected disabled>Chọn xã/phường</option>`;
        let default_local_address = user_address ? user_address.local : '';

        let order_user_content_html = `
            <p class="order_title">Thông tin khách hàng</p>
            <form id="order_information">
                <div class="form-group">
                    <input type="text" id="username" class="form-control" value="${user_info.fullname}" placeholder="Họ và Tên" required>
                    <label for="username" class="form-label">Họ và Tên*</label>
                </div>
                <div class="form_group-1">
                    <div class="form-group">
                        <input type="text" id="phone" class="form-control" value="${user_info.phone_number}" pattern="[0-9]*" inputmode="numeric" placeholder="Số Điện Thoại" required>
                        <label for="phone" class="form-label">Số Điện Thoại*</label>
                    </div>
                    <div class="form-group">
                        <input type="email" id="email" class="form-control" value="${user_info.email}" placeholder="Email" required disabled>
                        <label for="email" class="form-label">Email</label>
                    </div>
                </div>
                <div class="form-group">
                    <input type="text" id="address" class="form-control" value="${default_local_address}" placeholder="Địa Chỉ" required>
                    <label for="address" class="form-label">Địa Chỉ*</label>
                </div>
                <div class="form-group css_select_div">
                    <select class="css_select" id="province" name="province" title="Chọn Tỉnh Thành">${default_province_address}</select>
                    <select class="css_select" id="district" name="district" title="Chọn Quận Huyện">${default_dstrict_address}</select>
                    <select class="css_select" id="ward" name="ward" title="Chọn Phường Xã">${default_ward_address}</select>
                </div>
                <div class="form-group">
                    <input type="text" id="note" class="form-control" value="" placeholder="Ghi chú">
                    <label for="note" class="form-label">Ghi chú</label>
                </div>
            </form>
        `;

        let order_payment_method_html = `
            <p class="order_title">Phương thức thanh toán</p>
            <div class="payment-options">
                <div class="option">
                    <input type="radio" id="momo_payment" name="payment-method" value="momo">
                    <label for="momo_payment">Thanh toán bằng Momo
                        <img src="./images/momo.png" alt="">
                    </label>
                </div>
                <div class="option">
                    <input type="radio" id="vnpay_payment" name="payment-method" value="vnpay">
                    <label for="vnpay_payment">Thanh toán bằng VNpay
                        <img src="./images/icon-payment-vnpay.png" alt="">
                    </label>
                </div>
                <div class="option">
                    <input type="radio" id="stripe_payment" name="payment-method" value="stripe">
                    <label for="stripe_payment">Thanh toán bằng Stripe
                        <img src="./images/stripe.jpg" alt="">
                    </label>
                </div>
                <div class="option">
                    <input type="radio" id="paypal_payment" name="payment-method" value="paypal">
                    <label for="paypal_payment">Thanh toán bằng Paypal
                        <img src="./images/PayPal_Logo_2007.png" alt="">
                    </label>
                </div>
                <div class="option">
                    <input type="radio" id="9pay_payment" name="payment-method" value="9pay">
                    <label for="paypal_payment">Thanh toán bằng 9pay
                        <img src="./images/PayPal_Logo_2007.png" alt="">
                    </label>
                </div>
                <div class="option">
                    <input type="radio" id="zalopay_payment" name="payment-method" value="zalopay">
                    <label for="zalopay_payment">Thanh toán bằng Zalopay
                        <img src="./images/zalopay.png" alt="">
                    </label>
                </div>
            </div>
        `;

        let order_price_html = `
            <p class="order_title">Tổng tiền thanh toán</p>
            <div class="order_total-price">
                <p class="order_total-price-title">Tổng cộng: </p>
                <div class="total_price">${module.formatNumber(total_price)} đ</div>
            </div>
        `;

        let order_btn_html = `
            <button class="btn" id="submit_order">Thanh toán</button>
        `;

        order_products_content.innerHTML = order_products_content_html;
        order_customer_info_content.innerHTML = order_user_content_html;
        order_payment_method_content.innerHTML = order_payment_method_html;
        order_price_content.innerHTML = order_price_html;
        order_button_content.innerHTML = order_btn_html;

        // Fetch provinces and handle change events
        let list_provinces = await module.get_province_list();

        let province_select = document.querySelector("#province");
        list_provinces.forEach(tinh => {
            const option = document.createElement("option");
            option.value = tinh.name;
            option.textContent = tinh.name;
            option.setAttribute('data-id', tinh.id);
            province_select.appendChild(option);
        });

        let district_select = document.querySelector("#district");
        province_select.addEventListener('change', async () => {
            district_select.innerHTML = `<option value="" selected disabled>Chọn quận/huyện</option>`;
            ward_select.innerHTML = `<option value="" selected disabled>Chọn xã/phường</option>`;
            let selectedOption = province_select.options[province_select.selectedIndex];
            let id_tinh = selectedOption.getAttribute('data-id');
            let list_dstricts = await module.get_dstrict_list(id_tinh);
            list_dstricts.forEach(huyen => {
                const option = document.createElement("option");
                option.value = huyen.name;
                option.textContent = huyen.name;
                option.setAttribute('data-id', huyen.id);
                district_select.appendChild(option);
            });
        });

        let ward_select = document.querySelector("#ward");
        district_select.addEventListener("change", async () => {
            ward_select.innerHTML = `<option value="" selected disabled>Chọn xã/phường</option>`;
            let selectedOption = district_select.options[district_select.selectedIndex];
            let id_huyen = selectedOption.getAttribute('data-id');
            let list_wards = await module.get_ward_list(id_huyen);
            list_wards.forEach(xa => {
                const option = document.createElement("option");
                option.value = xa.name;
                option.textContent = xa.name;
                option.setAttribute('data-id', xa.id);
                ward_select.appendChild(option);
            });
        });

        // Handle order submission
        document.querySelector("#submit_order").addEventListener("click", async () => {
            let payment_method = document.querySelector('input[name="payment-method"]:checked');
            if (!payment_method) {
                alert("Vui lòng chọn phương thức thanh toán.");
                return;
            }

            let username = document.querySelector("#username").value;
            let phone = document.querySelector("#phone").value;
            let address = document.querySelector("#address").value;
            let province = document.querySelector("#province").value;
            let district = document.querySelector("#district").value;
            let ward = document.querySelector("#ward").value;
            let note = document.querySelector("#note").value || "Không ghi chú";

            // let redirecturl = module.redirecturl
            // if (payment_method.value == "stripe"){
            //     redirecturl = `${redirecturl}?status=1&order_id=${order_id}`
            // }

            let order_data = {
                user_name: username,
                phone_number: phone,
                order_id: order_id,
                address: module.combineAddress({soNha:address, xa:ward, huyen:district, tinh:province}),
                note: note,
                payment_method: payment_method.value,
                redirecturl: module.redirecturl,
                token_login_session: login_session_token
            };
            console.log(order_data)

            let order_response = await module.request_data_to_server({ url: url_api_create_url_for_payment, data: order_data, method: post_method });
            if (order_response.status) {
                console.log(order_response)
                let url_payment = order_response.message
                console.log(url_payment)
                console.log(typeof url_payment)
                sessionStorage.setItem("payment_method",payment_method.value)
                // alert(order_response.message)
                window.location.href = `${url_payment}`
                // alert("Đơn hàng đã được tạo thành công!");
                // Redirect or perform further actions
            } else {
                alert("Thanh toán thất bại do lỗi: " + order_response.message);
            }
        });
    } else {
        alert(response.message);
    }
});
