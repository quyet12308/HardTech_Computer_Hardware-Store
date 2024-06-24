// import * as module from './module.js';
// let login_session_token = sessionStorage.getItem('tokek_for_login_session');

// let keyword = module.getQueryParameter('q')
// let post_method = module.method_post;

// let url_api_search_products_by_keyword = module.url_api_search_products_by_keyword;

// document.addEventListener('DOMContentLoaded', async function () {
    
//     let data = { keyword: keyword};
//     let response_data = await module.request_data_to_server({
//         url: url_api_search_products_by_keyword,
//         data: data,
//         method: post_method
//     });

//     if (response_data.status) {
//         console.log(response_data.message.products_list[0])
//         console.log(response_data.message.brands[0])
//         displayProducts(response_data.message.products_list)
//         populateManufacturers(response_data.message.brands);
        
//     } else {
//         alert(response_data.message);
//     }
// });

// function displayProducts(products) {
//     const productGrid = document.getElementById('productGrid');
//     productGrid.innerHTML = '';

//     products.forEach(product => {
//         const productItem = document.createElement('div');
//         productItem.className = 'product-item';
//         // productItem.id = ``
//         productItem.setAttribute('data-id', product.product_id);
//         productItem.addEventListener('click', function() {
//             window.location.href = `${module.url_base_front_hosting}/preview.html?id=${product.product_id}`;
//         });

//         const productImage = document.createElement('img');
//         productImage.src = product.image;
//         productImage.alt = product.product_name;

//         const productName = document.createElement('h3');
//         productName.textContent = product.product_name;

//         const productPrice = document.createElement('p');
//         productPrice.textContent = `Price: ${module.formatNumber(product.price) } VND`;

//         productItem.appendChild(productImage);
//         productItem.appendChild(productName);
//         productItem.appendChild(productPrice);

//         productGrid.appendChild(productItem);
//     });
// }

// function populateManufacturers(manufacturers) {
//     const manufacturerFilter = document.getElementById('manufacturerFilter');
//     manufacturerFilter.innerHTML = '<option value="">All Manufacturers</option>';

//     manufacturers.forEach(manufacturer => {
//         const option = document.createElement('option');
//         option.value = manufacturer.id;
//         option.textContent = manufacturer.name;
//         manufacturerFilter.appendChild(option);
//     });
// }

import * as module from './module.js';
let login_session_token = sessionStorage.getItem('tokek_for_login_session');

let keyword = module.getQueryParameter('q');
let post_method = module.method_post;
let url_api_search_products_by_keyword = module.url_api_search_products_by_keyword;

let allProducts = [];  // Biến để lưu trữ tất cả sản phẩm ban đầu

document.addEventListener('DOMContentLoaded', async function () {
    // Khởi tạo bộ lọc
    initFilters();

    // Lấy dữ liệu sản phẩm ban đầu
    await fetchInitialProducts();
});

function initFilters() {
    const searchInput = document.getElementById('searchInput');
    const manufacturerFilter = document.getElementById('manufacturerFilter');
    const priceFilter = document.getElementById('priceFilter');

    searchInput.addEventListener('input', applyFilters);
    manufacturerFilter.addEventListener('change', applyFilters);
    priceFilter.addEventListener('change', applyFilters);
}

async function fetchInitialProducts() {
    let data = { keyword: keyword };
    let response_data = await module.request_data_to_server({
        url: url_api_search_products_by_keyword,
        data: data,
        method: post_method
    });

    if (response_data.status) {
        allProducts = response_data.message.products_list;  // Lưu trữ tất cả sản phẩm ban đầu
        displayProducts(allProducts);
        populateManufacturers(response_data.message.brands);
    } else {
        alert(response_data.message);
    }
}

function applyFilters() {
    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    const manufacturer = document.getElementById('manufacturerFilter').value;
    const priceRange = document.getElementById('priceFilter').value;

    let filteredProducts = allProducts;

    // Lọc theo từ khóa tìm kiếm
    if (searchInput) {
        filteredProducts = filteredProducts.filter(product => product.product_name.toLowerCase().includes(searchInput));
    }

    // Lọc theo nhà sản xuất
    if (manufacturer) {
        console.log(manufacturer)
        filteredProducts = filteredProducts.filter(product => product.brand_id === manufacturer);
    }

    // Lọc theo khoảng giá
    if (priceRange) {
        let [minPrice, maxPrice] = priceRange.split('-').map(Number);
        filteredProducts = filteredProducts.filter(product => {
            let productPrice = Number(product.price);
            return (minPrice ? productPrice >= minPrice : true) && (maxPrice ? productPrice <= maxPrice : true);
        });
    }

    displayProducts(filteredProducts);
}

function displayProducts(products) {
    const productGrid = document.getElementById('productGrid');
    productGrid.innerHTML = '';

    products.forEach(product => {
        const productItem = document.createElement('div');
        productItem.className = 'product-item';
        productItem.setAttribute('data-id', product.product_id);
        productItem.addEventListener('click', function() {
            window.location.href = `${module.url_base_front_hosting}/preview.html?id=${product.product_id}`;
        });

        const productImage = document.createElement('img');
        productImage.src = product.image;
        productImage.alt = product.product_name;

        const productName = document.createElement('h3');
        productName.textContent = product.product_name;

        const productPrice = document.createElement('p');
        productPrice.textContent = `Price: ${module.formatNumber(product.price)} VND`;

        productItem.appendChild(productImage);
        productItem.appendChild(productName);
        productItem.appendChild(productPrice);

        productGrid.appendChild(productItem);
    });
}

function populateManufacturers(manufacturers) {
    const manufacturerFilter = document.getElementById('manufacturerFilter');
    manufacturerFilter.innerHTML = '<option value="">All Manufacturers</option>';

    manufacturers.forEach(manufacturer => {
        const option = document.createElement('option');
        option.value = manufacturer.id;
        option.textContent = manufacturer.name;
        manufacturerFilter.appendChild(option);
    });
}
