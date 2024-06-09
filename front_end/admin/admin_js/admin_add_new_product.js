import * as module from './admin_module.js';

let token_admin = sessionStorage.getItem("is_admin")
let login_session_token =  sessionStorage.getItem('tokek_for_login_session')

let url_api_product_management_add_new_product = module.url_api_product_management_add_new_product
let url_api_product_management_get_brands_and_catagories = module.url_api_product_management_get_brands_and_catagories
let post_method = module.method_post

document.addEventListener('DOMContentLoaded', async function () {
    if (token_admin === null) {
        alert("Bạn chưa đăng nhập. Vui lòng đăng nhập để tiếp tục.");
        window.location.href = "http://127.0.0.1:5500/login.html"; // Chuyển hướng tới trang đăng nhập
      } else if (token_admin === "false") {
          // Kiểm tra nếu token_admin là false (lưu ý là giá trị trong sessionStorage là chuỗi)
          alert("Bạn không đủ quyền truy cập trang này.");
          window.location.href = "http://127.0.0.1:5500/index.html"; // Chuyển hướng tới trang home
      } else if (token_admin === "true") {
    
      }
      else {
          // Trường hợp không mong muốn, có thể xử lý thêm nếu cần
          console.error("Giá trị không hợp lệ trong sessionStorage: is_admin");
      }
      
      let response_data = await module.get_data_from_server(url_api_product_management_get_brands_and_catagories)
        if (response_data.status) {
            let brands_and_catagories = response_data.message;
            let brands = brands_and_catagories.brands;
            let categories = brands_and_catagories.categories;
            
            let brands_html = `<option value="" disabled selected>Chọn hãng sản xuất</option>`;
            let categories_html = `<option value="" disabled selected>Chọn thể loại</option>`;
            
            // Dùng for...of thay vì for...in
            for (let brand of brands) {
                let brand_html = `<option value="${brand.id}">${brand.name}</option>`;
                brands_html = brands_html + brand_html;
            }
            
            for (let category of categories) {
                let category_html = `<option value="${category.id}">${category.name}</option>`;
                categories_html = categories_html + category_html;
            }
            
            document.querySelector("#productBrand").innerHTML = brands_html;
            document.querySelector("#productCategory").innerHTML = categories_html;
        } else {
            alert(response_data.message);
        }


    
      
    // Thêm sự kiện 'change' cho phần tử input
    const productImageInput = document.getElementById('productImage');
    productImageInput.addEventListener('change', previewImage);
});


function previewImage(event) {
    const file = event.target.files[0];
    const previewContainer = document.getElementById('imagePreview');
    previewContainer.innerHTML = '';

    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            img.style.maxWidth = '200px';
            img.style.maxHeight = '200px';
            previewContainer.appendChild(img);
        };
        reader.readAsDataURL(file);
    }
}

document.getElementById('discountPercentage').addEventListener('input', function() {
    const discountPercentage = document.getElementById('discountPercentage').value;
    const startDateInput = document.getElementById('discountStartDate');
    const endDateInput = document.getElementById('discountEndDate');

    if (discountPercentage > 0) {
        startDateInput.disabled = false;
        endDateInput.disabled = false;
    } else {
        startDateInput.disabled = true;
        endDateInput.disabled = true;
        startDateInput.value = '';
        endDateInput.value = '';
    }
});

document.getElementById('discountPercentage').addEventListener('input', function() {
    const discountPercentage = parseFloat(this.value);
    const discountDates = document.getElementById('discountDates');
    if (discountPercentage > 0) {
        discountDates.style.display = 'block';
    } else {
        discountDates.style.display = 'none';
    }
});

document.getElementById('productForm').addEventListener('submit', async (event) =>{
    event.preventDefault();

    const errorMessages = [];
    const productImage = document.getElementById('productImage').files[0];
    const productName = document.getElementById('productName').value.trim();
    const productPrice = parseFloat(document.getElementById('productPrice').value);
    const productDescription = document.getElementById('productDescription').value.trim();
    const productQuantity = parseInt(document.getElementById('productQuantity').value);
    const discountPercentage = parseFloat(document.getElementById('discountPercentage').value);
    const discountStartDate = document.getElementById('discountStartDate').value;
    const discountEndDate = document.getElementById('discountEndDate').value;
    const brand_id = document.getElementById('productBrand').value;
    const category_id = document.getElementById('productCategory').value;

    // Kiểm tra ảnh
    if (!productImage) {
        errorMessages.push('Vui lòng chọn ảnh sản phẩm.');
    }

    // Kiểm tra tên sản phẩm
    if (productName.length < 10 || productName.length > 100) {
        errorMessages.push('Tên sản phẩm phải có từ 10 đến 100 ký tự.');
    }

    // Kiểm tra giá sản phẩm
    if (isNaN(productPrice) || productPrice <= 0) {
        errorMessages.push('Giá sản phẩm phải là số dương lớn hơn 0.');
    }

    // Kiểm tra mô tả sản phẩm
    if (productDescription.length < 30 || productDescription.length > 1000) {
        errorMessages.push('Mô tả sản phẩm phải có từ 30 đến 1000 ký tự.');
    }

    // Kiểm tra số lượng sản phẩm
    if (isNaN(productQuantity) || productQuantity <= 0) {
        errorMessages.push('Số lượng nhập về phải là số dương khác 0.');
    }

    // Kiểm tra ngày giảm giá (nếu có)
    if (discountPercentage > 0) {
        const startDate = new Date(discountStartDate);
        const endDate = new Date(discountEndDate);
        const now = new Date();

        if (isNaN(startDate) || isNaN(endDate)) {
            errorMessages.push('Ngày bắt đầu và kết thúc giảm giá phải là ngày hợp lệ.');
        } else {
            if (startDate <= now) {
                errorMessages.push('Ngày bắt đầu giảm giá phải là ngày trong tương lai.');
            }
            if (endDate <= startDate) {
                errorMessages.push('Ngày kết thúc giảm giá phải sau ngày bắt đầu.');
            }
            if ((endDate - startDate) / (1000 * 60 * 60 * 24) < 1 || (endDate - startDate) / (1000 * 60 * 60 * 24) > 365) {
                errorMessages.push('Thời gian giảm giá phải từ 1 ngày đến 1 năm.');
            }
        }
    }

    // Hiển thị thông báo lỗi
    const errorContainer = document.getElementById('errorMessages');
    errorContainer.innerHTML = '';
    if (errorMessages.length > 0) {
        errorMessages.forEach(message => {
            const div = document.createElement('div');
            div.textContent = message;
            errorContainer.appendChild(div);
        });
        return;
    }

    // Chuyển ảnh sang base64
    
    let imageFile = document.getElementById('productImage').files[0];
    let base64img = await module.convertToBase64(imageFile)

    let data = {
        token_login_session: login_session_token,
        image: base64img,
        product_name: productName,
        description: productDescription,
        price: productPrice,
        quantity: productQuantity,
        category_id: parseInt(category_id), // Đảm bảo kiểu int
        brand_id: parseInt(brand_id),       // Đảm bảo kiểu int
        discount_percentage: discountPercentage > 0 ? discountPercentage : null,
        discount_startdate: discountPercentage > 0 ? discountStartDate : null,
        discount_enddate: discountPercentage > 0 ? discountEndDate : null,
    };
    console.log(data)
    let response_data = await module.request_data_to_server({url:url_api_product_management_add_new_product,data:data,method:post_method})
    if (response_data.status){
      alert(response_data.message)
      location.reload()
    }
    else{
      alert(response_data.message)
    }

  location.reload()
    reader.readAsDataURL(productImage);
});


