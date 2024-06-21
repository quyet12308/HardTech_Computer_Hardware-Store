document.addEventListener('DOMContentLoaded',  function() {

let navBar = document.querySelector('.navbar');
navBar.innerHTML = `
    <a href="./admin_hompage.html">Trang Chủ</a>
    <a href="./admin_product_management_preview.html">Quản Lý Sản Phẩm</a>
    <a href="./admin_add_new_product.html">Thêm Mới Sản Phẩm</a>
    <a href="./admin_brands_management.html">Quản Lý Hãng Sản Xuất</a>
    <a href="./admin_categories_management.html">Quản Lý Thể Loại</a>
  `
})