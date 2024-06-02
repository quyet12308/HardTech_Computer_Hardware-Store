let products = [
    {id:1,}
  ];
  
  // Hàm hiển thị danh sách sản phẩm
  function displayProducts() {
    const productList = document.getElementById('product-list');
    productList.innerHTML = '';
  
    products.forEach(product => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${product.id}</td>
        <td>${product.name}</td>
        
        <td>${product.price.toFixed(2)} VND</td>
        <td>
          <button onclick="editProduct(${product.id})">Sửa</button>
          <button onclick="deleteProduct(${product.id})">Xóa</button>
        </td>
      `;
      productList.appendChild(row);
    });
  }
  
  // Hàm thêm sản phẩm mới
  const productForm = document.getElementById('product-form');
  productForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('product-name').value;
    const description = document.getElementById('product-description').value;
    const price = parseFloat(document.getElementById('product-price').value);
  
    const newProduct = { id: products.length + 1, name, description, price };
    products.push(newProduct);
    displayProducts();
  
    productForm.reset();
  });

  // Hiển thị hình ảnh sản phẩm
// function displayProductImage(product) {
//     const imageElement = document.createElement('img');
//     imageElement.src = `images/${product.image}`;
//     imageElement.alt = product.name;
//     imageElement.style.maxWidth = '100px';
//     return imageElement;
//   }
  
  // Cập nhật hình ảnh sản phẩm
//   function updateProductImage(id) {
//     const product = products.find(p => p.id === id);
//     const fileInput = document.getElementById(`product-image-${id}`);
//     const file = fileInput.files[0];
  
//     if (file) {
//       const reader = new FileReader();
//       reader.onload = function(e) {
//         product.image = file.name;
//         displayProducts();
//       };
//       reader.readAsDataURL(file);
//     }
//   }
  
  // Hàm sửa thông tin sản phẩm
  function editProduct(id) {
    const product = products.find(p => p.id === id);
    document.getElementById('product-name').value = product.name;
    document.getElementById('product-description').value = product.description;
    document.getElementById('product-price').value = product.price;
  }
  
  // Hàm xóa sản phẩm
  function deleteProduct(id) {
    products = products.filter(p => p.id !== id);
    displayProducts();
  }


  
  // Hiển thị danh sách sản phẩm ban đầu
  displayProducts();