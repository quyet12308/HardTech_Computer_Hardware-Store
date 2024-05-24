const pages = [
  { name: 'Trang chủ', path: '/' },
  { name: 'Giỏ hàng', path: '/cart.html' },
  { name: 'Giới thiệu', path: '/about.html' },
  { name: 'Thông tin cá nhân', path: '/user_info' },
  { name: 'Giao hàng', path: '/delivery.html' },
  { name: 'Tin tức', path: '/news.html' },
  { name: 'Thông tin sản phẩm', path: '/preview.html' },
  { name: 'Liên hệ', path: '/contact.html' },
  { name: 'Danh sách sản phẩm mới', path: '/new_product.html' },
  { name: 'VGA - Card màn hình', path: '/category_products/vga_card.html' }
];

function updateBreadcrumb() {
  const breadcrumbElement = document.querySelector('.breadcrumb');
  const currentPath = window.location.pathname;

  const currentPage = pages.find(page => currentPath.startsWith(page.path));

  if (!currentPage) {
    breadcrumbElement.innerHTML = 'Trang chủ';
    return;
  }

  let breadcrumbHtml = '';
  for (let i = 0; i < pages.length; i++) {
    if (currentPath.startsWith(pages[i].path)) {
      breadcrumbHtml += `<a href="${pages[i].path}">${pages[i].name}</a>`;
      if (i !== pages.length - 1) {
        breadcrumbHtml += ' > ';
      }
    }
  }

  // Không hiển thị dấu > ở cuối chuỗi
  if (breadcrumbHtml.endsWith(' > ')) {
    breadcrumbHtml = breadcrumbHtml.slice(0, -3);
  }

  breadcrumbElement.innerHTML = breadcrumbHtml;
}

// gọi hàm khi trang web được tải
window.addEventListener('load', updateBreadcrumb);
// gọi hàm khi url thay đổi
window.addEventListener('popstate', updateBreadcrumb);

