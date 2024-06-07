url = 

function previewImage(event) {
    const reader = new FileReader();
    reader.onload = function() {
        const imagePreview = document.getElementById('imagePreview');
        imagePreview.innerHTML = '';
        const img = document.createElement('img');
        img.src = reader.result;
        img.style.maxWidth = '100%';
        img.style.maxHeight = '100%';
        imagePreview.appendChild(img);
    };
    reader.readAsDataURL(event.target.files[0]);
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

document.getElementById('productForm').addEventListener('submit', function(event) {
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
    const reader = new FileReader();
    reader.onload = function(event) {
        const imgBase64 = event.target.result;

        // Tạo đối tượng sản phẩm
        const productData = {
            tokek_for_login_session: sessionStorage.getItem("tokek_for_login_session"),
            img_base64: imgBase64,
            product_name: productName,
            product_description: productDescription,
            product_price: productPrice,
            product_quantity: productQuantity,
            discount_percentage: discountPercentage > 0 ? discountPercentage : null,
            discount_startdate: discountPercentage > 0 ? discountStartDate : null,
            discount_enddate: discountPercentage > 0 ? discountEndDate : null
        };

        // Chuyển đối tượng sản phẩm thành JSON
        const productJSON = JSON.stringify(productData);
        console.log(productJSON);

        // Gửi dữ liệu đến backend (ví dụ sử dụng fetch API)
        // fetch('/api/add_product', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: productJSON
        // }).then(response => response.json())
        // .then(data => {
        //     console.log('Success:', data);
        // }).catch(error => {
        //     console.error('Error:', error);
        // });
    };
    reader.readAsDataURL(productImage);
});


