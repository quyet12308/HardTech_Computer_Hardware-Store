import * as module from './admin_module.js';

let token_admin = sessionStorage.getItem("is_admin")
let login_session_token =  sessionStorage.getItem('tokek_for_login_session')

// Lấy id_product từ URL
let brand_id = module.getQueryParameter('brand_id');

document.addEventListener('DOMContentLoaded', async function () {

    let container = document.querySelector("#container")
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
    let url_api_product_management_get_brand_detail_admin_brand_management = module.url_api_product_management_get_brand_detail_admin_brand_management;
    let post_method = module.method_post
    let data = {
        token_login_session:login_session_token,
        brand_id: brand_id
    }
    let response_data = await module.request_data_to_server({url:url_api_product_management_get_brand_detail_admin_brand_management,data:data,method:post_method})
    if (response_data.status){
        container.innerHTML = `
            <form id="editBrandForm" enctype="multipart/form-data">
                    <img id="brandImage" src="${response_data.message.img}" alt="Brand Image">
                    <input type="file" id="imageInput" accept="image/*" style="display: none;">
                    <button type="button" onclick="document.getElementById('imageInput').click()">Change Image</button>
                    <input type="text" id="brandName" placeholder="Brand Name" value="${response_data.message.brand_name}">
                    <textarea id="brandDescription" placeholder="Brand Description">${response_data.message.description}</textarea>
                    <button type="submit">Submit</button>
                </form>
            `
    }

    
    
    document.getElementById('imageInput').addEventListener('change', function (event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                document.getElementById('brandImage').src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });
    
    document.getElementById('editBrandForm').addEventListener('submit', async function (event) {
        event.preventDefault();
        let url_api_product_management_edit_brand_admin_brand_management = module.url_api_product_management_edit_brand_admin_brand_management
        let put_method = module.method_put
        
        
        const fileInput = document.getElementById('imageInput');
        let img 
        if (fileInput.files[0]) {
            img = await module.convertToBase64(fileInput.files[0])
        }
        let data = {
            token_login_session:login_session_token,
            brand_id: brand_id,
            brand_name : document.getElementById('brandName').value,
            brand_img : img,
            brand_description : document.getElementById('brandDescription').value
        }
        let response_data = await module.request_data_to_server({url:url_api_product_management_edit_brand_admin_brand_management,data:data,method:put_method})
        if (response_data.status){
            alert(response_data.message)
            location.reload()
        }
        else{
            alert(response_data.message)
        }
    });
});
