// import * as module from './module.js';

// let url_api_preview_product_detail = module.url_api_preview_product_detail
// let url_api_add_product_to_cart = module.url_api_add_product_to_cart
// let post_method = module.method_post

// let product_id = module.getQueryParameter('id');

// let content_product_detail = document.querySelector("#content_product_detail")

// document.addEventListener('DOMContentLoaded', async  ()=> {
//     let data = {
        
//         product_id:product_id
//       }
//       let response_data = await module.request_data_to_server({url:url_api_preview_product_detail,data:data,method:post_method})
//         if (response_data.status){
//             let detail_product = response_data.message
//             let price = parseFloat(detail_product.price)

//             let discount_percentage = parseFloat(detail_product.discount_percentage)/100;
//             if (isNaN(discount_percentage)) {
//             discount_percentage = 0;
//             }

//           let content_html_detail_product = `
//             <div class="section group">
// 				<div class="cont-desc ">
// 				  <div class="product-details">				
// 					<div class="grid images_3_of_2">
// 						<div id="container">
// 						<div id="products_example">
// 							<div id="products">
// 							  <div class="slides_container">
// 								<div class="slide">
// 								  <img src="${detail_product.image}" alt=" " />
// 								</div>
								
// 							  </div>
							  
// 							</div>
// 						  </div>
// 					</div>
// 				</div>
// 				<div class="desc span_3_of_2">
// 					<h2>${detail_product.product_name}</h2>
// 					<div class="basic_product-info">
// 						<div class="item_basic">Mã Sản Phẩm:
// 							<div class="product_ID">${detail_product.product_id}</div>
// 						</div>
// 						<div class="item_basic">Đánh giá:
// 								<div class="review-stars">
// 									<i class="fa-solid fa-star"></i>
// 									<i class="fa-solid fa-star"></i>
// 									<i class="fa-solid fa-star"></i>
// 									<i class="fa-solid fa-star"></i>
// 									<i class="fa-solid fa-star"></i>
// 								  </div>
// 						</div>
// 					</div>
// 					<div class="price">
// 						<p>Giá:</p>
// 						<div class="discounted_price">${ price - (price * discount_percentage)} đ</div>
// 						<div class="original_price">${price} đ</div>
// 						<div class="discounted_amount">Tiết kiệm ${price * discount_percentage }đ</div>
// 					</div>
// 					<div class="available">
// 						<p>Số lượng :</p>
// 						<div class="cart__quantity-input">
// 							<button class="btn-minus">-</button>
// 							<input type="text" class="quantity-value" value="1" pattern="[0-9]*" inputmode="numeric">
// 							<button class="btn-plus">+</button>
// 						</div>
// 						<div class="available_quantity">
// 							<span> ${detail_product.quantity} </span>sản phẩm có sẵn
// 						</div>
// 					</div>
// 					<div class="pay_button">
// 						<div class="add_cart-btn" id="add_to_cart_btn" data-id>
// 							<a href="#">
// 								<i class="fa-solid fa-cart-plus"></i>
// 								Thêm vào giỏ hàng
// 							</a>
// 						</div>					
// 						<div class="buy_now-btn">
// 							<a href="./cart.html">
// 								Mua ngay
// 							</a>
// 						</div>					
// 						<div class="clear"></div>
// 					</div>
// 					<div class="product_policy">
// 						<p>Yên tâm mua hàng</p>
// 						<div class="group_1-row">
// 							<div class="product_policy-detail">
// 								<i class="fa-solid fa-wallet"></i>
// 								<p>Cam kết giá tốt trên thị trường</p>
// 							</div>
// 							<div class="product_policy-detail">
// 								<i class="fa-solid fa-copyright"></i>
// 								<p>Sản phẩm mới 100%</p>
// 							</div>
// 						</div>
// 						<div class="group_2-row">
// 							<div class="product_policy-detail">
// 								<i class="fa-solid fa-right-left"></i>
// 								<p>Lỗi 1 đổi 1 ngay lập tức</p>
// 							</div>
// 							<div class="product_policy-detail">
// 								<i class="fa-solid fa-handshake-angle"></i>
// 								<p>Hỗ trợ thanh toán - Thủ tục nhanh gọn</p>
// 							</div>
// 						</div>
// 					</div>
// 			</div>
// 			<div class="clear"></div>
// 		  </div>
// 				<div class="resp-tabs-container">
// 					<div class="product_desc">
// 						<p>Mô tả sản phẩm</p>
// 						<p>${detail_product.description}</p>
// 					</div>	

// 				<div class="review">
// 					<h4>Đánh giá sản phẩm được viết bởi<a href="#">Nguyễn Tùng lâm</a></h4>
					 
// 					 <p>tạm ổn</p>
// 				  <div class="your-review">
// 				  	 <h3>How Do You Rate This Product?</h3>
// 				  	  <p>Write Your Own Review?</p>
// 				  	  <form>
// 					    	<div>
// 						    	<span><label>Nickname<span class="red">*</span></label></span>
// 						    	<span><input type="text" value=""></span>
// 						    </div>
// 						    <div><span><label>Summary of Your Review<span class="red">*</span></label></span>
// 						    	<span><input type="text" value=""></span>
// 						    </div>						
// 						    <div>
// 						    	<span><label>Review<span class="red">*</span></label></span>
// 						    	<span><textarea> </textarea></span>
// 						    </div>
// 						   <div>
// 						   		<span><input type="submit" value="SUBMIT REVIEW"></span>
// 						  </div>
// 					    </form>
// 				  	 </div>				
// 				</div>
// 		 </div>
//           `
//           content_product_detail.innerHTML = content_html_detail_product


          
//         }
//         else{
//           alert(response_data.message)
//         }
  
// });


import * as module from './module.js';

let url_api_preview_product_detail = module.url_api_preview_product_detail;
let url_api_add_product_to_cart = module.url_api_add_product_to_cart;
let post_method = module.method_post;

let product_id = module.getQueryParameter('id');
let login_session_token =  sessionStorage.getItem('tokek_for_login_session')

let content_product_detail = document.querySelector("#content_product_detail");

document.addEventListener('DOMContentLoaded', async () => {
    let data = {
        product_id: product_id
    };
    let response_data = await module.request_data_to_server({ url: url_api_preview_product_detail, data: data, method: post_method });
    if (response_data.status) {
        let detail_product = response_data.message;
        let price = parseFloat(detail_product.price);

        let discount_percentage = parseFloat(detail_product.discount_percentage) / 100;
        if (isNaN(discount_percentage)) {
            discount_percentage = 0;
        }

        let content_html_detail_product = `
            <div class="section group">
                <div class="cont-desc ">
                    <div class="product-details">				
                        <div class="grid images_3_of_2">
                            <div id="container">
                            <div id="products_example">
                                <div id="products">
                                  <div class="slides_container">
                                    <div class="slide">
                                      <img src="${detail_product.image}" alt=" " />
                                    </div>
                                  </div>
                                </div>
                              </div>
                        </div>
                    </div>
                    <div class="desc span_3_of_2">
                        <h2>${detail_product.product_name}</h2>
                        <div class="basic_product-info">
                            <div class="item_basic">Mã Sản Phẩm:
                                <div class="product_ID">${detail_product.product_id}</div>
                            </div>
                            <div class="item_basic">Đánh giá:
                                    <div class="review-stars">
                                        <i class="fa-solid fa-star"></i>
                                        <i class="fa-solid fa-star"></i>
                                        <i class="fa-solid fa-star"></i>
                                        <i class="fa-solid fa-star"></i>
                                        <i class="fa-solid fa-star"></i>
                                      </div>
                            </div>
                        </div>
                        <div class="price">
                            <p>Giá:</p>
                            <div class="discounted_price">${ price - (price * discount_percentage)} đ</div>
                            <div class="original_price">${price} đ</div>
                            <div class="discounted_amount">Tiết kiệm ${price * discount_percentage }đ</div>
                        </div>
                        <div class="available">
                            <p>Số lượng :</p>
                            <div class="cart__quantity-input">
                                <button class="btn-minus">-</button>
                                <input type="text" class="quantity-value" value="1" pattern="[0-9]*" inputmode="numeric">
                                <button class="btn-plus">+</button>
                            </div>
                            <div class="available_quantity">
                                <span> ${detail_product.quantity} </span>sản phẩm có sẵn
                            </div>
                        </div>
                        <div class="pay_button">
                            <div class="add_cart-btn" id="add_to_cart_btn">
                                <a href="#">
                                    <i class="fa-solid fa-cart-plus"></i>
                                    Thêm vào giỏ hàng
                                </a>
                            </div>					
                            <div class="buy_now-btn">
                                <a href="./cart.html">
                                    Mua ngay
                                </a>
                            </div>					
                            <div class="clear"></div>
                        </div>
                        <div class="product_policy">
                            <p>Yên tâm mua hàng</p>
                            <div class="group_1-row">
                                <div class="product_policy-detail">
                                    <i class="fa-solid fa-wallet"></i>
                                    <p>Cam kết giá tốt trên thị trường</p>
                                </div>
                                <div class="product_policy-detail">
                                    <i class="fa-solid fa-copyright"></i>
                                    <p>Sản phẩm mới 100%</p>
                                </div>
                            </div>
                            <div class="group_2-row">
                                <div class="product_policy-detail">
                                    <i class="fa-solid fa-right-left"></i>
                                    <p>Lỗi 1 đổi 1 ngay lập tức</p>
                                </div>
                                <div class="product_policy-detail">
                                    <i class="fa-solid fa-handshake-angle"></i>
                                    <p>Hỗ trợ thanh toán - Thủ tục nhanh gọn</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="clear"></div>
                  </div>
                    <div class="resp-tabs-container">
                        <div class="product_desc">
                            <p>Mô tả sản phẩm</p>
                            <p>${detail_product.description}</p>
                        </div>	
                    <div class="review">
                        <h4>Đánh giá sản phẩm được viết bởi<a href="#">Nguyễn Tùng lâm</a></h4>
                         <p>tạm ổn</p>
                      <div class="your-review">
                         <h3>How Do You Rate This Product?</h3>
                          <p>Write Your Own Review?</p>
                          <form>
                                <div>
                                    <span><label>Nickname<span class="red">*</span></label></span>
                                    <span><input type="text" value=""></span>
                                </div>
                                <div><span><label>Summary of Your Review<span class="red">*</span></label></span>
                                    <span><input type="text" value=""></span>
                                </div>						
                                <div>
                                    <span><label>Review<span class="red">*</span></label></span>
                                    <span><textarea> </textarea></span>
                                </div>
                               <div>
                                    <span><input type="submit" value="SUBMIT REVIEW"></span>
                              </div>
                            </form>
                         </div>				
                    </div>
             </div>
          `;
        content_product_detail.innerHTML = content_html_detail_product;

        // Thêm sự kiện click cho nút Thêm vào giỏ hàng
        document.getElementById('add_to_cart_btn').addEventListener('click', function (event) {
            event.preventDefault();
            let quantity = parseInt(document.querySelector('.quantity-value').value);
            addProductToCart(quantity, product_id);
        });

    } else {
        alert(response_data.message);
    }
});

async function addProductToCart(quantity, product_id) {
    let data = {
        quantity: quantity,
        product_id: product_id,
        token_login_session: login_session_token
    };
    console.log(data)
    let response = await module.request_data_to_server({ url: url_api_add_product_to_cart, data: data, method: post_method });
    if (response.status) {
        alert('Sản phẩm đã được thêm vào giỏ hàng thành công!');
    } else {
        alert('Có lỗi xảy ra khi thêm sản phẩm vào giỏ hàng: ' + response.message);
    }
}
