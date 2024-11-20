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

var options2 = {
    chart: {
        type: 'line'
    }, series: [{
        name: 'sales', data: [30, 40, 35, 50, 49, 60, 70, 91, 125]
    }], xaxis: {
        categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
    },

}

var chart2 = new ApexCharts(document.querySelector("#sale-category2"), options2);

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
var options5 = {
    series: [{
        name: 'TEAM A', type: 'column', data: [23, 11, 22, 27, 13, 22, 37, 21, 44, 22, 30]
    }, {
        name: 'TEAM B', type: 'area', data: [44, 55, 41, 67, 22, 43, 21, 41, 56, 27, 43]
    }, {
        name: 'TEAM C', type: 'line', data: [30, 25, 36, 30, 45, 35, 64, 52, 59, 36, 39]
    }],
    chart: {
        height: 350, type: 'line', stacked: false,
    },
    stroke: {
        width: [0, 2, 5], curve: 'smooth'
    },
    plotOptions: {
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
    },
    labels: ['01/01/2003', '02/01/2003', '03/01/2003', '04/01/2003', '05/01/2003', '06/01/2003', '07/01/2003', '08/01/2003', '09/01/2003', '10/01/2003', '11/01/2003'],
    markers: {
        size: 0
    },
    xaxis: {
        type: 'datetime'
    },
    yaxis: {
        title: {
            text: 'Points',
        }
    },
    tooltip: {
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
var options7 = {
    series: [{
        data: [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380]
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
        categories: ['South Korea', 'Canada', 'United Kingdom', 'Netherlands', 'Italy', 'France', 'Japan', 'United States', 'China', 'India'],
    },
    yaxis: {
        labels: {
            show: false
        }
    },
    title: {
        text: 'Custom DataLabels', align: 'center', floating: true
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


chart1.render();
chart2.render();
chart3.render();
chart4.render();
chart5.render();
chart6.render();
chart7.render();

const getData = () => {
    console.log("This script is running")
}
window.onload(getData())