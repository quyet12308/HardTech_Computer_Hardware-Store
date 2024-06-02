document.addEventListener('DOMContentLoaded',  function() {
    let pagination = document.querySelector('.pagination');
    pagination.innerHTML = ` 
  <ul class="pagination product__pagination">
  <li class="pagination-item">
      <a href="" class="pagination-item__link">
          <i class="pagination-item__icon fa-solid fa-angle-left"></i>
      </a>
  </li>
  <li class="pagination-item pagination-item--active">
      <a href="" class="pagination-item__link">1</a>
  </li>
  <li class="pagination-item">
      <a href="" class="pagination-item__link">2</a>
  </li>
  <li class="pagination-item">
      <a href="" class="pagination-item__link">3</a>
  </li>
  <li class="pagination-item">
      <a href="" class="pagination-item__link">4</a>
  </li>
  <li class="pagination-item">
      <a href="" class="pagination-item__link">5</a>
  </li>
  <li class="pagination-item">
      <a href="" class="pagination-item__link">...</a>
  </li>
  <li class="pagination-item">
      <a href="" class="pagination-item__link">14</a>
  </li>
  <li class="pagination-item">
      <a href="" class="pagination-item__link">
          <i class="pagination-item__icon fa-solid fa-angle-right"></i>
      </a>
  </li>
</ul>
  
`
})