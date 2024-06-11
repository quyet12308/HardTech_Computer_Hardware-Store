
// method
export const method_post = "POST"
export const method_put = "PUT"
export const method_delete = "DELETE"

// url api

export const url_api_hompage_layout = "http://localhost:8030/api/homepage/hompage_layout"
export const url_api_preview_product_detail = "http://localhost:8030/api/homepage/show-detailed-products"
export const url_api_add_product_to_cart = "http://localhost:8030/api/cartpage/add-product-to-cart"
export const url_api_get_cart_infor = "http://localhost:8030/api/cartpage/get_cart_infor"






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