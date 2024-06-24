import * as module from '../logic_js_frontend/module.js';

let url_api_search_products_by_keyword = module.url_api_search_products_by_keyword
let post_method = module.method_post;
let delete_method = module.method_delete;
let put_method = module.method_put

// let login_session_token = sessionStorage.getItem('tokek_for_login_session');


document.addEventListener('DOMContentLoaded', async function() {

    let header = document.querySelector('.header');
    header.innerHTML = `
    <div class="headertop_desc">
    <div class="call">
        <p><span>Cần giúp đỡ?</span> Gọi chúng tôi <a href="tel:+1234567890">123-456-7890</a></p>
    </div>
    <div class="account_desc" id="is_logined"></div>
    <div class="clear"></div>
    </div>
    <div class="header_top">
        <!-- header log -->
        <div class="logo">
            <a href="../index.html">
                <div class="logo_text">hard<span>tech</span></div>
            </a>
        </div>
        <!-- header search -->
        <div class="search_box">
            <form id="searchForm">
                <input type="text" id="searchInput" value="Tìm kiếm sản phẩm" onfocus="this.value = '';" onblur="if (this.value == '') {this.value = 'Search';}">
                <input type="submit" value="">
            </form>
        </div>
        <!-- header cart -->
        <div class="header__cart">
            <div class="header__cart-wrap">
                <a href="../cart.html"><i class="header__cart-icon fa-solid fa-cart-shopping"></i></a>
                <span class="header__cart-notice">3</span>
                <div class="header__cart-list hover-animation">
                    <img src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/9bdd8040b334d31946f49e36beaf32db.png" alt="" class="header__cart-list-no-cart-img">
                    <span class="header__cart-list-no-cart-msg">Chưa có sản phẩm</span>
                    <h4 class="header__cart-heading">Sản phẩm mới thêm</h4>
                    <ul class="header__cart-list-item">
                        <li class="header__cart-item">
                            <img src="../images/CPU AMD Ryzen 9 5950X.jpg" alt="" class="header__cart-img">
                            <div class="header__cart-item-info">
                                <div class="header__cart-item-head">
                                    <h5 class="header__cart-item-name">CPU AMD Ryzen 9 5950X</h5>
                                    <div class="header__cart-item-price-wrap">
                                        <span class="header__cart-item-price">8.700.000đ</span>
                                        <span class="header__cart-item-multiply">x</span>
                                        <span class="header__cart-item-quantity">1</span>
                                    </div>
                                </div>
                                <div class="header__cart-item-body">
                                    <span class="header__cart-item-description">16 Nhân / 32 Luồng | 3.4GHz Boost 4.9GHz</span>
                                    <span class="header__cart-item-remove">Xóa</span>
                                </div>
                            </div>
                        </li>
                        <li class="header__cart-item">
                            <img src="../images/Gigabyte RTX 4070 AORUS MASTER.jpg" alt="" class="header__cart-img">
                            <div class="header__cart-item-info">
                                <div class="header__cart-item-head">
                                    <h5 class="header__cart-item-name">Gigabyte RTX 4070 AORUS MASTER</h5>
                                    <div class="header__cart-item-price-wrap">
                                        <span class="header__cart-item-price">18.890.000đ</span>
                                        <span class="header__cart-item-multiply">x</span>
                                        <span class="header__cart-item-quantity">1</span>
                                    </div>
                                </div>
                                <div class="header__cart-item-body">
                                    <span class="header__cart-item-description">VGA NEW 100% Full Box bảo hành 3 năm</span>
                                    <span class="header__cart-item-remove">Xóa</span>
                                </div>
                            </div>
                        </li>
                        <li class="header__cart-item">
                            <img src="../images/Mainboard Asus TUF Gaming.png" alt="" class="header__cart-img">
                            <div class="header__cart-item-info">
                                <div class="header__cart-item-head">
                                    <h5 class="header__cart-item-name">Mainboard Asus TUF Gaming B760M-E DDR4</h5>
                                    <div class="header__cart-item-price-wrap">
                                        <span class="header__cart-item-price">3.390.000đ</span>
                                        <span class="header__cart-item-multiply">x</span>
                                        <span class="header__cart-item-quantity">5</span>
                                    </div>
                                </div>
                                <div class="header__cart-item-body">
                                    <span class="header__cart-item-description">Socket: LGA1700 | Chipset: B760 | Kích thước: Micro ATX</span>
                                    <span class="header__cart-item-remove">Xóa</span>
                                </div>
                            </div>
                        </li>
                    </ul>
                    <a href="../cart.html" class="header__cart-view-cart btn btn--primary">Xem giỏ hàng</a>
                </div>
            </div>
        </div>
        <div class="clear"></div>
    </div>
    <div class="header_bottom">
        <div class="menu">
            <ul>
                <li><a href="../index.html" class="nav-link">Trang chủ</a></li>
                <li><a href="../about.html" class="nav-link">giới thiệu</a></li>
                <li><a href="../delivery.html" class="nav-link">giao hàng</a></li>
                <li><a href="../news.html" class="nav-link">tin tức</a></li>
                <li><a href="../contact.html" class="nav-link">liên hệ</a></li>
                <div class="clear"></div>
            </ul>
        </div>
        <div class="clear"></div>
    </div>  
`

document.getElementById('searchForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    let searchValue = document.getElementById('searchInput').value;
    // let data = {
    //     keyword:searchValue
    // }
    // // console.log('Search Value:', searchValue);
    // // Here you can add code to send the searchValue to the backend
    // let response = await module.request_data_to_server({ url: url_api_search_products_by_keyword, data: data, method: post_method });

    // if (response.status) {

    // }
    window.location.href = `${module.url_base_front_hosting}/search_product.html?q=${searchValue}`
});
})

