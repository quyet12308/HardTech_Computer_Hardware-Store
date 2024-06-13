
// method
export const method_post = "POST"
export const method_put = "PUT"
export const method_delete = "DELETE"

// let base_url_api_backend = `https://phat-trien-he-thong-thuong-mai-dien-tu-nhom-10-oerf.vercel.app`
let base_url_api_backend = "http://localhost:8030"


// url api

// admin

export const url_api_homepage = `${base_url_api_backend}/api/admin/admin-homepage`
export const url_api_product_management_preview =  `${base_url_api_backend}/api/admin/admin_product_management_preview`
export const url_api_product_management_delete_product =  `${base_url_api_backend}/api/admin/delete_product`
export const url_api_product_management_get_product_detail =  `${base_url_api_backend}/api/admin/get_product_detail`
export const url_api_product_management_get_all_brands_admin_brand_management =  `${base_url_api_backend}/api/admin/get_all_brands_admin_brand_management`
export const url_api_product_management_add_new_brand_admin_brand_management =  `${base_url_api_backend}/api/admin/add_new_brand`
export const url_api_product_management_delete_brand_admin_brand_management =  `${base_url_api_backend}/api/admin/delete_brand`
export const url_api_product_management_get_brand_detail_admin_brand_management =  `${base_url_api_backend}/api/admin/get_brand_detail`
export const url_api_product_management_edit_brand_admin_brand_management =  `${base_url_api_backend}/api/admin/edit_brand`
export const url_api_product_management_get_all_categories_admin_brand_management =  `${base_url_api_backend}/api/admin/get_all_categories`
export const url_api_product_management_add_new_category_admin_brand_management =  `${base_url_api_backend}/api/admin/add_new_category`
export const url_api_product_management_edit_category_admin_brand_management =  `${base_url_api_backend}/api/admin/edit_category`
export const url_api_product_management_delete_category_admin_brand_management =  `${base_url_api_backend}/api/admin/delete_category`
export const url_api_product_management_get_a_category_admin_brand_management =  `${base_url_api_backend}/api/admin/get_a_category`
export const url_api_product_management_add_new_product =  `${base_url_api_backend}/api/admin/add-new-product`
export const url_api_product_management_get_brands_and_catagories =  `${base_url_api_backend}/api/admin/get_brands_and_catagories`




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

export let check_is_admin_logined = ()=>{
  let token_admin = sessionStorage.getItem("is_admin")
  if (token_admin === null) {
    alert("Bạn chưa đăng nhập. Vui lòng đăng nhập để tiếp tục.");
    window.location.href = "http://127.0.0.1:5500/login.html"; // Chuyển hướng tới trang đăng nhập
  } else if (token_admin === "false") {
      // Kiểm tra nếu token_admin là false (lưu ý là giá trị trong sessionStorage là chuỗi)
      alert("Bạn không đủ quyền truy cập trang này.");
      window.location.href = "http://127.0.0.1:5500/index.html"; // Chuyển hướng tới trang home
  } else if (token_admin === "true") {

  }
  else {
      // Trường hợp không mong muốn, có thể xử lý thêm nếu cần
      console.error("Giá trị không hợp lệ trong sessionStorage: is_admin");
  }
}