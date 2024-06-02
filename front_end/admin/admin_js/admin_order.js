// script.js
document.addEventListener('DOMContentLoaded', () => {
    const orderList = document.getElementById('order-list');
    const filterForm = document.getElementById('filter-form');
    const statusForm = document.getElementById('status-form');
  
    // Fetch order data and populate the order list
    fetchOrders().then(orders => {
      orders.forEach(order => {
        const row = createOrderRow(order);
        orderList.appendChild(row);
      });
    });
  
    // Handle filter form submission
    filterForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const status = document.getElementById('order-status').value;
      filterOrders(status);
    });
  
    // Handle status update form submission
    statusForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const orderId = document.getElementById('order-id').value;
      const newStatus = document.getElementById('new-status').value;
      updateOrderStatus(orderId, newStatus);
    });
  });
  
  // Fetch order data from a backend API or database
  async function fetchOrders() {
    // Replace this with your actual order data fetching logic
    return [
      { id: 1, customer: 'Lâm', total: 100000, status: 'Chưa giải quyết' },
      { id: 2, customer: 'Dương', total: 2310130, status: 'Đang xử lý' },
      { id: 3, customer: 'Quyết', total: 12313, status: 'Đã vận chuyển' },
      { id: 4, customer: 'Panh', total: 12050, status: 'Đã giao hàng' },
      { id: 5, customer: 'Thái', total: 1240, status: 'Đã giao hàng' }
    ];
  }
  
  // Filter orders based on the selected status
  function filterOrders(status) {
    const orderRows = document.querySelectorAll('#order-list tr');
    orderRows.forEach(row => {
      const orderStatus = row.querySelector('td:nth-child(4)').textContent;
      if (status === '' || orderStatus.toLowerCase() === status.toLowerCase()) {
        row.style.display = 'table-row';
      } else {
        row.style.display = 'none';
      }
    });
  }
  
  // Update the order status
function updateOrderStatus(orderId, newStatus) {
    // Replace this with your actual order status update logic
    // Gửi yêu cầu cập nhật trạng thái đơn hàng đến backend
    fetch(`/api/orders/${orderId}/status`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ status: newStatus })
    })
    .then(response => {
      if (response.ok) {
        // Cập nhật trạng thái đơn hàng trong giao diện
        const statusCell = document.querySelector(`#order-list tr[data-id="${orderId}"] td:nth-child(4)`);
        statusCell.textContent = newStatus;
        alert(`Đã cập nhật trạng thái đơn hàng ${orderId} thành ${newStatus}`);
      } else {
        alert('Không thể cập nhật trạng thái đơn hàng. Vui lòng thử lại sau.');
      }
    })
    .catch(error => {
      console.error('Lỗi khi cập nhật trạng thái đơn hàng:', error);
      alert('Đã xảy ra lỗi khi cập nhật trạng thái đơn hàng. Vui lòng thử lại sau.');
    });
  }
  
  // Create a table row for an order
  function createOrderRow(order) {
    const row = document.createElement('tr');
  
    const idCell = document.createElement('td');
    idCell.textContent = order.id;
    row.appendChild(idCell);
  
    const customerCell = document.createElement('td');
    customerCell.textContent = order.customer;
    row.appendChild(customerCell);
  
    const totalCell = document.createElement('td');
    totalCell.textContent = order.total.toFixed(2);
    row.appendChild(totalCell);
  
    const statusCell = document.createElement('td');
    statusCell.textContent = order.status;
    row.appendChild(statusCell);
  
    const actionsCell = document.createElement('td');
    const editButton = document.createElement('button');
    editButton.textContent = 'Edit';
    editButton.addEventListener('click', () => {
      // Handle edit button click
      console.log(`Editing order ${order.id}`);
    });
    actionsCell.appendChild(editButton);
    row.appendChild(actionsCell);
  
    return row;
  }