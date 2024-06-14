// import * as module from './module.js';


// let post_method = module.method_post;
// let delete_method = module.method_delete;

// let url_api_get_show_user_infor = module.url_api_get_show_user_infor


// let login_session_token = sessionStorage.getItem('tokek_for_login_session');

// let user_infor_container = document.querySelector("#user_infor_container");

// document.addEventListener('DOMContentLoaded', async () => {
//     let data = {
//         token_login_session:login_session_token
//     }
//     let response = await module.request_data_to_server({ url: url_api_get_show_user_infor, data: data, method: post_method });
//     if (response.status) {
//         let user_info = response.message.user_infor
//         let user_comments = response.message.user_comments
//         let user_infor_htmls = `
//             <div class="user_main-info">
//                     <div class="user_group">
//                         <span>Tên đăng nhập</span>
//                         <input type="text" class="user_input" id="user_account-name-text" ></input>
//                     </div>
//                     <div class="user_group">
//                         <span>Tên người dùng</span>
//                         <input type="text" class="user_input" id="user_name-text"></input>
//                     </div>
//                     <div class="user_group">
//                         <span>Email</span>
//                         <input type="text" class="user_input" id="user_email-text"></input>
//                     </div>
//                     <div class="user_group">
//                         <span>Số điện thoại</span>
//                         <input type="text" class="user_input" id="user_phone-text"></input>
//                     </div>
//                     <div class="user_group">
//                         <span>địa chỉ</span>
//                         <input type="text" class="user_input" id="user_address-text"></input>
//                     </div>
//                     <button class="save_user-btn">Lưu</button>
//                 </div>
//                 <div class="user_main-img" >
//                     <p>Ảnh đại diện</p>
//                     <input type="file" id="image-input" accept="image/*" style="display: none;">
//                     <div id="image-container">
//                         <img id="preview-image" src="./images/thumbnailslide-1.jpg" alt="Preview Image" style="width: 100%; height: 100%; object-fit: cover;">
//                     </div>
//                     <button id="choose_image-btn">Chọn ảnh</button>
//                 </div>
//         `
//     }
//     else{
//         alert(response.message)
//     }

// });


// import * as module from './module.js';

// let post_method = module.method_post;
// let delete_method = module.method_delete;

// let url_api_get_show_user_infor = module.url_api_get_show_user_infor;
// // let url_api_update_user_infor = module.url_api_update_user_infor;

// let login_session_token = sessionStorage.getItem('tokek_for_login_session');

// let user_infor_container = document.querySelector("#user_infor_container");

// document.addEventListener('DOMContentLoaded', async () => {
//     let data = {
//         token_login_session: login_session_token
//     };
//     console.log(data)

//     let response = await module.request_data_to_server({ url: url_api_get_show_user_infor, data: data, method: post_method });

//     if (response.status) {
//         let user_info = response.message.user_infor;
//         let user_comments = response.message.user_comments
//         let user_infor_htmls = `
//             <div class="user_main-info">
//                 <div class="user_group">
//                     <span>Tên đăng nhập</span>
//                     <input type="text" class="user_input" id="user_account-name-text" value="${user_info.username}" ></input>
//                 </div>
//                 <div class="user_group">
//                     <span>Tên người dùng</span>
//                     <input type="text" class="user_input" id="user_name-text" value="${user_info.fullname}"></input>
//                 </div>
//                 <div class="user_group">
//                     <span>Email</span>
//                     <input type="text" class="user_input" id="user_email-text" value="${user_info.email}"></input>
//                 </div>
//                 <div class="user_group">
//                     <span>Số điện thoại</span>
//                     <input type="text" class="user_input" id="user_phone-text" value="${user_info.phone_number}"></input>
//                 </div>
//                 <div class="user_group">
//                     <span>Địa chỉ</span>
//                     <select id="province-select"></select>
//                     <select id="district-select"></select>
//                     <select id="ward-select"></select>
//                     <input type="text" class="user_input" id="user_address-text" value="${user_info.address}"></input>
//                 </div>
//                 <button class="save_user-btn">Lưu</button>
//             </div>
//             <div class="user_main-img">
//                 <p>Ảnh đại diện</p>
//                 <input type="file" id="image-input" accept="image/*" style="display: none;">
//                 <div id="image-container">
//                     <img id="preview-image" src="${user_info.avatar}" alt="Preview Image" style="width: 100%; height: 100%; object-fit: cover;">
//                 </div>
//                 <button id="choose_image-btn">Chọn ảnh</button>
//             </div>
//         `;
//         user_infor_container.innerHTML = user_infor_htmls;

        

//         // Xử lý sự kiện chọn ảnh
//         let chooseImageButton = document.querySelector("#choose_image-btn");
//         let imageInput = document.querySelector("#image-input");
//         let previewImage = document.querySelector("#preview-image");

//         chooseImageButton.addEventListener('click', () => {
//             imageInput.click();
//         });

//         imageInput.addEventListener('change', (event) => {
//             let file = event.target.files[0];
//             if (file) {
//                 let reader = new FileReader();
//                 reader.onload = function(e) {
//                     previewImage.src = e.target.result;
//                 };
//                 reader.readAsDataURL(file);
//             }
//         });

//         // Xử lý sự kiện lưu thông tin
//         let saveUserButton = document.querySelector(".save_user-btn");
//         saveUserButton.addEventListener('click', async () => {
//             let username = document.querySelector("#user_account-name-text").value;
//             let name = document.querySelector("#user_name-text").value;
//             let email = document.querySelector("#user_email-text").value;
//             let phone = document.querySelector("#user_phone-text").value;
//             let address = document.querySelector("#user_address-text").value;
//             let province = document.querySelector("#province-select").value;
//             let district = document.querySelector("#district-select").value;
//             let ward = document.querySelector("#ward-select").value;

//             // Kiểm tra tính hợp lệ của các trường nhập liệu
//             if (username.length < 5) {
//                 alert("Tên đăng nhập phải có ít nhất 5 ký tự");
//                 return;
//             }
//             if (name.length < 8) {
//                 alert("Tên người dùng phải có ít nhất 8 ký tự");
//                 return;
//             }
//             if (!validateEmail(email)) {
//                 alert("Email không đúng định dạng");
//                 return;
//             }
//             if (!validatePhone(phone)) {
//                 alert("Số điện thoại không đúng định dạng");
//                 return;
//             }

//             let updatedData = {
//                 username: username,
//                 name: name,
//                 email: email,
//                 phone: phone,
//                 address: address,
//                 province: province,
//                 district: district,
//                 ward: ward,
//                 token_login_session: login_session_token
//             };

//             let updateResponse = await module.request_data_to_server({ url: url_api_update_user_infor, data: updatedData, method: post_method });
//             if (updateResponse.status) {
//                 alert("Cập nhật thông tin thành công!");
//             } else {
//                 alert("Cập nhật thông tin thất bại: " + updateResponse.message);
//             }
//         });
//     } else {
//         alert(response.message);
//     }
// });

import * as module from './module.js';

let post_method = module.method_post;
let delete_method = module.method_delete;
let put_method = module.method_put

let url_api_get_show_user_infor = module.url_api_get_show_user_infor;
let url_api_edit_user_information = module.url_api_edit_user_information;

let login_session_token = sessionStorage.getItem('tokek_for_login_session');

let user_infor_container = document.querySelector("#user_infor_container");

document.addEventListener('DOMContentLoaded', async () => {
    let list_provinces =await module.get_province_list()
    // console.log(list_provinces)
    let data = {
        token_login_session: login_session_token
    };
    // console.log(data);

    let response = await module.request_data_to_server({ url: url_api_get_show_user_infor, data: data, method: post_method });

    if (response.status) {
        let user_info = response.message.user_infor;
        let user_comments = response.message.user_comments;
        let user_address = user_info.address
        
        let default_province_address = ``
        let default_dstrict_address = ``
        let default_ward_address = ``
        let default_local_address = ``
        if (user_address === "" ){
            
            default_province_address =  `<option value="" selected disabled> Chọn tỉnh/thành phố </option>`
            default_dstrict_address =  `<option value="" selected disabled> Chọn quận/huyện </option>`
            default_ward_address =  `<option value="" selected disabled> Chọn xã/phường </option>`
            default_local_address = ``
        }
        else {
            user_address = module.decodeAddress(user_address)
            default_province_address =  `<option value=" ${user_address.province}" selected disabled> ${user_address.province} </option>`
            default_dstrict_address =  `<option value="${user_address.dstrict}" selected disabled> ${user_address.dstrict} </option>`
            default_ward_address =  `<option value="${user_address.ward}" selected disabled> ${user_address.ward} </option>`
            default_local_address = `${user_address.local}`
        }
        let user_infor_htmls = `
            <div class="user_main-info">
                <div class="user_group">
                    <span>Tên đăng nhập</span>
                    <input type="text" class="user_input" id="user_account-name-text" value="${user_info.username}"></input>
                </div>
                <div class="user_group">
                    <span>Tên người dùng</span>
                    <input type="text" class="user_input" id="user_name-text" value="${user_info.fullname}"></input>
                </div>
                <div class="user_group">
                    <span>Email</span>
                    <input type="text" class="user_input" id="user_email-text" value="${user_info.email}" disabled></input>
                </div>
                <div class="user_group">
                    <span>Số điện thoại</span>
                    <input type="text" class="user_input" id="user_phone-text" value="${user_info.phone_number}"></input>
                </div>
                <div class="user_group">
                    <span>Địa chỉ</span>
                    <input type="text" class="user_input" id="user_address-text" placeholder="Số nhà, đường" value="${default_local_address}"> </input>
                    <select id="province-select"> ${default_province_address} </select>
                    <select  id="district-select"> ${default_dstrict_address} </select>
                    <select  id="ward-select"> ${default_ward_address}</select>
                </div>
                <button class="save_user-btn">Lưu</button>
            </div>
            <div class="user_main-img">
                <p>Ảnh đại diện</p>
                <input type="file" id="image-input" accept="image/*" style="display: none;">
                <div id="image-container">
                    <img id="preview-image" src="${user_info.img}" alt="Preview Image" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
                <button id="choose_image-btn">Chọn ảnh</button>
            </div>
        `;
        user_infor_container.innerHTML = user_infor_htmls;

        let province_select = document.querySelector("#province-select")
        list_provinces.forEach(tinh => {
            const option = document.createElement("option");
            option.value = tinh.name;
            option.textContent = tinh.name;
            option.setAttribute('data-id', tinh.id);
            province_select.appendChild(option);
        }); 

        let district_select = document.querySelector("#district-select")
        province_select.addEventListener('change', async () => {
            district_select.innerHTML = `<option value="" selected disabled> Chọn quận/huyện </option>`;
            ward_select.innerHTML = `<option value="" selected disabled> Chọn xã/phường </option>`;
            let selectedOption = province_select.options[province_select.selectedIndex];
            let id_tinh = selectedOption.getAttribute('data-id');
            // console.log(id_tinh)
            let list_dstricts = await module.get_dstrict_list(id_tinh);
            list_dstricts.forEach(huyen => {
                const option = document.createElement("option");
                option.value = huyen.name;
                option.textContent = huyen.name;
                option.setAttribute('data-id', huyen.id);
                district_select.appendChild(option);
            }); 
        })

        let ward_select = document.querySelector("#ward-select")
        district_select.addEventListener("change", async () => {
            ward_select.innerHTML = `<option value="" selected disabled> Chọn xã/phường </option>`;
            let selectedOption = district_select.options[district_select.selectedIndex];
            let id_huyen = selectedOption.getAttribute('data-id');
            // console.log(id_huyen)
            let list_wards = await module.get_ward_list(id_huyen);
            list_wards.forEach(xa => {
                const option = document.createElement("option");
                option.value = xa.name;
                option.textContent = xa.name;
                option.setAttribute('data-id', xa.id);
                ward_select.appendChild(option);
            }); 
        })
        

        // Xử lý sự kiện chọn ảnh
        let chooseImageButton = document.querySelector("#choose_image-btn");
        let imageInput = document.querySelector("#image-input");
        let previewImage = document.querySelector("#preview-image");

        chooseImageButton.addEventListener('click', () => {
            imageInput.click();
        });

        imageInput.addEventListener('change', (event) => {
            let file = event.target.files[0];
            if (file) {
                let reader = new FileReader();
                reader.onload = function(e) {
                    previewImage.src = e.target.result;
                };
                reader.readAsDataURL(file);
            }
        });

        

        // Xử lý sự kiện lưu thông tin
        let saveUserButton = document.querySelector(".save_user-btn");
        saveUserButton.addEventListener('click', async () => {
            let username = document.querySelector("#user_account-name-text").value;
            let fullname = document.querySelector("#user_name-text").value;
            let phone = document.querySelector("#user_phone-text").value;
            let local_address = document.querySelector("#user_address-text").value;
            let province = document.querySelector("#province-select").value;
            let district = document.querySelector("#district-select").value;
            let ward = document.querySelector("#ward-select").value;
            let image = document.getElementById('image-input');
            let preview_image = document.querySelector("#preview-image")
            let imageFile = document.getElementById('image-input').files[0];
            let base64img = ``

            let src_image = preview_image.src 
            if (module.isBase64Image(src_image)) {
                // console.log(src); // src đã là base64
                base64img = src_image

            } else {
                if (!imageFile) {
                    console.error('No file selected');
                    return;
                }
                try {
                    base64img = await module.convertToBase64(imageFile);
                    // console.log(base64img);
                } catch (error) {
                    console.error(error);
                }
            }


            // Kiểm tra tính hợp lệ của các trường nhập liệu
            if (username.length < 5) {
                alert("Tên đăng nhập phải có ít nhất 5 ký tự");
                return;
            }
            if (fullname.length < 8) {
                alert("Tên người dùng phải có ít nhất 8 ký tự");
                return;
            }
            if (!module.validatePhone(phone)) {
                alert("Số điện thoại không đúng định dạng");
                return;
            }
            if (local_address == ""){
                alert("Địa chỉ không được chống");
                return
            }
            if (province == ""){
                
                alert("Tỉnh/thành phố chưa được chọn")
                return
            }
            if (district == ""){
                alert("Huyện/quận chưa được chọn")
                return
            }
            if (ward == ""){
                alert("xã/phường chưa được chọn")
                return
            } 
            console.log(local_address)
            console.log(typeof local_address)
            console.log(province)
            console.log(district)
            console.log(ward)
            let updatedData = {
                username: username,
                fullname:fullname,
                image: base64img,
                phone_number: phone,
                address: module.encodeAddress({local:local_address,ward:ward,dstrict:district,province:province}),
                token_login_session: login_session_token
            };

            let updateResponse = await module.request_data_to_server({ url: url_api_edit_user_information, data: updatedData, method: put_method });
            if (updateResponse.status) {
                alert("Cập nhật thông tin thành công!");
            } else {
                alert("Cập nhật thông tin thất bại: " + updateResponse.message);
            }
        });
    } else {
        alert(response.message);
    }
});