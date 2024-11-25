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


var options3 = {
    chart: {
        type: 'bar'

    }, plotOptions: {
        bar: {
            horizontal: true
        }
    }, series: [{
        data: [{
            x: 'category A', y: 10, goals: [{
                name: 'Expected', value: 22, strokeColor: '#775DD0'
            }, {
                name: 'Plan', value: 13, strokeColor: '#FF5AA0'
            },]
        }, {
            x: 'category B', y: 18, goals: [{
                name: 'Expected', value: 30, strokeColor: '#775DD0'
            }, {
                name: 'Plan', value: 25, strokeColor: '#FF5AA0'
            },]
        }, {
            x: 'category C', y: 13
        }]
    }]


}

var chart3 = new ApexCharts(document.querySelector("#sale-category3"), options3);

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

chart3.render();
chart4.render();
// chart5.render();
chart6.render();


const getMonthly = () => {
    fetch('api/statistics/').then(res => res.json()).then(result => {
        const yearly_data = result['yearly_stats']
        const months = yearly_data.map(item => item.month);
        const total_sale = yearly_data.map(item => item.total_sales);
        var options_yearly = {
            chart: {
                type: 'line'
            }, series: [{
                name: 'sales', data: total_sale
            }], xaxis: {
                categories: months
            },

        }
        var chart_yearly = new ApexCharts(document.querySelector("#sale-category2"), options_yearly);

        chart_yearly.render(months, total_sale)
    })
}

const getMonthlyTopProducts = () => {
    fetch('api/statistics/').then(res => res.json()).then(result => {
        const monthly_top_products_data = result['monthly_top_products']
        const product = monthly_top_products_data.map(item => item.NameProduct);
        const total_sold = monthly_top_products_data.map(item => item.total_sold);
        var options7 = {
            series: [{
                data: total_sold
            }],
            chart: {
                type: 'bar', height: 320
            },
            plotOptions: {
                bar: {
                    barHeight: '100%', distributed: true, horizontal: true, dataLabels: {
                        position: 'bottom'
                    },
                }
            },
            colors: ['#33b2df', '#546E7A', '#d4526e', '#13d8aa', '#A5978B', '#2b908f', '#f9a3a4', '#90ee7e', '#f48024', '#69d2e7'],
            dataLabels: {
                enabled: true, textAnchor: 'start', style: {
                    colors: ['#fff']
                }, formatter: function (val, opt) {
                    return opt.w.globals.labels[opt.dataPointIndex] + ":  " + val
                }, offsetX: 0, dropShadow: {
                    enabled: true
                }
            },
            stroke: {
                width: 1, colors: ['#fff']
            },
            xaxis: {
                categories: product,
            },
            yaxis: {
                labels: {
                    show: false
                }
            },
            title: {
                text: 'Monthly Top Products', align: 'center', floating: true
            },
            subtitle: {
                text: 'Category Names as DataLabels inside bars', align: 'center',
            },
            tooltip: {
                theme: 'dark', x: {
                    show: false
                }, y: {
                    title: {
                        formatter: function () {
                            return ''
                        }
                    }
                }
            }
        }

        var chart7 = new ApexCharts(document.querySelector("#sale-category7"), options7);
        chart7.render(product, total_sold)
    })
}

const getClients_monthly_trade_by_user = () => {
    fetch('api/statistics/').then(res => res.json()).then(result => {
        const clients_monthly_trade_by_user = result['clients_monthly_trade_by_user']
        // const month = clients_monthly_trade_by_user.map(item => item.month)
        const month = [...new Set(clients_monthly_trade_by_user.map(item => item.month))];

        const client = clients_monthly_trade_by_user.map(item => item.client__name)
        const trade = clients_monthly_trade_by_user.map(item => item.total_trade)


        var options5 = {
            series: [{
                name: client, type: 'column', data: trade
            },], chart: {
                height: 350, type: 'line', stacked: false,
            }, stroke: {
                width: [0, 2, 5], curve: 'smooth'
            }, plotOptions: {
                bar: {
                    columnWidth: '50%'
                }
            },

            fill: {
                opacity: [0.85, 0.25, 1], gradient: {
                    inverseColors: false,
                    shade: 'light',
                    type: "vertical",
                    opacityFrom: 0.85,
                    opacityTo: 0.55,
                    stops: [0, 100, 100, 100]
                }
            }, labels: month, markers: {
                size: 0
            }, xaxis: {
                type: 'datetime'
            }, yaxis: {
                title: {
                    text: 'Points',
                }
            }, tooltip: {
                shared: true, intersect: false, y: {
                    formatter: function (y) {
                        if (typeof y !== "undefined") {
                            return y.toFixed(0) + " points";
                        }
                        return y;

                    }
                }
            }

        }

        var chart5 = new ApexCharts(document.querySelector("#sale-category5"), options5);
        chart5.render()
    })
}

const getTest = () => {
    fetch('api/statistics/')
        .then(response => response.json())
        .then(result => {
            const clients_monthly_trade_by_user = result['clients_monthly_trade_by_user'];
            // Get unique months for the x-axis categories
            const months = [...new Set(clients_monthly_trade_by_user.map(item => item.month))];

            // Group data by client
            const tradeByClient = {};
            clients_monthly_trade_by_user.forEach(item => {
                const client = item.client__name;
                const trade = item.total_trade;
                const monthIndex = months.indexOf(item.month);

                if (!tradeByClient[client]) {
                    // Initialize trade array with zeros for all months
                    tradeByClient[client] = Array(months.length).fill(0);
                }

                // Set trade value for the correct month
                tradeByClient[client][monthIndex] = trade;
            });

            // Prepare series data
            const series = Object.entries(tradeByClient).map(([client, tradeData]) => ({
                name: client, type: 'column', data: tradeData
            }));

            console.log("Series Data:", series); // Debugging

            // Configure the ApexChart
            const options = {
                chart: {
                    type: 'line', // You can mix column and line charts
                    stacked: false
                }, series: series, xaxis: {
                    categories: months
                }, yaxis: {
                    title: {
                        text: "Trade Amount"
                    }
                }
            };

            const chart = new ApexCharts(document.querySelector("#sale-category5"), options);
            chart.render();
        })
        .catch(error => console.error("Error:", error));

}

window.onload(getMonthly(), getMonthlyTopProducts(), getTest())
