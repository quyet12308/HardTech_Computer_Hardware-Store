import * as module from './module.js';

let url_login_basic = module.url_api_login
let post_method = module.method_post

document.addEventListener('DOMContentLoaded',  function() {
    var loginForm = document.getElementById('login-form');
    var fogotLink = document.querySelector("#forgot-link");
    var loginError = document.getElementById('login-error');
    var registerLink = document.getElementById('register-link');
    
    fogotLink.addEventListener("click",()=>{
      window.location.href = "forgot_password.html"
    });

    registerLink.addEventListener("click",()=>{
      window.location.href = "register.html"
    })

  // xử lý logic đăng nhập
    loginForm.addEventListener('submit',async function(event) {
      event.preventDefault();
  
      var username = document.getElementById('username').value;
      var password = document.getElementById('password').value;
  
      if (username.length < 4) {
        loginError.innerText = 'Tên đăng nhập phải có ít nhất 4 ký tự.';
        return;
      }
  
      if (password.length < 5 || !/\d/.test(password) || !/[a-zA-Z]/.test(password)) {
        loginError.innerText = 'Mật khẩu phải có ít nhất 5 ký tự và bao gồm cả chữ và số.';
        return;
      }
  
      loginError.innerText = ''; // Xóa thông báo nếu điều kiện đúng
      // Tiếp tục xử lý đăng nhập

      let data = {
        username: username,
        password: password,
      }
      
    
    let a = await module.request_data_to_server({ url: url_login_basic, data: data, method: post_method })
    if(a.status){
      alert(a.message)
      // alert(a.token)
      let token = a.token
      let email = a.email
      let is_admin = a.is_admin
      let avata_img = a.avata_img
      let user_name = a.user_name
      sessionStorage.setItem('tokek_for_login_session', token);
      sessionStorage.setItem("avatar_img",avata_img)
      sessionStorage.setItem("user_name",user_name)
      if (is_admin){
        sessionStorage.setItem("is_admin",true)
        window.location.href = "admin/admin_hompage.html"
      }
      else{
        sessionStorage.setItem("is_admin",false)
        window.location.href = "index.html"
      }
      
    }
    else{
      alert(a.message)
    }
    });
  

    // if (a.status){
    //     // ý tưởng là truyền tham số vào url , lưu user vào web để chỉ cần đăng nhập 1 lần 
    //     window.location.href = "http://127.0.0.1:5500"
    // }

    
  });
