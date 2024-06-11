// let cartIcon = document.querySelector('.header__cart-icon')

// cartIcon.addEventListener("click", () =>{
// 	window.location.href = "/cart.html";

// })





// Lấy tất cả các mục menu
const menuItems = document.querySelectorAll('.menu li');

// Lặp qua từng mục menu và thêm sự kiện click
menuItems.forEach(item => {
  item.addEventListener('click', () => {
    // Xóa class "active" từ tất cả các mục menu
    menuItems.forEach(i => i.classList.remove('active'));
    
    // Thêm class "active" vào mục menu được nhấp
    item.classList.add('active');
  });
});