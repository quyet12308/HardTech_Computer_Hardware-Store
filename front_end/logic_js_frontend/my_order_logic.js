import * as module from './module.js';



let url_api_my_order = module.url_api_my_order
let post_method = module.method_post
let login_session_token = sessionStorage.getItem('tokek_for_login_session');
document.addEventListener("DOMContentLoaded", async function() {
    // Tạo dữ liệu để gửi tới server, nếu cần
    let data = {
        token_login_session:login_session_token
    }
    console.log(data)
    console.log(url_api_my_order)
    try {
        // Sử dụng hàm request_data_to_server để lấy dữ liệu từ server
        let orders = await module.request_data_to_server({url: url_api_my_order, data: data, method: post_method});
        if (orders.status) {
            const tableBody = document.querySelector("#order-table tbody");
            orders.message.forEach(order => {
                const row = document.createElement("tr");

                const orderIdCell = document.createElement("td");
                orderIdCell.textContent = order.order_id;
                row.appendChild(orderIdCell);

                // const productNameCell = document.createElement("td");
                // productNameCell.textContent = order.productName;
                // row.appendChild(productNameCell);

                const productNameCell = document.createElement("td");
                productNameCell.innerHTML = order.products.map(product => `${product}`).join('<br>');
                row.appendChild(productNameCell);

                // const quantityCell = document.createElement("td");
                // quantityCell.textContent = order.quantity;
                // row.appendChild(quantityCell);

                const priceCell = document.createElement("td");
                priceCell.textContent = order.total_price;
                row.appendChild(priceCell);

                const paymentmethodCell = document.createElement("td");
                paymentmethodCell.textContent = order.payment_method;
                row.appendChild(paymentmethodCell);

                const orderDateCell = document.createElement("td");
                orderDateCell.textContent = module.formatDate(order.order_date) ;
                row.appendChild(orderDateCell);

                const ordernoteCell = document.createElement("td");
                ordernoteCell.textContent = order.order_note;
                row.appendChild(ordernoteCell);

                tableBody.appendChild(row);
            });
        } else {
            alert(orders.message)
            console.error("Dữ liệu đơn hàng không hợp lệ:", orders);
        }
    } catch (error) {
        console.error("Lỗi khi lấy dữ liệu từ server:", error);
    }
});



