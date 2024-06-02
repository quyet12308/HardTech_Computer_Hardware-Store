const imageInput = document.getElementById('image-input');
const previewImage = document.getElementById('preview-image');
const chooseImageBtn = document.getElementById('choose_image-btn');
const imageContainer = document.getElementById('image-container');

chooseImageBtn.addEventListener('click', () => {
  imageInput.click();
});

imageInput.addEventListener('change', () => {
  const file = imageInput.files[0];
  const imageUrl = URL.createObjectURL(file);
  previewImage.src = imageUrl;
  previewImage.style.display = 'block';

  // Điều chỉnh kích thước ảnh để vừa khít với khung
  const containerWidth = imageContainer.offsetWidth;
  const containerHeight = imageContainer.offsetHeight;
  previewImage.width = containerWidth;
  previewImage.height = containerHeight;
});

