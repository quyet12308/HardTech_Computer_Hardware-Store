// url base hosting web back-end
export let base_url_api_backend = `http://localhost:8030`
// export let base_url_api_backend = `https://phat-trien-he-thong-thuong-mai-dien-tu-nhom-10-oerf.vercel.app`

// url base hosting web front-end
export let url_base_front_hosting = `http://127.0.0.1:5500` // local
// export let url_base_front_hosting = `https://phat-trien-he-thong-thuong-mai-dien-tu-nhom-10.vercel.app` // local

// method
export const method_post = "POST"
export const method_put = "PUT"
export const method_delete = "DELETE"

// url api
// user
export const url_api_login = `${base_url_api_backend}/api/login`
export const url_api_hompage_layout =  `${base_url_api_backend}/api/homepage/hompage_layout`
export const url_api_preview_product_detail =  `${base_url_api_backend}/api/homepage/show-detailed-products`
export const url_api_add_product_to_cart =  `${base_url_api_backend}/api/cartpage/add-product-to-cart`
export const url_api_get_cart_infor =  `${base_url_api_backend}/api/cartpage/get_cart_infor`






export let request_data_to_server = async ({data,url,method}) => {
    // Ngăn chặn hành vi mặc định của form submit
    // event.preventDefault();
  
    // Tạo các tùy chọn cho yêu cầu POST
    const requestOptions = {
      method: method,
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data) 
    };
  
    // Gửi yêu cầu POST đến backend
    return fetch(url, requestOptions)
      .then(response => response.text())
      .then(data => {
        // Xử lý kết quả trả về từ server
        try {
          const parsedData = JSON.parse(data);
          // console.log(parsedData)
        //   console.log(typeof(parsedData))
          let a = parsedData.response;
          // console.log(a);
        //   console.log(typeof(a))
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

export let get_data_from_server = async (url) => {
    try {
      const response = await fetch(url);
      const data = await response.json();
      console.log(data);
      console.log(typeof data);
      return data.response;
    } catch (error) {
      console.error("Lỗi khi gửi yêu cầu đến máy chủ:", error);
      throw error;
    }
  };

export function getQueryParameter(name) {
  let params = new URLSearchParams(window.location.search);
  return params.get(name);
}

// Chuyển đổi hình ảnh sang base64
export const convertToBase64 = (file) => {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = (error) => reject(error);
    });
};

export function formatNumber(number) {
  // Chuyển số thành chuỗi và đảm bảo nó là một số nguyên dương
  number = Math.abs(parseInt(number, 10));

  // Kiểm tra nếu số là NaN hoặc không phải là số
  if (isNaN(number)) {
    return '';
  }

  // Chuyển số thành chuỗi và đảm bảo độ dài chuỗi lớn hơn 3
  let numberString = number.toString();
  while (numberString.length < 3) {
    numberString = '0' + numberString;
  }

  // Tạo một mảng để lưu trữ các phần tử chuỗi
  let parts = [];

  // Chia chuỗi thành các phần tử có độ dài 3 và lưu vào mảng
  while (numberString.length > 3) {
    parts.unshift(numberString.slice(-3));
    numberString = numberString.slice(0, -3);
  }

  // Thêm phần tử cuối cùng vào mảng
  parts.unshift(numberString);

  // Kết hợp các phần tử lại với nhau, giữa các phần tử có dấu chấm
  return parts.join('.');
}

export let check_user_logined = ()=>{
  let login_session_token =  sessionStorage.getItem('tokek_for_login_session')
  if (login_session_token) {
    // Người dùng đã đăng nhập
    return true;
  } else {
    // Người dùng chưa đăng nhập
    return false;
  }
}