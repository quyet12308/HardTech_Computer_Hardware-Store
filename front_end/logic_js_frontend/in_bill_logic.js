import * as module from './module.js';

let login_session_token = sessionStorage.getItem('tokek_for_login_session');
let payment_method = sessionStorage.getItem("payment_method")

let checksum = ""
let url_api_update_order_status_when_user_payment_success = module.url_api_update_order_status_when_user_payment_success
let post_method = module.method_post;
let delete_method = module.method_delete;

document.addEventListener('DOMContentLoaded', async  ()=> {
    if (payment_method === "zalopay"){
        let payment_status = module.getQueryParameter('status');
        if (payment_status != 1){
            alert("Thanh toán thất bại")
            window.location.href = `${module.url_base_front_hosting}/index.html`
        }
        else {
            checksum = module.getQueryParameter("apptransid")
        }
    }
    if (payment_method === "momo"){
        let payment_status = module.getQueryParameter('resultCode');
        if (payment_status != 0){
            alert("Thanh toán thất bại")
            window.location.href = `${module.url_base_front_hosting}/index.html`
        }
        else {
            checksum = module.getQueryParameter("orderId")
        }
    }
    if (payment_method === "paypal"){
        let payment_status = module.getQueryParameter('resultCode');
        // if (payment_status != 0){
        //     alert("Thanh toán thất bại")
        //     window.location.href = `${module.url_base_front_hosting}/index.html`
        // }
        // else {
        //     checksum = module.getQueryParameter("token")
        // }
        checksum = module.getQueryParameter("token")
    }
    if (payment_method === "stripe"){
        let payment_status = module.getQueryParameter('status');
        if (payment_status != 1){
            alert("Thanh toán thất bại")
            window.location.href = `${module.url_base_front_hosting}/index.html`
        }
        else {
            checksum = module.getQueryParameter("stripe_payid")
        }
    }


    let data = {
        token_login_session:login_session_token,
        checksum:checksum,
        payment_method:payment_method
    }
    console.log(data)
    let response = await module.request_data_to_server({ url: url_api_update_order_status_when_user_payment_success, data: data, method: post_method });
    if (response.status) {

        let user_info = response.message.user_info
        let order_details = response.message.order_details
        // Sample data
        let customerName = user_info.fullname;
        let customerAddress = user_info.order_address;
        let paymentMethod = payment_method
        let note = user_info.order_note
        let products = order_details
        // let products = [
        //     { name: "Sản Phẩm 1", quantity: 2, price: 50000 },
        //     { name: "Sản Phẩm 2", quantity: 1, price: 100000 },
        //     { name: "Sản Phẩm 3", quantity: 3, price: 75000 }
        // ];

        document.getElementById('customer-name').textContent = customerName;
        document.getElementById('customer-address').textContent = customerAddress;
        document.getElementById('payment-method').textContent = paymentMethod;
        document.querySelector("#note-order").textContent = note
        document.getElementById('print-date').textContent = new Date().toLocaleDateString('vi-VN');

        const productTable = document.getElementById('product-list');
        let totalAmount = 0;

        products.forEach(product => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${product.product_name}</td>
                <td>${product.qty}</td>
                <td>${product.order_price.toLocaleString('vi-VN')} VNĐ</td>
                <td>${(product.qty * product.order_price).toLocaleString('vi-VN')} VNĐ</td>
            `;
            productTable.appendChild(row);
            totalAmount += product.qty * product.order_price;
        });

        document.getElementById('total-amount-number').textContent = totalAmount.toLocaleString('vi-VN');
        document.getElementById('total-amount-text').textContent = module.convertNumberToWords(totalAmount) + " đồng";
        // Download PDF
        let btn_download_pdf = document.querySelector("#btn_download_pdf")
        btn_download_pdf.addEventListener("click",()=>{
            const invoiceElement = document.getElementById('invoice');
            html2pdf().from(invoiceElement).save('hoa-don.pdf');
        }
        
        )
        let btn_go_homepage = document.querySelector("#btn_go_homepage")
        btn_go_homepage.addEventListener("click",()=>{
            window.location.href = `${module.url_base_front_hosting}/index.html`
        })
    }
    else{
        alert(response.message)
    }

    
    
        

});

