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