const slides = document.querySelectorAll('.slide');
const thumbs = document.querySelectorAll('.thumb');

let currentIndex = 0;

function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.classList.toggle('active', i === index);
  });

  thumbs.forEach((thumb, i) => {
    thumb.classList.toggle('active', i === index);
  });
}

thumbs.forEach((thumb, index) => {
  thumb.addEventListener('click', () => {
    currentIndex = index;
    showSlide(currentIndex);
  });
});

// setInterval(() => {
//   currentIndex = (currentIndex + 1) % slides.length;
//   showSlide(currentIndex);
// }, 5000);

showSlide(currentIndex);

// Lấy tất cả các nút tăng, giảm và ô input số lượng
const btnMinus = document.querySelectorAll('.btn-minus');
const btnPlus = document.querySelectorAll('.btn-plus');
const quantityValues = document.querySelectorAll('.quantity-value');

// Xử lý sự kiện click trên nút giảm
btnMinus.forEach(btn => {
  btn.addEventListener('click', () => {
    const quantityValue = btn.parentNode.querySelector('.quantity-value');
    let value = parseInt(quantityValue.value);
    if (value > 1) {
      quantityValue.value = value - 1;
    }
  });
});

// Xử lý sự kiện click trên nút tăng
btnPlus.forEach(btn => {
  btn.addEventListener('click', () => {
    const quantityValue = btn.parentNode.querySelector('.quantity-value');
    let value = parseInt(quantityValue.value);
    quantityValue.value = value + 1;
  });
});

// Xử lý sự kiện input trên ô nhập số lượng
quantityValues.forEach(input => {
  input.addEventListener('input', () => {
    let value = parseInt(input.value);
    if (isNaN(value) || value < 1) {
      input.value = '1';
    }
  });

  input.addEventListener('input', (event) => {
    // Chỉ cho phép nhập số
    event.target.value = event.target.value.replace(/\D/g, '');
  });
});