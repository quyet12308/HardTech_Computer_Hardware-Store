// Lấy reference của master checkbox và danh sách các item checkbox
const masterCheckbox = document.getElementById('cart__check-all');
const itemCheckboxes = document.querySelectorAll('.cart__check');

// Thêm event listener cho master checkbox
masterCheckbox.addEventListener('change', function() {
  // Duyệt qua danh sách các item checkbox và đánh dấu chúng theo trạng thái của master checkbox
  itemCheckboxes.forEach(function(checkbox) {
    checkbox.checked = masterCheckbox.checked;
  });
});

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