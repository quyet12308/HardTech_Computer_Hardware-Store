import * as module from './admin_module.js';

let token_admin = sessionStorage.getItem("is_admin")
let login_session_token =  sessionStorage.getItem('tokek_for_login_session')

let  deleteManufacturer = async ({brand_id,brand_name}) => {
  if (confirm(`Bạn có chắc chắn muốn xóa hãng sản xuất ${brand_name} và tất cả các sản phẩm thuộc nhãn này không?`)) {
    let delete_method = module.method_delete
    let url_api_product_management_delete_brand_admin_brand_management = module.url_api_product_management_delete_brand_admin_brand_management

    let data = {
      token_login_session:login_session_token,
      brand_id:brand_id
    }
    let response_data = await module.request_data_to_server({url:url_api_product_management_delete_brand_admin_brand_management,data:data,method:delete_method})
      if (response_data.status){
        alert(response_data.message)
        location.reload()
      }
      else{
        alert(response_data.message)
      }

  }
}

let editManufacturer = ({brand_id})=> {
  window.location.href = `http://127.0.0.1:5500/admin/admin_edit_brand.html?brand_id=${brand_id}`;
}

document.getElementById('addManufacturerForm').addEventListener('submit', async function(event) {
  event.preventDefault(); // Ngăn chặn hành vi submit mặc định

  // Lấy các giá trị từ form
  let imageFile = document.getElementById('newImage').files[0];
  let name = document.getElementById('newName').value;
  let description = document.getElementById('newDescription').value;

  try {
      let base64Image = await module.convertToBase64(imageFile);
      let post_method = module.method_post
    
      let url_api_product_management_add_new_brand_admin_brand_management = module.url_api_product_management_add_new_brand_admin_brand_management;
      // Tạo object chứa dữ liệu
      let formData = {
          token_login_session:login_session_token,
          img: base64Image,
          brand_name: name,
          description: description
      };
      let response_data = await module.request_data_to_server({url:url_api_product_management_add_new_brand_admin_brand_management,data:formData,method:post_method})
      if (response_data.status){
        alert(response_data.message)
        location.reload()
      }
      else{
        alert(response_data.message)
      }
      
  } catch (error) {
      console.error('Error:', error);
      alert('Đã xảy ra lỗi khi xử lý hình ảnh.');
  }
});

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



  let url_api_product_management_get_all_brands_admin_brand_management = module.url_api_product_management_get_all_brands_admin_brand_management;

  let response_data = await module.get_data_from_server(url_api_product_management_get_all_brands_admin_brand_management)
  if (response_data.status){
    let manufacturers = response_data.message
    function renderTable() {
      const tbody = document.querySelector("#manufacturerTable tbody");
      tbody.innerHTML = "";
      manufacturers.forEach((manufacturer, index) => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td>${index + 1}</td>
          <td><img src="${manufacturer.img}" alt="${manufacturer.brand_name}" width="50"></td>
          <td>${manufacturer.brand_name}</td>
          <td>${manufacturer.description}</td>
          <td>
            <button id="editManufacturer" data-id="${manufacturer.brand_id}" >Sửa</button>
            <button id="deleteManufacturer" data-id="${manufacturer.brand_id}" data-name="${manufacturer.brand_name}">Xóa</button>
          </td>
        `;
        tbody.appendChild(tr);
        
      });
      
      document.querySelectorAll('#deleteManufacturer').forEach(button => {
          button.addEventListener('click', function() {
            deleteManufacturer({
                brand_id: this.getAttribute('data-id'),
                brand_name: this.getAttribute('data-name')
              });
          });
      });
      document.querySelectorAll('#editManufacturer').forEach(button => {
        button.addEventListener('click', function() {
          editManufacturer({
              brand_id: this.getAttribute('data-id')
            });
        });
    });
    }
    
    renderTable();
  }
  else{
    alert(response_data.message)
  }
  
});
