//** bar chart **// 
var ctx = document.getElementById('barchart');
new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Vote A', 'Vote B', 'Vote C', 'Vote D', 'Vote E'],
    datasets: [{
      label: '# of Votes',
      data: [65, 59, 80, 81, 56],
      borderWidth: 2,
      backgroundColor:[Codexdmeki.themeprimary,Codexdmeki.themesecondary,Codexdmeki.themesuccess,Codexdmeki.themeinfo,Codexdmeki.themedanger],
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});




//** bubble chart **// 
var ctx = document.getElementById('bubblechart');
new Chart(ctx, {
  type: 'bubble',
  pointStyle: 'cross',
  data: {
    labels: ['Vote A', 'Vote B', 'Vote C', 'Vote D', 'Vote E'],
    datasets: [{
      label: 'value a',
      data: [
        {
          x: 20,
          y: 30,
          r: 15
        },
        {
          x: 40,
          y: 10,
          r: 10
        }
      ],
      borderWidth: 2,
      backgroundColor:[Codexdmeki.themeprimary,Codexdmeki.themesecondary],
    }]
  },
   
});



//** doughnu chart **// 
var ctx = document.getElementById('doughnutchart');
new Chart(ctx, {
  type: 'doughnut',
  data: {   
    datasets: [{
      label: 'Votes',
      data: [50,80,90,50,60],
      borderWidth: 2,
      backgroundColor:[
        Codexdmeki.themeprimary, 
        Codexdmeki.themesecondary, 
        Codexdmeki.themesuccess, 
        Codexdmeki.themeinfo,
        Codexdmeki.themewarning, 
        Codexdmeki.themedanger],
    }]
  } 
});


//** pie chart **// 
var ctx = document.getElementById('piechart');
new Chart(ctx, {
  type: 'pie',
  data: {   
    datasets: [{
      label: 'Votes',
      data: [50,80,90,50,60],
      borderWidth: 2,
      backgroundColor:[
        Codexdmeki.themeprimary, 
        Codexdmeki.themesecondary, 
        Codexdmeki.themesuccess, 
        Codexdmeki.themeinfo,
        Codexdmeki.themewarning, 
        Codexdmeki.themedanger],
    }]
  } 
});



//** line chart **// 
var ctx = document.getElementById('linechart');
new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Vote A', 'Vote B', 'Vote C', 'Vote D', 'Vote E'],
    datasets: [{      
      label: '# of Votes',
      data: [65, 59, 80, 81, 56, 55, 40],     
      fill: false,     
      tension: 0.1,
      borderColor:[Codexdmeki.themeprimary],
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});


//** mix chart **// 
var ctx = document.getElementById("mixchart");
var chart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: ['January','February','March','April'],
    datasets: [
      {
        label: "value A",
        type: "bar",
        data: [65, 59, 80, 81, 56, 55, 40],
        backgroundColor: 'rgba(8, 155, 171, 0.2)',
        borderColor:[Codexdmeki.themeprimary],
        borderWidth: 2,
      },
      {
        label: "value B",
        data: [25, 13, 30, 35, 25, 40],
        type: "line",  
        backgroundColor: 'rgba(255, 94, 93, 0.2)',
        borderColor:[Codexdmeki.themesecondary],     
        lineTension: 0,
        fill: true
      }
    ]
  }
});






//** Polar area chart **// 
var ctx = document.getElementById('polarchart');
new Chart(ctx, {
  type: 'polarArea',
  data: {   
    datasets: [{
      label: '# of Votes',
      data: [65, 59, 80, 81, 56],
      borderWidth: 2,
      backgroundColor:[Codexdmeki.themeprimary,Codexdmeki.themesecondary,Codexdmeki.themesuccess,Codexdmeki.themeinfo,Codexdmeki.themedanger],
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});



//** Radar Chart **// 
var ctx = document.getElementById('radarchart');
new Chart(ctx, {
  type: 'radar',
  data: {
    labels: [
    'Eating',
    'Drinking',
    'Sleeping',
    'Designing',
    'Coding',
    'Cycling',
    'Running'
  ],
    datasets: [
      {
        data: [65, 59, 90, 81, 56, 55, 40],
        fill: true,
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgb(255, 99, 132)',
        pointBackgroundColor: 'rgb(255, 99, 132)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgb(255, 99, 132)'
      },
      {
        label: 'My Second Dataset',
        data: [28, 48, 40, 19, 96, 27, 100],
        fill: true,
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgb(54, 162, 235)',
        pointBackgroundColor: 'rgb(54, 162, 235)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgb(54, 162, 235)'
      }
    ]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});



//** Scatter chart **// 
var ctx = document.getElementById('scatterchart');
new Chart(ctx, {
  type: 'scatter',
  data: {
    labels: ['Vote A', 'Vote B', 'Vote C', 'Vote D', 'Vote E'],
    datasets: [{
      label: '# of Votes',
        data: [
        {
          x: -10,
          y: 0
        }, {
          x: 0,
          y: 10
        }, {
          x: 10,
          y: 5
        }, {
          x: 0.5,
          y: 5.5
        }
        ],
      fill: false,
      backgroundColor: Codexdmeki.themeprimary,
      borderColor: 'rgb(0, 0, 0,0)',      
    }
    ]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});