
//** line chart **//
new Morris.Line({ 
  element: 'morrisline',
  data: [
    { year: '2015', value1: 10 , value2: 5},
    { year: '2016', value1: 30 , value2: 20},
    { year: '2017', value1: 15 , value2: 30},
    { year: '2018', value1: 20 , value2: 15},
    { year: '2019', value1: 35 , value2: 20}
  ],
  lineColors:[Codexdmeki.themeprimary,Codexdmeki.themesecondary],
  xkey: 'year',
  ykeys: ['value1','value2'], 
  labels: ['Series a','Series b']
});


//** area chart **//
Morris.Area({
  element: 'morrisarea',
  data: [
    { y: '2006', valuea: 50, valueb: 90 },
    { y: '2007', valuea: 60,  valueb: 65 },
    { y: '2008', valuea: 80,  valueb: 40 },
    { y: '2009', valuea: 40,  valueb: 65 },
    { y: '2010', valuea: 80,  valueb: 40 },
    { y: '2011', valuea: 20,  valueb: 65 },
    { y: '2012', valuea: 90, valueb: 90 }
  ], 
  lineColors:[Codexdmeki.themeprimary,Codexdmeki.themesecondary],
  xkey: 'y',
  ykeys: ['valuea', 'valueb'],
  labels: ['Series A', 'Series B']
});


//** bar chart **//
Morris.Bar({
  element: 'morrisbar',
  data: [
    { y: '2015', valuea: 100, valueb: 90 },
    { y: '2016', valuea: 75,  valueb: 65 },
    { y: '2017', valuea: 50,  valueb: 40 },
    { y: '2018', valuea: 75,  valueb: 65 },
    { y: '2019', valuea: 50,  valueb: 40 },
    { y: '2020', valuea: 75,  valueb: 65 },
    { y: '2021', valuea: 100, valueb: 90 }
  ],
  barColors:[Codexdmeki.themeprimary,Codexdmeki.themesecondary],
  xkey: 'y',
  ykeys: ['valuea', 'valueb'],
  labels: ['Series A', 'Series B']
});


//** stacked bar chart **//
Morris.Bar({
  element: 'morrisbarstacked',
  data: [
    { y: '2015', valuea: 100, valueb: 90 },
    { y: '2016', valuea: 75,  valueb: 65 },
    { y: '2017', valuea: 50,  valueb: 40 },
    { y: '2018', valuea: 75,  valueb: 65 },
    { y: '2019', valuea: 50,  valueb: 40 },
    { y: '2020', valuea: 75,  valueb: 65 },
    { y: '2021', valuea: 100, valueb: 90 }
  ],
  barColors:[Codexdmeki.themeprimary,Codexdmeki.themesecondary],
  stacked:true,
  barSize:30,
  xkey: 'y',
  ykeys: ['valuea', 'valueb'],
  labels: ['Series A', 'Series B']
});



//** donut chart **//
Morris.Donut({
  element: 'morrisdonut',
  data: [
    {label: "value a", value: 20},
    {label: "value b", value: 30},
    {label: "value c", value: 40},
    {label: "value d", value: 50}
  ],
  colors:[Codexdmeki.themeprimary,Codexdmeki.themesecondary,Codexdmeki.themewarning,Codexdmeki.themeinfo]
});
