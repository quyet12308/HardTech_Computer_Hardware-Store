import * as module from './module.js';




document.addEventListener('DOMContentLoaded', async function() {
    var fogotpasswordForm = document.getElementById('fogotpassword-form');
    var fogotpasswordError = document.getElementById('fogotpassword-error');
    let login_link = document.querySelector("#login-link2");

    //chuyển trang login
    login_link.addEventListener("click",()=>{
      window.location.href = "login.html"
    })

    // xử lý logic đăng ký
    fogotpasswordForm.addEventListener('submit',async function(event)  {
        event.preventDefault();
        let url_api_forgot_password = module.url_api_forgot_password
        let url_api_reset_password = module.url_api_reset_password
        let post_method = module.method_post
        // var username = document.getElementById('username2').value;
        var email = document.getElementById('email2').value;
        var password = document.getElementById('password2').value;
    
        // if (username.length < 6) {
        //   fogotpasswordError.innerText = 'Tên đăng ký phải có ít nhất 6 ký tự.';
        //   return;
        // }
    
        if (!/\S+@\S+\.\S+/.test(email)) {
          fogotpasswordError.innerText = 'Vui lòng nhập đúng định dạng email.';
          return;
        }
    
        if (password.length < 5 || !/\d/.test(password) || !/[a-zA-Z]/.test(password)) {
          fogotpasswordError.innerText = 'Mật khẩu phải có ít nhất 5 ký tự và bao gồm cả chữ và số.';
          return;
        }
    
        fogotpasswordError.innerText = ''; // Xóa thông báo nếu điều kiện đúng
        // Tiếp tục xử lý đăng k
        let data = {
          email:email
        }
        console.log(data)
        console.log(url_api_forgot_password)
        
        let a = await module.request_data_to_server({ url: url_api_forgot_password, data: data, method: post_method })
        console.log(a.message)
        if(a.status){
            let code = prompt("Vui lòng nhập code đã được gửi đến email của bạn đã điền , chú ý code chỉ có giá trị trong thời gian 3 phút ,nếu không thấy email đến rất có thể nó nằm trong hòm thư rác")
            let data2 ={
                new_password: password,
                email:email,
                code: code
            }
            let check_code_from_server = await module.request_data_to_server({ url: url_api_reset_password, data: data2, method: post_method })
            if(check_code_from_server.status){
                alert("Bạn thay đổi mật khẩu thành công")
                window.location.href = "login.html"
                }
            else{
            alert(check_code_from_server.message)
            }
      }
      else{
        alert(a.message)
      }
    });
})