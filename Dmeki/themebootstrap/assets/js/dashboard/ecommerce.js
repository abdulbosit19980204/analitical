 //*** over revenue start  ***//
 var options = {
  series: [{
    name: 'Income',
    type: 'column',
    data: [40, 50, 70, 90, 65, 50, 40,80,55,70,60,40],
  }, {
    name: 'Profit',
    type: 'area',
    data: [50, 30, 40, 55, 40, 25,55,20,30,60,30,40]
  }],
  chart: {
    height: 452,
    type: 'line',
    toolbar:{
      show: false
    },
  zoom: {
    enabled: false
  }
},
legend:{
  show:false
},
dataLabels: {
  enabled: false
},
stroke: {
  width: [0,0],
  curve: 'smooth',   
}, 
plotOptions: {
  bar: {       
      columnWidth:"20%",
      startingShape:"rounded",
      endingShape: "rounded",
  }
},
fill:{        
    opacity:[1, 0.08],     
      gradient:{
      type:"horizontal",       
      opacityFrom:0.5,
      opacityTo:0.1,
      stops: [100, 100, 100]       
    }
}, 
colors: [Codexdmeki.themeprimary],  
states: {
   normal: {
          filter: {
              type: 'darken',
              value: 1,
          }
      },
      hover: {
          filter: {
              type: 'darken',
              value: 1,
          }
      },
      active: {
          allowMultipleDataPointsSelection: false,
          filter: {
              type: 'darken',
              value: 1,
          }
      },
  },
grid:{
   strokeDashArray: 2,
},   

 yaxis:{     
    tickAmount: 10 ,
    min: 10.00 ,
    max: 80.00 ,

    labels:{
      formatter: function (y) {
          return  "$" + y.toFixed(0);
        },
      style: {
        colors: '#262626',
        fontSize: '14px',              
        fontWeight: 500, 
        fontFamily: 'Roboto, sans-serif'   
      }              
    },
},
xaxis: {
  categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct','Nov','Dece'],      
  axisTicks: {
    show:false
  },
  axisBorder:{
    show:false
  },
  labels:{
        style: {
            colors: '#262626',
            fontSize: '14px',              
            fontWeight: 500, 
            fontFamily: 'Roboto, sans-serif'                 
        },
    },
},
responsive:[
  {
    breakpoint: 1441,
      options:{
          chart:{
            height: 445
          }
      },
    },
    {
    breakpoint: 1366,
      options:{
          chart:{
            height: 320
          }
      },
    },
  ] 
};
var chart = new ApexCharts(document.querySelector("#over-revenue"), options);
chart.render();
//*** over revenue end  ***//
      

//*** Earning Revenue start  ***//
var options = {
series:[{
  name: 'Selling growth',
  data: [35,50,55,40,50,60,50,35,60,30,65,35],
}  
],
chart:{
  type: 'area',
  height: 430,
  stacked:true,
  toolbar:{
    show: false,
  },
},
  colors: [Codexdmeki.themeprimary,Codexdmeki.themesecondary],
  plotOptions: {
    bar:{        
      borderRadius: 5,
      horizontal: false,
      columnWidth: '35%',       
    },
  },
  dataLabels:{
    enabled:false
  },       
  legend:{
    show: false,
  },  
  stroke:{
    curve: 'smooth',
  },     
  grid:{
    strokeDashArray: 2,
  },
  xaxis: {
    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct','Nov','Dec'], 
    axisTicks: {
      show:false
    },
    axisBorder:{
      show:false
    },
    labels:{
        style: {
            colors: '#262626',
            fontSize: '14px',              
            fontWeight: 500, 
            fontFamily: 'Roboto, sans-serif'                 
        },
    },
  },
  yaxis:{
    axisTicks: {
      show:false
    },
    axisBorder:{
      show:false
    },  
    labels:{
      formatter: function (y) {
          return y.toFixed(0) + "k";
        },
        style: {
            colors: '#262626',
            fontSize: '14px',              
            fontWeight: 500, 
            fontFamily: 'Roboto, sans-serif'                 
        },
    },   
  },
  responsive:[
    {
      breakpoint:1366,
      options:{
        chart:{
          height: 320
        }
      },
    },
    {
      breakpoint:481,
      options:{
        chart:{
          height:290
        }
      },
    }      
  ]         
};
var chart = new ApexCharts(document.querySelector("#earning-revenue"), options);
chart.render();  
//*** Earning Revenue end  ***//


//*** sale by category start  ***//
var options = {
    labels: ['Panding','Delevered', 'Canceled', 'Returned'],
    series: [40, 35, 20, 50],
    chart: {
      type: 'donut',
      height: 345 ,
    },     
    states: {
          normal: {
              filter: {
                  type: 'darken',
                  value: 1,
              }
          },
          hover: {
              filter: {
                  type: 'darken',
                  value: 1,                   
              }
          },
          active: {
              allowMultipleDataPointsSelection: true,
              filter: {
                  type: 'darken',
                  value: 1,
              }
          },
      },
    plotOptions: {
      pie: {
        startAngle: -90,
        endAngle: 270
      },
    },
    stroke: {
      width: 0,
    },
    legend:{
      position:'bottom',       
      horizontalAlign: 'left', 
      offsetX: 0,
      offsetY: 0,
      colors: '#262626',
      fontSize: '14px',              
      fontWeight: 500, 
      fontFamily: 'Roboto, sans-serif',
      onItemClick: {
        toggleDataSeries: true
      },
      onItemHover: {
        highlightDataSeries: false
      },       
    },
    dataLabels: {
      enabled: false,
    },
  colors: [Codexdmeki.themeprimary,Codexdmeki.themesecondary,Codexdmeki.themeinfo,Codexdmeki.themewarning],
  responsive:[  
    {
      breakpoint:992,
      options:{
        chart:{
          height:350
        }
      },
    }

  ]
};
var chart = new ApexCharts(document.querySelector("#sale-category"), options);
chart.render();
//*** sale by category end ***//
