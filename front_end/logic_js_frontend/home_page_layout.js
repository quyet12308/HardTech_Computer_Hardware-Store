import * as module from './module.js';

let url_api_hompage_layout = module.url_api_hompage_layout

document.addEventListener('DOMContentLoaded', async  ()=> {

    let response_data = await module.get_data_from_server(url_api_hompage_layout)
        if (response_data.status) {
            let newest_products = document.querySelector(".main .content #newest_products")
            let product_1_list_heading = document.querySelector(".main .content #product_1_list_heading")
            let product_1_list_content = document.querySelector(".main .content #product_1_list_content")

            let product_2_list_heading = document.querySelector(".main .content #product_2_list_heading")
            let product_2_list_content = document.querySelector(".main .content #product_2_list_content")

            let product_3_list_heading = document.querySelector(".main .content #product_3_list_heading")
            let product_3_list_content = document.querySelector(".main .content #product_3_list_content")

            let product_4_list_heading = document.querySelector(".main .content #product_4_list_heading")
            let product_4_list_content = document.querySelector(".main .content #product_4_list_content")

            let product_1_list_content_htmls = ``
            let product_2_list_content_htmls = ``
            let product_3_list_content_htmls = ``
            let product_4_list_content_htmls = ``
            // let categories_and_brands = response_data.message.categories_and_brands
            // let brands = brands_and_catagories.brands;
            // let categories = brands_and_catagories.categories;

            
            // let categories_html = `<h3>Categories</h3>`;
            
            
            // for (let category of categories) {
            //     let category_html = `<li><a href="#" id="catagory_${category.id}">${category.name}</a></li>`;
            //     categories_html = categories_html + category_html;
            // }
            
            // document.querySelector("#categories_list ul").innerHTML = categories_html;

            let new_products = response_data.message.list_products.newest
            let product_type_0 = response_data.message.list_products.product_type_0
            let product_type_1 = response_data.message.list_products.product_type_1
            let product_type_2 = response_data.message.list_products.product_type_2
            let product_type_3 = response_data.message.list_products.product_type_3
            let newest_product_htmls = ``
            
            
            for (let new_product of new_products){
                let new_product_html =  `
                    <div class="grid_1_of_4 images_1_of_4">
                        <a href="#" class="product_detail" data-id-product="${new_product.product_id}"><img src="${new_product.image}" alt="" />
                            <h2>${new_product.product_name}</h2>
                        </a>	 
                        <div class="price-details">
                            <div class="discounted_detail">
                                <div class="original_price-main">${new_product.price}đ</div>
                                <div class="discounted_persent-main">${new_product.discount}%</div>
                            </div>
                            <div class="discounted_price-main">${new_product.price -(new_product.price * (new_product.discount/100)) }đ</div>
                                <div class="clear"></div>
                        </div>
                    </div>
                `

                newest_product_htmls = newest_product_htmls + new_product_html
                
            }
            let product_1_list_heading_html = `
                <div class="heading">
				<h3>${product_type_0[0].category_name}</h3>
				</div>
				<div class="see">
					<p id="see_all_products_type_0" data-id= "${product_type_0[0].category_id}"><a href="#">See all Products</a></p>
				</div>
				<div class="clear"></div>
            `
            for (let product of product_type_0){
                let product_type_0_html = `
                    <div class="grid_1_of_4 images_1_of_4">
						 <a href="#" class="product_detail" data-id-product="${product.product_id}"><img src="${product.image}" alt="" /></a>					
						 <h2>${product.product_name} </h2>
						<div class="price-details">
						   <div class="price-number">
								<p><span class="rupees">${product.price}đ</span></p>
							</div>
								 <div class="clear"></div>
						</div>
					</div>
                `
                product_1_list_content_htmls = product_1_list_content_htmls + product_type_0_html

            }
            let product_2_list_heading_html = `
                <div class="heading">
				<h3>${product_type_1[0].category_name}</h3>
				</div>
				<div class="see">
					<p id="see_all_products_type_1" data-id= "${product_type_1[0].category_id}"><a href="#">See all Products</a></p>
				</div>
				<div class="clear"></div>
            `
            for (let product of product_type_1){
                let product_type_1_html = `
                    <div class="grid_1_of_4 images_1_of_4">
						 <a href="#" class="product_detail" data-id-product="${product.product_id}"><img src="${product.image}" alt="" /></a>					
						 <h2>${product.product_name} </h2>
						<div class="price-details">
						   <div class="price-number">
								<p><span class="rupees">${product.price}đ</span></p>
							</div>
								 <div class="clear"></div>
						</div>
					</div>
                `
                product_2_list_content_htmls = product_2_list_content_htmls + product_type_1_html

            }
            let product_3_list_heading_html = `
                <div class="heading">
				<h3>${product_type_2[0].category_name}</h3>
				</div>
				<div class="see">
					<p id="see_all_products_type_2" data-id= "${product_type_2[0].category_id}"><a href="#">See all Products</a></p>
				</div>
				<div class="clear"></div>
            `
            for (let product of product_type_2){
                let product_type_2_html = `
                    <div class="grid_1_of_4 images_1_of_4">
						 <a href="#" class="product_detail" data-id-product="${product.product_id}"><img src="${product.image}" alt="" /></a>					
						 <h2>${product.product_name} </h2>
						<div class="price-details">
						   <div class="price-number">
								<p><span class="rupees">${product.price}đ</span></p>
							</div>
								 <div class="clear"></div>
						</div>
					</div>
                `
                product_3_list_content_htmls = product_3_list_content_htmls + product_type_2_html

            }
            let product_4_list_heading_html = `
                <div class="heading">
				<h3>${product_type_3[0].category_name}</h3>
				</div>
				<div class="see">
					<p id="see_all_products_type_3" data-id= "${product_type_3[0].category_id}"><a href="#">See all Products</a></p>
				</div>
				<div class="clear"></div>
            `
            for (let product of product_type_3){
                let product_type_3_html = `
                    <div class="grid_1_of_4 images_1_of_4">
						 <a href="#" class="product_detail" data-id-product="${product.product_id}"><img src="${product.image}" alt="" /></a>					
						 <h2>${product.product_name} </h2>
						<div class="price-details">
						   <div class="price-number">
								<p><span class="rupees">${product.price}đ</span></p>
							</div>
								 <div class="clear"></div>
						</div>
					</div>
                `
                product_4_list_content_htmls = product_4_list_content_htmls + product_type_3_html

            }
            
            newest_products.innerHTML = newest_product_htmls
            product_1_list_heading.innerHTML = product_1_list_heading_html
            product_2_list_heading.innerHTML = product_2_list_heading_html
            product_3_list_heading.innerHTML = product_3_list_heading_html
            product_4_list_heading.innerHTML = product_4_list_heading_html

            product_1_list_content.innerHTML = product_1_list_content_htmls
            product_2_list_content.innerHTML = product_2_list_content_htmls
            product_3_list_content.innerHTML = product_3_list_content_htmls
            product_4_list_content.innerHTML = product_4_list_content_htmls

            document.querySelectorAll('.product_detail').forEach(button => {
                button.addEventListener('click', function(event) {
                    event.preventDefault(); // Prevent default anchor behavior
                    let productId = this.getAttribute('data-id-product');
                    redirectToProductDetail(productId);
                });
            });
        }
});

function redirectToProductDetail(productId) {
    // Replace 'product-detail.html' with the actual URL of your product detail page
    let productDetailUrl = `http://127.0.0.1:5500/preview.html?id=${productId}`;
    window.location.href = productDetailUrl;
}