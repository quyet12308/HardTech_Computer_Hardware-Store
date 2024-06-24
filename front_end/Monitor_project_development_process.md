# Tổng quát
- File này được tạo ra để ghi lại quá trình phát triển dự án (các thay đổi , các lỗi tìm thấy , các phương án khắc phục, rút kinh nghiệm ...vv)
- Nó rất hữu ích để sau này có bảo trì hay nâng cấp dự án hoặc đơn giản hơn là xem lại , bàn giao cho người mới thì họ sẽ nắm bắt nhanh hơn
## Ngày 6/6/2024
- nó bị lỗi ở chọn admin homepage , chỉ chọn được 1 lần đến lần thứ 2 thì không chọn được nữa . Nhưng hiện tại không còn time nữa => có thể bàn giao lại cho Lâm fix hoặc khi đã xong hết mọi thứ rồi quay lại fix sau

## Ngày 7/6/2024
- bị vướng khá lâu lỗi giữa globel và local . Cụ thể đây là phần giải thích của gpt-4 
```cmd
Vấn đề bạn gặp phải là các hàm editProduct và deleteProduct được định nghĩa bên trong hàm xử lý sự kiện DOMContentLoaded, do đó chúng không có phạm vi toàn cục và không thể được truy cập từ các sự kiện onclick được đặt trực tiếp trong HTML.
```
- 2 hướng khắc phục là:
    ```cmd
    function displayProducts(filteredProducts) {
        const productTable = document.getElementById('productTable');
        productTable.innerHTML = '';

        filteredProducts.forEach((product, index) => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${index + 1}</td>
                <td>${product.product_name}</td>
                <td>${product.brand_name}</td>
                <td>${product.category_name}</td>
                <td>${product.quantity}</td>
                <td>${product.discount_percentage}</td>
                <td>${product.price.toLocaleString('vi-VN', { style: 'currency', currency: 'VND' })}</td>
                <td>
                    <button class="button edit-button" data-id="${index + 1}">Sửa</button>
                    <button class="button delete-button" data-id="${index + 1}">Xóa</button>
                </td>
            `;
            productTable.appendChild(row);
        });

        // Thêm sự kiện cho các nút sau khi chúng được tạo
        document.querySelectorAll('.edit-button').forEach(button => {
            button.addEventListener('click', function() {
                editProduct({ id_product: this.getAttribute('data-id') });
            });
        });

        document.querySelectorAll('.delete-button').forEach(button => {
            button.addEventListener('click', function() {
                deleteProduct({ id_product: this.getAttribute('data-id') });
            });
        });
    }
    ```


    ```cmd
    // Định nghĩa các hàm ở phạm vi toàn cục
    function editProduct({ id_product }) {
        alert(`Chỉnh sửa sản phẩm với id: ${id_product}`);
        // Thêm chức năng chỉnh sửa sản phẩm tại đây
    }

    function deleteProduct({ id_product }) {
        alert(`Xóa sản phẩm với id: ${id_product}`);
        // Thêm chức năng xóa sản phẩm tại đây
    }

    document.addEventListener('DOMContentLoaded', async function () {
        // ... mã khác của bạn ở đây ...

        function displayProducts(filteredProducts) {
            const productTable = document.getElementById('productTable');
            productTable.innerHTML = '';

            filteredProducts.forEach((product, index) => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${index + 1}</td>
                    <td>${product.product_name}</td>
                    <td>${product.brand_name}</td>
                    <td>${product.category_name}</td>
                    <td>${product.quantity}</td>
                    <td>${product.discount_percentage}</td>
                    <td>${product.price.toLocaleString('vi-VN', { style: 'currency', currency: 'VND' })}</td>
                    <td>
                        <button class="button" onclick="editProduct({ id_product: '${index + 1}' })">Sửa</button>
                        <button class="button" onclick="deleteProduct({ id_product: '${index + 1}' })">Xóa</button>
                    </td>
                `;
                productTable.appendChild(row);
            });
        }

        // ... mã khác của bạn ở đây ...

        populateFilters();
        displayProducts(products);
    });
    ```
- bị vướng thêm ở cái vụ edit brand , nó khi ấn không điền các thông tin đã có vào form 

## Ngày 9/6/2024
- tạm bỏ qua phần edit product để làm phần user trước đẻ kịp mai kiểm tra
- chưa làm được phần quản lý order

## Ngày 10/6/2024
- tính làm phần vụ ...

## Ngày 13/6/2024
- hình như nó bị lỗi , nếu là ngời dùng mới chưa có giỏ hàng thì sẽ không thể ấn mua ngay được , mà phải ấn trước thêm vào giỏ hàng => để fix sau

## ngày 14/6/2024 
- nó bị lỗi khi sửa user thì cần phải sửa ảnh ko là bị lỗi => đã fix được , hóa ra là bị lỗi cái chỗ khác biệt giữa base64 và file . tức là nếu là file thì nó có thể chuyển qua base64 nhưng nếu là base64 thì ko được . và cả chỗ chọn file nữa

## Ngày 21/6/2024 
- éo hiểu sao lúc dữ liệu truyền từ backend sang front-end lại phải gọi 2 lần message làm tốn mất mấy lần test trên zalopay (khi nào rảnh check lại nó ở file order.js cái chỗ chyển hướng đến url payment)
- check cẩn thận trạng thái của giao dịch vì nó có thể hủy chứ ko được khi chuyển hướng về trang của mình là mặc định thành công vd url sau là hủy 
    ```cmd
    http://127.0.0.1:5500/in_bill.html?amount=13980000&appid=2553&apptransid=240621_11&bankcode=&checksum=63f4b8f943d4f8aebcc60da77295a8887d2ccb56e549662c61bd444c8dff3293&discountamount=0&pmcid=0&status=-49
    ```
- Cái hcaptcha éo hiểu sao nó lại chặn future gì đó , nên hiện tại sẽ tạm bỏ qua nó => lúc nào rảnh fix lại sau

- Cái brand chưa phích được trong cái search

## Ngày 24/6/2024
- cái captcha hiện tại chỉ có giao diện => để bao giờ rảnh thì làm thêm
