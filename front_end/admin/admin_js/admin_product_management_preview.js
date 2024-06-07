const products = [
    {  name: "Sản phẩm A", brand: "Hãng 1", category: "Thể loại 1", quantity: 15,discount: 10, price: 1500000 },
        {  name: "Sản phẩm B", brand: "Hãng 2", category: "Thể loại 2", quantity: 5,discount: 20, price: 800000 },
        { name: "Sản phẩm C", brand: "Hãng 1", category: "Thể loại 3", quantity: 25,discount: 30, price: 3000000 },
        // Thêm dữ liệu sản phẩm tại đây
    ];

    const brands = [...new Set(products.map(product => product.brand))];
    const categories = [...new Set(products.map(product => product.category))];

    function populateFilters() {
        const brandFilter = document.getElementById('brandFilter');
        const categoryFilter = document.getElementById('categoryFilter');

        brands.forEach(brand => {
            const option = document.createElement('option');
            option.value = brand;
            option.textContent = brand;
            brandFilter.appendChild(option);
        });

        categories.forEach(category => {
            const option = document.createElement('option');
            option.value = category;
            option.textContent = category;
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
                <td>${product.name}</td>
                <td>${product.brand}</td>
                <td>${product.category}</td>
                <td>${product.quantity}</td>
                <td>${product.discount}</td>
                <td>${product.price.toLocaleString('vi-VN', { style: 'currency', currency: 'VND' })}</td>
                <td>
                    <button class="button" onclick="editProduct(${index + 1})">Sửa</button>
                    <button class="button" onclick="deleteProduct(${index + 1})">Xóa</button>
                    <button class="button" onclick="detailProduct(${product.stt})">Chi tiết</button>
                </td>
            `;
            productTable.appendChild(row);
        });
    }

    function filterProducts() {
        const nameFilter = document.getElementById('nameFilter').value.toLowerCase();
        const brandFilter = document.getElementById('brandFilter').value;
        const categoryFilter = document.getElementById('categoryFilter').value;
        const quantityFilter = document.getElementById('quantityFilter').value;
        const priceFilter = document.getElementById('priceFilter').value;

        let filteredProducts = products;

        if (nameFilter) {
            filteredProducts = filteredProducts.filter(product => product.name.toLowerCase().includes(nameFilter));
        }
        if (brandFilter) {
            filteredProducts = filteredProducts.filter(product => product.brand === brandFilter);
        }
        if (categoryFilter) {
            filteredProducts = filteredProducts.filter(product => product.category === categoryFilter);
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
                    case '<1000000':
                        return product.price < 1000000;
                    case '1000000-2000000':
                        return product.price >= 1000000 && product.price <= 2000000;
                    case '2000000-5000000':
                        return product.price > 2000000 && product.price <= 5000000;
                    case '>5000000':
                        return product.price > 5000000;
                    default:
                        return true;
                }
            });
        }

        displayProducts(filteredProducts);
    }

    function editProduct(stt) {
        alert(`Chỉnh sửa sản phẩm với STT: ${stt}`);
        // Thêm chức năng chỉnh sửa sản phẩm tại đây
    }

    function deleteProduct(stt) {
        if (confirm(`Bạn có chắc chắn muốn xóa sản phẩm với STT: ${stt}?`)) {
            const productIndex = products.findIndex(product => product.stt === stt);
            if (productIndex !== -1) {
                products.splice(productIndex, 1);
                filterProducts();
            }
        }
    }

    window.onload = function() {
        populateFilters();
        displayProducts(products);
    }