import * as module from './admin_module.js';

let token_admin = sessionStorage.getItem("is_admin")
let login_session_token =  sessionStorage.getItem('tokek_for_login_session')
let editProduct =  ({id_product})=> {
    window.location.href = `${module.base_url_api_backend}/admin/admin_edit_product.html?id_product=${id_product}`;  
    // Thêm chức năng chỉnh sửa sản phẩm tại đây
}

let deleteProduct = async ({ id_product, product_name })=> {
    const confirmed = confirm(`Bạn có chắc chắn muốn xóa sản phẩm "${product_name}"?`);
    if (confirmed){
        let data = {
            token_login_session:login_session_token,
            product_id : id_product
        }
        let delete_method = module.method_delete
        let url_api_product_management_delete_product = module.url_api_product_management_delete_product
        let response_data = await module.request_data_to_server({url:url_api_product_management_delete_product,data:data,method:delete_method})
        if (response_data.status){
            alert(response_data.message)
            location.reload()
        }
        else{
            alert(response_data.message)
        }
        
    }

    
}

document.addEventListener('DOMContentLoaded', async function () {

    
    let filter_btn = document.querySelector("#filter_btn")

    module.check_is_admin_logined()
    let post_method = module.method_post
    let data = {
        token_login_session:login_session_token
    }
    let url_api_admin_product_preview = module.url_api_product_management_preview;
    
    let response_data = await module.request_data_to_server({url:url_api_admin_product_preview,data:data,method:post_method})
    if (response_data.status){
        let products = response_data.message
        console.log(products)
        
        const brands = [...new Set(products.map(product => product.brand_name))];
        console.log(brands)
        const categories = [...new Set(products.map(product => product.category_name))];
        console.log(categories)


    
        function populateFilters() {
            const brandFilter = document.getElementById('brandFilter');
            const categoryFilter = document.getElementById('categoryFilter');
    
            brands.forEach(brand_name => {
                const option = document.createElement('option');
                option.value = brand_name;
                option.textContent = brand_name;
                brandFilter.appendChild(option);
            });
    
            categories.forEach(category_name => {
                const option = document.createElement('option');
                option.value = category_name;
                option.textContent = category_name;
                categoryFilter.appendChild(option);
            });
        }

        
    
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
                        <button class="button edit-button" data-id="${product.product_id}">Sửa</button>
                        <button class="button delete-button" data-id="${product.product_id}" data-name="${product.product_name}">Xóa</button>
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
                deleteProduct({
                    id_product: this.getAttribute('data-id'),
                    product_name: this.getAttribute('data-name')
                });
            });
        });
            
        }
    
        let filterProducts = ()=> {
            const nameFilter = document.getElementById('nameFilter').value.toLowerCase();
            const brandFilter = document.getElementById('brandFilter').value;
            const categoryFilter = document.getElementById('categoryFilter').value;
            const quantityFilter = document.getElementById('quantityFilter').value;
            const priceFilter = document.getElementById('priceFilter').value;
    
            let filteredProducts = products;
    
            if (nameFilter) {
                filteredProducts = filteredProducts.filter(product => product.product_name.toLowerCase().includes(nameFilter));
            }
            if (brandFilter) {
                filteredProducts = filteredProducts.filter(product => product.brand_name === brandFilter);
            }
            if (categoryFilter) {
                filteredProducts = filteredProducts.filter(product => product.category_name === categoryFilter);
            }
            if (quantityFilter) {
                filteredProducts = filteredProducts.filter(product => {
                    switch (quantityFilter) {
                        case '<10':
                            return product.quantity < 10;
                        case '10-20':
                            return product.quantity >= 10 && product.quantity <= 20;
                        case '20-50':
                            return product.quantity > 20 && product.quantity <= 50;
                        case '>50':
                            return product.quantity > 50;
                        default:
                            return true;
                    }
                });
            }
            if (priceFilter) {
                filteredProducts = filteredProducts.filter(product => {
                    switch (priceFilter) {
                        case '<1.000.000':
                            return product.price < 1000000;
                        case '1.000.000-2.000.000':
                            return product.price >= 1000000 && product.price <= 2000000;
                        case '2.000.000-5.000.000':
                            return product.price > 2000000 && product.price <= 5000000;
                        case '>5.000.000':
                            return product.price > 5000000;
                        default:
                            return true;
                    }
                });
            }
    
            displayProducts(filteredProducts);
        }
    
        
        filter_btn.addEventListener("click",()=>{
            filterProducts()
        })
    
        // window.onload = function() {
        //     alert("hoạt động")
        //     populateFilters();
        //     displayProducts(products);
        // }
        populateFilters();
        displayProducts(products)

        // Lấy các nút bằng id
        const editButton = document.getElementById("editButton");
        const deleteButton = document.getElementById("deleteButton");

        
    }
    else {
        alert(response_data.message)
    }

    
});

