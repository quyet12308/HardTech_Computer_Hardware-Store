import * as module from './admin_module.js';

let token_admin = sessionStorage.getItem("is_admin")
let login_session_token =  sessionStorage.getItem('tokek_for_login_session')

// Lấy id_product từ URL
let brand_id = module.getQueryParameter('brand_id');

document.addEventListener('DOMContentLoaded', async function () {

    let container = document.querySelector("#container")
    module.check_is_admin_logined()
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
            <p>Hình Ảnh</p>
                    <img id="brandImage" src="${response_data.message.img}" alt="Brand Image">
                    <input type="file" id="imageInput" accept="image/*" style="display: none;">
                    <button type="button" onclick="document.getElementById('imageInput').click()">Change Image</button>
            <p>Tên Hãng Sản Xuất</p>

                    <input type="text" id="brandName" placeholder="Brand Name" value="${response_data.message.brand_name}">
            <p>Mô Tả</p>

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
