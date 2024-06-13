import * as module from './admin_module.js';

document.addEventListener('DOMContentLoaded', async function () {
    let main_content = document.querySelector(".group_right-container .main-content")
    let log_out = document.querySelector("#log_out")
    let token_admin = sessionStorage.getItem("is_admin")
    let login_session_token =  sessionStorage.getItem('tokek_for_login_session')

    // log out
    log_out.addEventListener("click",()=>{
        sessionStorage.removeItem("is_admin")
        sessionStorage.removeItem("tokek_for_login_session")
        window.location.href = `${module.base_url_api_backend}/login.html`;
    })

    module.check_is_admin_logined()

    let url_api_homepage = module.url_api_homepage;
    let post_method = module.method_post
    let data = {
        token_login_session:login_session_token,
        timeframe:"week"
    }
    let response_data = await module.request_data_to_server({url:url_api_homepage,data:data,method:post_method})
    if (response_data.status){
        let num_new_user = response_data.message.data_4_parameter.new_users
        let num_new_order = response_data.message.data_4_parameter.new_orders
        let num_total_revenue = response_data.message.data_4_parameter.total_revenue
        let num_new_product = response_data.message.data_4_parameter.new_products
        let data_lineChart = response_data.message.data_lineChart
        let data_pieChart = response_data.message.data_pieChart
        let data_barChart = response_data.message.data_barChart

        let layout_without_chart = `
            <!-- Nút chọn thời gian thống kê -->
            <div class="time-selector">
                    <label for="time-period">Chọn thời gian thống kê: </label>
                    <select id="time-period">
                        <option value="week">Tuần</option>
                        <option value="month">Tháng</option>
                        <option value="quarter">Quý</option>
                    </select>
            </div>

            <div class="tabbar">
                    <div class="tab-item">
                        <h3>Số lượng user mới</h3>
                        <p>${num_new_user}</p>
                    </div>
                    <div class="tab-item">
                        <h3>Số lượng đơn đặt hàng mới</h3>
                        <p>${num_new_order}</p>
                    </div>
                    <div class="tab-item">
                        <h3>Số doanh thu mới</h3>
                        <p>${num_total_revenue}đ</p>
                    </div>
                    <div class="tab-item">
                        <h3>Số lượng sản phẩm mới nhập</h3>
                        <p>${num_new_product}</p>
                    </div>
                </div>

                <div id="charts">
                    <div class="chart-container">
                        <canvas id="lineChart"></canvas>
                    </div>
                    <div class="chart-container">
                        <canvas id="pieChart"></canvas>
                    </div>
                    <div class="chart-container">
                        <canvas id="barChart"></canvas>
                    </div>
                </div>
            `
            main_content.innerHTML = layout_without_chart

            const ctxLine = document.getElementById('lineChart').getContext('2d');
            const ctxPie = document.getElementById('pieChart').getContext('2d');
            const ctxBar = document.getElementById('barChart').getContext('2d');

            const lineChart = new Chart(ctxLine, {
                type: 'line',
                data: data_lineChart,
                options: {
                    plugins: {
                        title: {
                            display: true,
                            text: 'Biểu đồ thống kê doanh thu và đơn hàng'
                        }
                    },
                    scales: {
                        y: {
                            type: 'linear',
                            display: true,
                            position: 'left',
                            title: {
                                display: true,
                                text: 'Doanh thu (đ)'
                            }
                        },
                        y1: {
                            type: 'linear',
                            display: true,
                            position: 'right',
                            title: {
                                display: true,
                                text: 'Số đơn hàng'
                            },
                            grid: {
                                drawOnChartArea: false, // Chỉ cần vẽ lưới cho trục y chính
                            },
                        }
                    }
                }
            });
            
            const pieChart = new Chart(ctxPie, {
                type: 'pie',
                data: data_pieChart,
                options: {
                    plugins: {
                        title: {
                            display: true,
                            text: 'Biểu đồ thống kê các sản phẩm bán chạy nhất'
                        }
                    }
                }
            });
            
            const barChart = new Chart(ctxBar, {
                type: 'bar',
                data: data_barChart,
                options: {
                    scales: {
                        y: {
                            beginAtZero: true,
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'Biểu đồ thống kê các loại mặt hàng nhập nhiều nhất'
                        }
                    }
                }
            });

            
      }else{
        alert(response_data.message)
      }
      document.getElementById('time-period').addEventListener('change',async function() {
        let selectedPeriod = this.value;
        // Ở đây bạn có thể gọi hàm để cập nhật biểu đồ với thời gian được chọn
        alert(selectedPeriod)
        let url_api_homepage = module.url_api_homepage;
        let post_method = module.method_post
        let data = {
            token_login_session:login_session_token,
            timeframe:selectedPeriod
        }
        let response_data = await module.request_data_to_server({url:url_api_homepage,data:data,method:post_method})
        if (response_data.status){
            let num_new_user = response_data.message.data_4_parameter.new_users
            let num_new_order = response_data.message.data_4_parameter.new_orders
            let num_total_revenue = response_data.message.data_4_parameter.total_revenue
            let num_new_product = response_data.message.data_4_parameter.new_products
            let data_lineChart = response_data.message.data_lineChart
            let data_pieChart = response_data.message.data_pieChart
            let data_barChart = response_data.message.data_barChart
    
            let layout_without_chart = `
                <!-- Nút chọn thời gian thống kê -->
                <div class="time-selector">
                        <label for="time-period">Chọn thời gian thống kê: </label>
                        <select id="time-period">
                            <option value="week">Tuần</option>
                            <option value="month">Tháng</option>
                            <option value="quarter">Quý</option>
                        </select>
                </div>
    
                <div class="tabbar">
                        <div class="tab-item">
                            <h3>Số lượng user mới</h3>
                            <p>${num_new_user}</p>
                        </div>
                        <div class="tab-item">
                            <h3>Số lượng đơn đặt hàng mới</h3>
                            <p>${num_new_order}</p>
                        </div>
                        <div class="tab-item">
                            <h3>Số doanh thu mới</h3>
                            <p>${num_total_revenue}đ</p>
                        </div>
                        <div class="tab-item">
                            <h3>Số lượng sản phẩm mới nhập</h3>
                            <p>${num_new_product}</p>
                        </div>
                    </div>
    
                    <div id="charts">
                        <div class="chart-container">
                            <canvas id="lineChart"></canvas>
                        </div>
                        <div class="chart-container">
                            <canvas id="pieChart"></canvas>
                        </div>
                        <div class="chart-container">
                            <canvas id="barChart"></canvas>
                        </div>
                    </div>
                `
                main_content.innerHTML = layout_without_chart
    
                const ctxLine = document.getElementById('lineChart').getContext('2d');
                const ctxPie = document.getElementById('pieChart').getContext('2d');
                const ctxBar = document.getElementById('barChart').getContext('2d');
    
                const lineChart = new Chart(ctxLine, {
                    type: 'line',
                    data: data_lineChart,
                    options: {
                        plugins: {
                            title: {
                                display: true,
                                text: 'Biểu đồ thống kê doanh thu và đơn hàng'
                            }
                        },
                        scales: {
                            y: {
                                type: 'linear',
                                display: true,
                                position: 'left',
                                title: {
                                    display: true,
                                    text: 'Doanh thu (đ)'
                                }
                            },
                            y1: {
                                type: 'linear',
                                display: true,
                                position: 'right',
                                title: {
                                    display: true,
                                    text: 'Số đơn hàng'
                                },
                                grid: {
                                    drawOnChartArea: false, // Chỉ cần vẽ lưới cho trục y chính
                                },
                            }
                        }
                    }
                });
                
                const pieChart = new Chart(ctxPie, {
                    type: 'pie',
                    data: data_pieChart,
                    options: {
                        plugins: {
                            title: {
                                display: true,
                                text: 'Biểu đồ thống kê các sản phẩm bán chạy nhất'
                            }
                        }
                    }
                });
                
                const barChart = new Chart(ctxBar, {
                    type: 'bar',
                    data: data_barChart,
                    options: {
                        scales: {
                            y: {
                                beginAtZero: true,
                            }
                        },
                        plugins: {
                            title: {
                                display: true,
                                text: 'Biểu đồ thống kê các loại mặt hàng nhập nhiều nhất'
                            }
                        }
                    }
                });
                
    
                
          }else{
            alert(response_data.message)
          }
    });


    
    



    
    
    
    
});