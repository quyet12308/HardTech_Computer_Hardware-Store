import * as module from './admin_module.js';

let token_admin = sessionStorage.getItem("is_admin")
let login_session_token =  sessionStorage.getItem('tokek_for_login_session')

let url_api_product_management_get_all_categories_admin_brand_management = module.url_api_product_management_get_all_categories_admin_brand_management
let url_api_product_management_add_new_category_admin_brand_management = module.url_api_product_management_add_new_category_admin_brand_management
let url_api_product_management_edit_category_admin_brand_management = module.url_api_product_management_edit_category_admin_brand_management
let url_api_product_management_delete_category_admin_brand_management = module.url_api_product_management_delete_category_admin_brand_management
let url_api_product_management_get_a_category_admin_brand_management = module.url_api_product_management_get_a_category_admin_brand_management

let delete_method = module.method_delete
let put_method = module.method_put
let post_method = module.method_post

let currentCategoryId = null;

document.addEventListener('DOMContentLoaded', async function () {
  module.check_is_admin_logined()
  
  let response_data = await module.get_data_from_server(url_api_product_management_get_all_categories_admin_brand_management)
  if (response_data.status){
    let categories = response_data.message
    renderTable(categories)
  }
  else{
    alert(response_data.message)
  }

});


  
  function renderTable(categories) {
    const tbody = document.querySelector("#categoryTable tbody");
    tbody.innerHTML = "";
    categories.forEach((category, index) => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${index + 1}</td>
        <td>${category.category_name}</td>
        <td>${category.description}</td>
        <td>
          <button  id="editCategory" data-id="${category.category_id}" >Sửa</button>
          <button  id="deleteCategory" data-id="${category.category_id}" data-name="${category.category_name}">Xóa</button>
        </td>
      `;
      tbody.appendChild(tr);

    });
    document.querySelectorAll('#deleteCategory').forEach(button => {
      button.addEventListener('click', function() {
        deleteCategory({
          Category_id: this.getAttribute('data-id'),
          Category_name: this.getAttribute('data-name')
          });
      });
    });
    document.querySelectorAll('#editCategory').forEach(button => {
      button.addEventListener('click', function() {
          editCategory({
            Category_id: this.getAttribute('data-id')
            });
        });
    });
  }
  
  let addCategory = async (event)=> {
    event.preventDefault();
    const newCategoryName = document.getElementById("newCategoryName").value;
    const newCategoryDescription = document.getElementById("newCategoryDescription").value;
  
    // categories.push({
    //   name: newCategoryName,
    //   description: newCategoryDescription
    // });
    let data = {
      token_login_session:login_session_token,
      catagory_name:newCategoryName,
      catagory_description:newCategoryDescription
    }
    let response_data = await module.request_data_to_server({url:url_api_product_management_add_new_category_admin_brand_management,data:data,method:post_method})
      if (response_data.status){
        alert(response_data.message)
        location.reload()
      }
      else{
        alert(response_data.message)
      }

    location.reload()
    
  
    // document.getElementById("addCategoryForm").reset();
  }
  let editCategory = async ({Category_id}) => {
    let data = {
      token_login_session : login_session_token,
      catagory_id : Category_id
    }
    let response_data = await module.request_data_to_server({url:url_api_product_management_get_a_category_admin_brand_management,data:data,method:post_method})
      if (response_data.status){
        let category_id = response_data.message.category_id
        document.getElementById("editCategoryName").value = response_data.message.category_name;
        document.getElementById("editCategoryDescription").value = response_data.message.description;
        document.getElementById("editCategoryForm").style.display = "block";
        currentCategoryId = category_id; 
      }
      else{
        alert(response_data.message)
      }
    
  }
  
  let updateCategory = async (event) => {
    event.preventDefault();
    const editCategoryName = document.getElementById("editCategoryName").value;
    const editCategoryDescription = document.getElementById("editCategoryDescription").value;
  
    let data = {
      token_login_session : login_session_token,
      catagory_id : currentCategoryId,
      catagory_name:editCategoryName,
      catagory_description:editCategoryDescription
    }
    console.log(data)
    let response_data = await module.request_data_to_server({url:url_api_product_management_edit_category_admin_brand_management,data:data,method:put_method})
      if (response_data.status){
        alert(response_data.message)
        location.reload()
      }
      else{
        alert(response_data.message)
      }
  
    // document.getElementById("editCategoryForm").reset();
    // document.getElementById("editCategoryForm").style.display = "none";
  }
  
  let deleteCategory = async ({Category_id,Category_name}) =>{
    if (confirm(`Bạn có chắc chắn muốn xóa thể loại ${Category_name} và các sản phẩm của thể loại này không?`)) {
      let data = {
        token_login_session:login_session_token,
        catagory_id:Category_id
      }
      let response_data = await module.request_data_to_server({url:url_api_product_management_delete_category_admin_brand_management,data:data,method:delete_method})
      if (response_data.status){
        alert(response_data.message)
        location.reload()
      }
      else{
        alert(response_data.message)
      }
    }
  }
  
  document.getElementById("addCategoryForm").addEventListener("submit", addCategory);
  document.getElementById("editCategoryForm").addEventListener("submit", updateCategory);
  
