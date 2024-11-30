var options1 = {
    chart: {
        type: 'bar'
    }, series: [{
        data: [{
            x: 'Evyap', y: 25000, goals: [{
                name: 'Expected', value: 20000, strokeColor: '#775DD0'
            }]
        }, {
            x: 'Avon', y: 18000
        }, {
            x: 'Garnier', y: 13000
        }, {
            x: 'Himalaya', y: 8000
        }]
    }]
}
var chart1 = new ApexCharts(document.querySelector("#sale-category"), options1);
// var month = ['September', 'October', 'November']
// var total_sales = [150, 250, 350]


var options4 = {
    series: [{
        data: [44, 55, 41, 64,]
    }, {
        data: [53, 32, 33, 52,]
    }], chart: {
        type: 'bar', height: 280
    }, plotOptions: {
        bar: {
            horizontal: true, dataLabels: {
                position: 'top',
            },
        }
    }, dataLabels: {
        enabled: true, offsetX: -6, style: {
            fontSize: '12px', colors: ['#fff']
        }
    }, stroke: {
        show: true, width: 1, colors: ['#fff']
    }, tooltip: {
        shared: true, intersect: false
    }, xaxis: {
        categories: [2020, 2021, 2022, 2023],
    },


}
var chart4 = new ApexCharts(document.querySelector("#sale-category4"), options4);

var options6 = {
    series: [{
        name: 'Marine Sprite', data: [44, 55, 41, 37, 22, 43, 21]
    }, {
        name: 'Striking Calf', data: [53, 32, 33, 52, 13, 43, 32]
    }, {
        name: 'Tank Picture', data: [12, 17, 11, 9, 15, 11, 20]
    }, {
        name: 'Bucket Slope', data: [9, 7, 5, 8, 6, 9, 4]
    }, {
        name: 'Reborn Kid', data: [25, 12, 19, 32, 25, 24, 10]
    }], chart: {
        type: 'bar', height: 350, stacked: true, stackType: '100%'
    }, plotOptions: {
        bar: {
            horizontal: true,
        },
    }, stroke: {
        width: 1, colors: ['#fff']
    }, title: {
        text: '100% Stacked Bar'
    }, xaxis: {
        categories: [2008, 2009, 2010, 2011, 2012, 2013, 2014],
    }, tooltip: {
        y: {
            formatter: function (val) {
                return val + "K"
            }
        }
    }, fill: {
        opacity: 1

    }, legend: {
        position: 'top', horizontalAlign: 'left', offsetX: 40
    }
}
var chart6 = new ApexCharts(document.querySelector("#sale-category6"), options6);


chart1.render();

// chart3.render();
chart4.render();

chart6.render();

const getDaily = () => {
    fetch('api/statistics/')
        .then(res => res.json())
        .then(result => {
            const daily_data = result['daily_order_statistics_for_month'];

            // Extract data for the chart
            const labels = daily_data.map(item => item.date); // Dates
            const daily_orders_count = daily_data.map(item => item.daily_orders_count); // Orders count
            const daily_total_sales = daily_data.map(item => item.daily_total_sales); // Total sales

            // Configure the ApexChart options
            var option_daily = {
                series: [{
                    name: 'Daily Orders (dona)', type: 'column', data: daily_orders_count, // Data for orders count
                }, {
                    name: 'Total Sales (Sum)', type: 'line', data: daily_total_sales, // Data for total sales
                },], chart: {
                    height: 350, type: 'line',
                }, stroke: {
                    width: [0, 4], // Width of column and line strokes
                }, title: {
                    text: 'Daily Order Statistics',
                }, dataLabels: {
                    enabled: true, enabledOnSeries: [1], // Enable data labels only on the line chart
                }, labels: labels, // Dates as labels
                yaxis: [{
                    title: {
                        text: 'Daily Orders',
                    },
                }, {
                    opposite: true, title: {
                        text: 'Total Sales',
                    },
                },],
            };

            // Render the chart
            var chart = new ApexCharts(document.querySelector("#daily-trade"), option_daily);
            chart.render();
        })
        .catch(error => console.error('Error fetching daily statistics:', error));

}
const getMonthly = () => {
    fetch('api/statistics/')
        .then(res => res.json())
        .then(result => {
            const data = result['monthly_trade_for_year'];
            const months = data.map(item => item.month);
            const trades = data.map(item => item.total_trade);

            // Set up your chart
            var options = {
                series: [{
                    name: 'Monthly Trade', data: trades,
                }], chart: {
                    type: 'line', height: 350,
                }, xaxis: {
                    categories: months,  // Months as categories
                },
            };

            var chart = new ApexCharts(document.querySelector("#monthly-trade"), options);
            chart.render();
        });

}
const getMonthlyProductSales = () => {
    fetch('api/statistics/')
        .then(res => res.json())
        .then(result => {
            const data = result['monthly_product_sales_statistics'];
            // Extract categories (months) and series (product data)

            const categories = data.map(item => item.month);
            const productData = {};

            data.forEach(item => {
                item.data.forEach(product => {
                    const name = product.product;
                    if (!productData[name]) {
                        productData[name] = new Array(categories.length).fill(0);
                    }
                    productData[name][categories.indexOf(item.month)] = product.count;
                });
            });
            const generateColors = () => {
                const colors = [];
                for (let i = 0; i < 100; i++) {
                    const hue = Math.floor(Math.random() * 360); // Random hue
                    const saturation = 70 + Math.random() * 30;  // Saturation 70-100%
                    const lightness = 50 + Math.random() * 20;   // Lightness 50-70%
                    colors.push(`hsl(${hue}, ${saturation}%, ${lightness}%)`);
                }
                return colors;
            };

            const colors = generateColors();

            const series = Object.keys(productData).map((product, index) => ({
                name: product, data: productData[product], color: colors[index], // Assign unique color to each product
            }));
            // ApexChart Options
            const options = {
                series: series, chart: {
                    type: 'bar', height: 550, stacked: true,
                }, plotOptions: {
                    bar: {
                        horizontal: true,
                    },
                }, xaxis: {
                    categories: categories,
                }, title: {
                    text: 'Monthly Product Sales',
                }, fill: {
                    opacity: 1,
                }, colors: colors, // Use dynamic colors
            };

            // Render the chart
            var chart = new ApexCharts(document.querySelector("#monthly-product-trade"), options);
            chart.render();

        });

}
const get6MonthProductSales = () => {
    fetch('api/statistics/')
        .then(res => res.json())
        .then(result => {
            const data = result['six_month_product_sales_statistics'];
            const months = data.months; // List of last 6 months
            const productData = data.data; // Product data

            // Extract product names for x-axis
            const productNames = productData.map(item => item.product);

            // Prepare series for chart (one series per month)
            const series = months.map((month, index) => ({
                name: month, data: productData.map(item => item.counts[index] || 0),
            }));

            // Chart options
            var options = {
                series: series, chart: {
                    type: 'bar', height: 550, stacked: true, toolbar: {
                        show: true,
                    }, zoom: {
                        enabled: true,
                    },
                }, plotOptions: {
                    bar: {
                        horizontal: false, columnWidth: '75%', endingShape: 'rounded',
                    },
                }, xaxis: {
                    categories: productNames, // Products on x-axis
                    title: {
                        text: 'Products',
                    }, labels: {
                        style: {
                            fontSize: '12px',
                            fontWeight: 'Bold'
                        },
                    }, // Enable scrolling for x-axis
                    tickPlacement: 'on', axisBorder: {
                        show: true,
                    },
                }, yaxis: {
                    title: {
                        text: 'Product Count',
                    }, labels: {
                        style: {
                            fontSize: '12px',
                            fontWeight:'Bold'
                        },
                    },
                }, dataLabels: {
                    enabled: false,
                }, legend: {
                    position: 'top', horizontalAlign: 'center',
                }, title: {
                    text: 'Product Sales (Last 6 Months)', align: 'center',
                }, tooltip: {
                    shared: true, intersect: false,
                }, grid: {
                    padding: {
                        bottom: 10,
                    },
                }, scrollable: {
                    x: true,
                },
            };

            // Render chart
            var chart = new ApexCharts(document.querySelector("#month6-trade-each-product"), options);
            chart.render();
        });


}
// const getMonthlyTopProducts = () => {
//     fetch('api/statistics/').then(res => res.json()).then(result => {
//         const monthly_top_products_data = result['monthly_top_products']
//         const product = monthly_top_products_data.map(item => item.NameProduct);
//         const total_sold = monthly_top_products_data.map(item => item.total_sold);
//         var options7 = {
//             series: [{
//                 data: total_sold
//             }],
//             chart: {
//                 type: 'bar', height: 320
//             },
//             plotOptions: {
//                 bar: {
//                     barHeight: '100%', distributed: true, horizontal: true, dataLabels: {
//                         position: 'bottom'
//                     },
//                 }
//             },
//             colors: ['#33b2df', '#546E7A', '#d4526e', '#13d8aa', '#A5978B', '#2b908f', '#f9a3a4', '#90ee7e', '#f48024', '#69d2e7'],
//             dataLabels: {
//                 enabled: true, textAnchor: 'start', style: {
//                     colors: ['#fff']
//                 }, formatter: function (val, opt) {
//                     return opt.w.globals.labels[opt.dataPointIndex] + ":  " + val
//                 }, offsetX: 0, dropShadow: {
//                     enabled: true
//                 }
//             },
//             stroke: {
//                 width: 1, colors: ['#fff']
//             },
//             xaxis: {
//                 categories: product,
//             },
//             yaxis: {
//                 labels: {
//                     show: false
//                 }
//             },
//             title: {
//                 text: 'Monthly Top Products', align: 'center', floating: true
//             },
//             subtitle: {
//                 text: 'Category Names as DataLabels inside bars', align: 'center',
//             },
//             tooltip: {
//                 theme: 'dark', x: {
//                     show: false
//                 }, y: {
//                     title: {
//                         formatter: function () {
//                             return ''
//                         }
//                     }
//                 }
//             }
//         }
//
//         var chart7 = new ApexCharts(document.querySelector("#sale-category7"), options7);
//         chart7.render(product, total_sold)
//     })
// }
//
//
// const getClients_monthly_trade_by_user = () => {
//     fetch('api/statistics/')
//         .then(response => response.json())
//         .then(result => {
//             const clients_monthly_trade_by_user = result['clients_monthly_trade_by_user'];
//             // Get unique months for the x-axis categories
//             const months = [...new Set(clients_monthly_trade_by_user.map(item => item.month))];
//
//             // Group data by client
//             const tradeByClient = {};
//             clients_monthly_trade_by_user.forEach(item => {
//                 const client = item.client__name;
//                 const trade = item.total_trade;
//                 const monthIndex = months.indexOf(item.month);
//
//                 if (!tradeByClient[client]) {
//                     // Initialize trade array with zeros for all months
//                     tradeByClient[client] = Array(months.length).fill(0);
//                 }
//
//                 // Set trade value for the correct month
//                 tradeByClient[client][monthIndex] = trade;
//             });
//
//             // Prepare series data
//             const series = Object.entries(tradeByClient).map(([client, tradeData]) => ({
//                 name: client, type: 'column', data: tradeData
//             }));
//
//             // Configure the ApexChart
//             const options = {
//                 series: series, chart: {
//                     height: 350, type: 'line', stacked: false,
//                 }, stroke: {
//                     width: [0, 2, 5], curve: 'smooth'
//                 }, plotOptions: {
//                     bar: {
//                         columnWidth: '50%'
//                     }
//                 },
//
//                 fill: {
//                     opacity: [0.85, 0.25, 1], gradient: {
//                         inverseColors: false,
//                         shade: 'light',
//                         type: "vertical",
//                         opacityFrom: 0.85,
//                         opacityTo: 0.55,
//                         stops: [0, 100, 100, 100]
//                     }
//                 }, labels: months, markers: {
//                     size: 0
//                 }, xaxis: {
//                     type: 'datetime'
//                 }, yaxis: {
//                     title: {
//                         text: 'Sum',
//                     }
//                 }, tooltip: {
//                     shared: true, intersect: false, y: {
//                         formatter: function (y) {
//                             if (typeof y !== "undefined") {
//                                 return y.toFixed(0) + " Sum";
//                             }
//                             return y;
//
//                         }
//                     }
//                 }
//             };
//
//             const chart = new ApexCharts(document.querySelector("#sale-category5"), options);
//             chart.render();
//         })
//         .catch(error => console.error("Error:", error));
//
// }
//
// const getPopularCategory = () => {
//     fetch('api/statistics/')
//         .then(response => response.json())
//         .then(result => {
//             const popular_categories = result['popular_categories_monthly_by_user'];
//             const monthly_trade = popular_categories['monthly_trade']
//             console.log(popular_categories[0]['category'])
//             var options3 = {
//                 chart: {
//                     type: 'bar'
//
//                 }, plotOptions: {
//                     bar: {
//                         horizontal: true
//                     }
//                 }, series: [{
//                     data: [{
//                         x: 'category A', y: 10, goals: [{
//                             name: 'Expected', value: 22, strokeColor: '#775DD0'
//                         }, {
//                             name: 'Plan', value: 13, strokeColor: '#FF5AA0'
//                         },]
//                     }, {
//                         x: 'category B', y: 18, goals: [{
//                             name: 'Expected', value: 30, strokeColor: '#775DD0'
//                         }, {
//                             name: 'Plan', value: 25, strokeColor: '#FF5AA0'
//                         },]
//                     }, {
//                         x: 'category C', y: 13
//                     }]
//                 }]
//
//
//             }
//
//             var chart3 = new ApexCharts(document.querySelector("#sale-category3"), options3);
//             chart3.render()
//         })
//         .catch(error => console.error("Error:", error));
//
// }

window.onload(getDaily(), getMonthly(), getMonthlyProductSales(), get6MonthProductSales())
