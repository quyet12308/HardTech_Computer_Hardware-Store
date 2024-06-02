url_login_basic = "http://localhost:8030/api/login"

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
      let datacovertojson = createDataObject(data)
      console.log(datacovertojson)
      console.log(typeof datacovertojson)
    
    a = await send_data_to_server_login_basic(datacovertojson)
    if(a.status){
      alert(a.message)
      // alert(a.token)
      token = a.token
      email = a.email
      is_admin = a.is_admin
      avata_img = a.avata_img
      sessionStorage.setItem('tokek_for_login_session', token);
      sessionStorage.setItem("avatar_img",avata_img)
      if (is_admin){
        window.location.href = "admin/admin_hompage.html"
      }
      else{
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

  function createDataObject(data) {

  
    return JSON.stringify(data);
  }


let send_data_to_server_login_basic = async (data) => {
    // Ngăn chặn hành vi mặc định của form submit
    // event.preventDefault();
  
    // Tạo các tùy chọn cho yêu cầu POST
    const requestOptions = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: data 
    };
  
    // Gửi yêu cầu POST đến backend
    return fetch(url_login_basic, requestOptions)
      .then(response => response.text())
      .then(data => {
        // Xử lý kết quả trả về từ server
        try {
          const parsedData = JSON.parse(data);
          a = parsedData.response;
          console.log(a);
          console.log(typeof(a))
          console.log(a.message)
          return a


          // Thực hiện các xử lý khác với dữ liệu ở đây
        } catch (error) {
          console.error("Lỗi khi phân tích dữ liệu JSON: ", error);
        }
      })
      .catch(error => {
        console.error("Lỗi khi gửi yêu cầu: ", error);
      });
  };