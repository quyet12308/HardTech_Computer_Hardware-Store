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

// Assuming we have a function to fetch current product details
function loadProductDetails(productId) {
    // Mock data for product details
    const productDetails = {
        image: 'path/to/current/image.jpg', // URL of the current product image
        name: 'Tên Sản Phẩm Hiện Tại',
        price: 100000,
        description: 'Mô tả sản phẩm hiện tại',
        brand: 'Brand1',
        category: 'Category2',
        quantity: 50
    };

    // Populate form with current product details
    document.getElementById('productName').value = productDetails.name;
    document.getElementById('productPrice').value = productDetails.price;
    document.getElementById('productDescription').value = productDetails.description;
    document.getElementById('productBrand').value = productDetails.brand;
    document.getElementById('productCategory').value = productDetails.category;
    document.getElementById('productQuantity').value = productDetails.quantity;

    // Display current product image
    const imagePreview = document.getElementById('imagePreview');
    imagePreview.innerHTML = '';
    const img = document.createElement('img');
    img.src = productDetails.image;
    img.style.maxWidth = '100%';
    img.style.maxHeight = '100%';
    imagePreview.appendChild(img);
}

// Call the function to load product details on page load
document.addEventListener('DOMContentLoaded', function() {
    const productId = 1; // Replace with actual product ID
    loadProductDetails(productId);
});

document.getElementById('editProductForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Collect form data
    const productData = {
        image: document.getElementById('productImage').files[0],
        name: document.getElementById('productName').value,
        price: document.getElementById('productPrice').value,
        description: document.getElementById('productDescription').value,
        brand: document.getElementById('productBrand').value,
        category: document.getElementById('productCategory').value,
        quantity: document.getElementById('productQuantity').value
    };

    // Log the collected data to the console (you can replace this with actual form submission logic)
    console.log(productData);

    // Optionally, you can reset the form or provide feedback to the user
    // document.getElementById('editProductForm').reset();
    // document.getElementById('imagePreview').innerHTML = '';
});