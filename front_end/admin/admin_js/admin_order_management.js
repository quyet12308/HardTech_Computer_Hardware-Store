import * as module from './admin_module.js';


document.addEventListener('DOMContentLoaded', function () {
  let return_home = document.querySelector("#return-home");
  let save_updates = document.querySelector("#save-updates");
  // Sample order data
  const orders = [
    { id: '001', customer: 'John Doe', value: '$100', products: 'Product A, Product B', status: 'completed' },
    { id: '002', customer: 'Jane Smith', value: '$150', products: 'Product C, Product D', status: 'pending' },
    { id: '003', customer: 'Sam Wilson', value: '$200', products: 'Product E, Product F', status: 'canceled' },
    // Add more orders as needed
];

function renderOrders(filterStatus = 'all', searchId = '') {
    const tbody = document.getElementById('order-table-body');
    tbody.innerHTML = '';
    let filteredOrders = orders;

    if (filterStatus !== 'all') {
        filteredOrders = filteredOrders.filter(order => order.status === filterStatus);
    }

    if (searchId) {
        filteredOrders = filteredOrders.filter(order => order.id.includes(searchId));
    }

    filteredOrders.forEach(((order, index) => {
      const row = document.createElement('tr');
      row.innerHTML = `
          <td>${index + 1}</td>
          <td>${order.id}</td>
          <td>${order.customer}</td>
          <td>${order.value}</td>
          <td>${order.products}</td>
          <td>
              <select class="status-select" id="status-select-${index}" onchange="updateStatus(${index}, this.value)">
                  <option value="pending" ${order.status === 'pending' ? 'selected' : ''}>Pending</option>
                  <option value="completed" ${order.status === 'completed' ? 'selected' : ''}>Completed</option>
                  <option value="canceled" ${order.status === 'canceled' ? 'selected' : ''}>Canceled</option>
              </select>
          </td>
      `;
      tbody.appendChild(row);
  }));
}



function updateStatus(index, newStatus) {
  orders[index].status = newStatus;
}

save_updates.addEventListener("click",()=>{
  console.log('Saving updates to the server...', orders);
  alert('Updates have been saved!');
})


document.getElementById('status-filter').addEventListener('change', (event) => {
  const filterStatus = event.target.value;
  const searchId = document.getElementById('order-search').value;
  renderOrders(filterStatus, searchId);
});

document.getElementById('order-search').addEventListener('input', (event) => {
  const searchId = event.target.value;
  const filterStatus = document.getElementById('status-filter').value;
  renderOrders(filterStatus, searchId);
});

return_home.addEventListener("click",()=>{
  alert('Returning to the admin dashboard...');
  window.location.href = 'admin_hompage.html';
})


// Initial render
renderOrders();
})


