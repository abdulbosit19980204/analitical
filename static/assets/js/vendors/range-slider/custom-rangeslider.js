//*** Basic Range ***//
// $(".basic-range").ionRangeSlider();


$(".basic-range").ionRangeSlider({
        min: 100,
        max: 1000,
        from: 550
    });




//*** Min & Max  Range ***//
$(".minmax-range").ionRangeSlider({
       type: "double",
        grid: true,
        min: 0,
        max: 1000,
        from: 200,
        to: 800,       
   });





//*** Negetive Value Range ***//
 $(".negetive-valrange").ionRangeSlider({
        type: "double",
        grid: true,
        min: -1000,
        max: 1000,
        from: -500,
        to: 500
    });
    



//*** Negetive Stap Value Range ***//
 $(".negetivestap-valragne").ionRangeSlider({
    type: "double",
    grid: true,
    min: -12.8,
    max: 12.8,
    from: -3.2,
    to: 3.2,
    step: 0.1
});



//*** Custom  Range ***//
var customValrange = [0, 10, 100, 1000, 10000, 100000, 1000000];
var valFrom = customValrange.indexOf(10);
var valTo = customValrange.indexOf(10000);
$(".custom-valrange").ionRangeSlider({
    type: "double",
    grid: true,
    from: valFrom,
    to: valTo,
    values: customValrange
});




//*** Even String Range ***//
$(".evenstring-range").ionRangeSlider({
        grid: true,
        from: new Date().getMonth(),
        values: [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ]
  });