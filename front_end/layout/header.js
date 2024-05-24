document.addEventListener('DOMContentLoaded',  function() {
    let header = document.querySelector('.header');
  header.innerHTML = `
  <div class="headertop_desc">
      <div class="call">
           <p><span>Need help?</span> call us <a href="tel:+1234567890">123-456-7890</a>
           </span></p>
      </div>
      <div class="account_desc">
          <ul>
          <li><a href="../delivery.html">Delivery</a></li>
          <li><a href="#">Checkout</a></li>
          <li><a href="../register.html">Register</a></li>
          <li><a href="../login.html">Login</a></li>
          <li class="header__navbar-user"><a href="../user_info.html">
          <img src="../images/about_img.jpg" alt="">	My Account
          </a>
              <ul class="header__navbar-user-menu hover-animation">
                  <li class="header__navbar-user-item">
                      <a href="../user_info.html">Tài khoản của tôi</a>
                  <li class="header__navbar-user-item header__navbar-user-item--separate">
                      <a href="">Đăng xuất</a>
                  </li>
          </ul>
      </div>
      <div class="clear"></div>
  </div>
  <div class="header_top">
      <!-- header log -->
      <div class="logo">
          <a href="../index.html">
              <div class="logo_text">hard<span>tech</span> </div>
          </a>
      </div>
      <!-- header search -->
      <div class="search_box">
          <form>
              <input type="text" value="Tìm kiếm sản phẩm" onfocus="this.value = '';" onblur="if (this.value == '') {this.value = 'Search';}"><input type="submit" value="">
          </form>
      </div>
      <!-- header cart -->
        <!-- <div class="cart">
                <a href="../cart.html"><i class="fa-solid fa-cart-shopping"></i></a>
        </div> -->
        <div class="header__cart">
          <div class="header__cart-wrap">
              <a href="../cart.html"><i class="header__cart-icon fa-solid fa-cart-shopping"></i></a>
              <span class="header__cart-notice">3</span>
              <!-- No cart: header__cart-list-no-cart  -->
              <div class="header__cart-list hover-animation">
                  <img src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/9bdd8040b334d31946f49e36beaf32db.png" alt="" class="header__cart-list-no-cart-img">
                  <span class="header__cart-list-no-cart-msg">Chưa có sản phẩm</span>
              
                  <!-- have item in cart -->
                  <h4 class="header__cart-heading">Sản phẩm mới thêm</h4>
                  <ul class="header__cart-list-item">
                      <!-- cart item -->
                      <li class="header__cart-item">
                          <img src="../images/CPU AMD Ryzen 9 5950X.jpg" alt="" class="header__cart-img">
                          <div class="header__cart-item-info">
                              <div class="header__cart-item-head">
                                  <h5 class="header__cart-item-name">CPU AMD Ryzen 9 5950X 
                                  </h5>
                                  <div class="header__cart-item-price-wrap">
                                      <span class="header__cart-item-price">8.700.000đ</span>
                                      <span class="header__cart-item-multiply">x</span>
                                      <span class="header__cart-item-quantity">1</span>
                                  </div>
                              </div>
                              <div class="header__cart-item-body">
                                  <span class="header__cart-item-description">
                                      16 Nhân / 32 Luồng | 3.4GHz Boost 4.9GHz
                                  </span>
                                  <span class="header__cart-item-remove">Xóa</span>
                              </div>
                          </div>
                      </li>
                      <li class="header__cart-item">
                          <img src="../images/Gigabyte RTX 4070 AORUS MASTER.jpg" alt="" class="header__cart-img">
                          <div class="header__cart-item-info">
                              <div class="header__cart-item-head">
                                  <h5 class="header__cart-item-name">Gigabyte RTX 4070 AORUS MASTER  </h5>
                                  <div class="header__cart-item-price-wrap">
                                      <span class="header__cart-item-price">18.890.000đ</span>
                                      <span class="header__cart-item-multiply">x</span>
                                      <span class="header__cart-item-quantity">1</span>
                                  </div>
                              </div>
                              <div class="header__cart-item-body">
                                  <span class="header__cart-item-description">
                                      VGA NEW 100% Full Box bảo hành 3 năm  
                                  </span>
                                  <span class="header__cart-item-remove">Xóa</span>
                              </div>

                          </div>
                      </li>
                      <li class="header__cart-item">
                          <img src="../images/Mainboard Asus TUF Gaming.png" alt="" class="header__cart-img">
                          <div class="header__cart-item-info">
                              <div class="header__cart-item-head">
                                  <h5 class="header__cart-item-name">MMainboard Asus TUF Gaming B760M-E DDR4   </h5>
                                  <div class="header__cart-item-price-wrap">
                                      <span class="header__cart-item-price">3.390.000đ</span>
                                      <span class="header__cart-item-multiply">x</span>
                                      <span class="header__cart-item-quantity">5</span>
                                  </div>
                              </div>
                              <div class="header__cart-item-body">
                                  <span class="header__cart-item-description">
                                      Socket: LGA1700 | Chipset: B760 | Kích thước: Micro ATX  
                                  </span>
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
                <li><a href="../index.html" class="nav-link">Home</a></li>
                <li><a href="../about.html" class="nav-link">About</a></li>
                <li><a href="../delivery.html" class="nav-link">Delivery</a></li>
                <li><a href="../news.html" class="nav-link">News</a></li>
                <li><a href="../contact.html" class="nav-link">Contact</a></li>
            <div class="clear"></div>
            </ul>
        </div>
   
       <div class="clear"></div>
   </div>	  
`
})

