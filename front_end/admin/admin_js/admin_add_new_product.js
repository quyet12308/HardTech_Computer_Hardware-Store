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

document.getElementById('productForm').addEventListener('submit', function(event) {
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

    // Reset form
    document.getElementById('productForm').reset();
    document.getElementById('imagePreview').innerHTML = '';
});