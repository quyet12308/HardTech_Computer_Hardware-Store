import * as module from './module.js';

let url_api_send_verification_email = module.url_api_send_verification_email
let url_api_create_account = module.url_api_create_account

let post_method = module.method_post;
let delete_method = module.method_delete;
let put_method = module.method_put


document.addEventListener('DOMContentLoaded', () => {
    let form = document.getElementById('register-form');
    let username = document.getElementById('username1');
    let email = document.getElementById('email1');
    let password1 = document.getElementById('password1');
    let password2 = document.getElementById('password2');
    let submitButton = document.getElementById('submit-button');
    let registerError = document.getElementById('register-error');
    let hCaptchaResponse = document.getElementById('h-captcha-response');
    let hCaptchaWidget = document.querySelector('.h-captcha');

    let validateEmail = (email) => {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    let validatePassword = (password) => {
        const re = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$/;
        return re.test(String(password));
    }

    let validateForm = () => {
        let isValid = true;
        let errorMessages = [];

        if (username.value.length <= 5) {
            isValid = false;
            errorMessages.push('Tên tài khoản phải dài hơn 5 kí tự.');
        }

        if (!validateEmail(email.value)) {
            isValid = false;
            errorMessages.push('Email không đúng định dạng.');
        }

        if (!validatePassword(password1.value)) {
            isValid = false;
            errorMessages.push('Mật khẩu phải dài hơn 5 ký tự và phải có chữ và số.');
        }

        if (password1.value !== password2.value) {
            isValid = false;
            errorMessages.push('Mật khẩu nhập lại không khớp.');
        }

        if (!hCaptchaResponse.value) {
            isValid = false;
            errorMessages.push('Vui lòng xác minh mình không phải là robot.');
        }

        registerError.innerHTML = errorMessages.join('<br>');

        return isValid;
    }

    // hCaptchaWidget.addEventListener('hcaptcha-verified', (event) => {
    //     hCaptchaResponse.value = event.detail.response;
    //     if (validateForm()) {
    //         submitButton.disabled = false;
    //     }
    // });

    // form.addEventListener('input', () => {
    //     if (validateForm()) {
    //         submitButton.disabled = false;
    //     } else {
    //         submitButton.disabled = true;
    //     }
    // });

    // form.addEventListener('submit', (event) => {
    //     if (!validateForm()) {
    //         event.preventDefault();
    //     }
    // });
    form.addEventListener('submit', async (event) => {
        console.log("register action")
        event.preventDefault();
        // if (validateForm()) {
            let data = {
                email: email.value,
                username: username.value,
                // hcaptcha_response: hCaptchaResponse.value,
            };
            console.log(data)
            let response = await module.request_data_to_server({ url: url_api_send_verification_email, data: data, method: post_method });

            if (response.status){
                let code = prompt("Vui lòng nhập code đã được gửi đến email của bạn đã đăng ký , chú ý code chỉ có giá trị trong thời gian 3 phút")
                let data_confirm_code ={
                    password :password1.value,
                    email : email.value,
                    code : code,
                    username : username.value,
                }
                console.log(data_confirm_code)
                let response_confirm_code = await module.request_data_to_server({ url: url_api_create_account, data: data_confirm_code, method: post_method });
                if (response_confirm_code.status){
                    alert(response_confirm_code.message)
                    window.location.href = `${module.url_base_front_hosting}/login.html`
                }
                else{
                    alert(response_confirm_code.message)
                }
            }
            else{
                alert(response.message)
            }
            
        // }
    });
});

// import * as module from './module.js';

//         let url_api_send_verification_email = module.url_api_send_verification_email
//         let url_api_create_account = module.url_api_create_account

//         let post_method = module.method_post;
//         let delete_method = module.method_delete;
//         let put_method = module.method_put


//         document.addEventListener('DOMContentLoaded', () => {
//             console.log('Document loaded');
            
//             const registerForm = document.getElementById('register-form');
//             const usernameInput = document.getElementById('username1');
//             const emailInput = document.getElementById('email1');
//             const passwordInput = document.getElementById('password1');
//             const confirmPasswordInput = document.getElementById('password2');
//             const hcaptchaResponseInput = document.getElementById('h-captcha-response');
//             const submitButton = document.getElementById('submit-button');
//             const registerErrorDiv = document.getElementById('register-error');
        
//             // Function to check if all conditions are met
//             function validateForm() {
//                 let errors = [];
        
//                 // Check username length
//                 if (usernameInput.value.length < 5) {
//                     errors.push('Tên đăng ký phải từ 5 ký tự trở lên.');
//                 }
        
//                 // Check password length
//                 if (passwordInput.value.length < 5) {
//                     errors.push('Mật khẩu phải từ 5 ký tự trở lên.');
//                 }
        
//                 // Check password contains both letters and numbers
//                 const passwordRegex = /^(?=.*[a-zA-Z])(?=.*[0-9])/;
//                 if (!passwordRegex.test(passwordInput.value)) {
//                     errors.push('Mật khẩu phải chứa cả chữ và số.');
//                 }
        
//                 // Check passwords match
//                 if (passwordInput.value !== confirmPasswordInput.value) {
//                     errors.push('Mật khẩu và Nhập lại mật khẩu không khớp.');
//                 }
        
//                 // Check hCaptcha
//                 if (!hcaptchaResponseInput.value) {
//                     errors.push('Vui lòng xác nhận captcha.');
//                 }
        
//                 return errors;
//             }
        
//             // Add event listener to form submit
//             registerForm.addEventListener('submit', (event) => {
//                 console.log('Form submit event triggered');
//                 event.preventDefault();
//                 registerErrorDiv.innerHTML = '';
//                 const errors = validateForm();
        
//                 if (errors.length > 0) {
//                     registerErrorDiv.innerHTML = errors.map(error => `<p>${error}</p>`).join('');
//                 } else {
//                     // Collect data and prepare to send to backend
//                     const data = {
//                         email: emailInput.value,
//                         username: usernameInput.value,
//                         hcaptcha_response: hcaptchaResponseInput.value
//                     };
        
//                     console.log(data)
//                 }
//             });
        
//             // Enable submit button if hCaptcha is completed
//             window.hcaptchaCallback = function (token) {
//                 console.log('hCaptcha completed with token: ', token);
//                 hcaptchaResponseInput.value = token;
//                 submitButton.disabled = false;
//             };
//         });
        