$(document).ready(function() {

  // product page
   $('.product-for').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: '.product-to'
  });
  $('.product-to').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    asNavFor: '.product-for',
    dots: false, 
    arrows: false,
    focusOnSelect: true
  });
  $('.slide-5').slick({
    infinite: true,
    slidesToShow: 4,
    slidesToScroll: 1,
    infinite: true,
    speed: 300 ,

    responsive: [
    {
      breakpoint: 1300,
      settings: {
        slidesToShow: 3,
      }
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 2,
      }
    },
    {
      breakpoint: 481,
      settings: {
        slidesToShow: 1,
      }
    }   
  ]   
  });
  $('.innerpage-slide').slick({
    infinite: true,
    slidesToShow: 4,
    slidesToScroll: 1,
    infinite: true,
    dots: true,
    arrows: false,
    speed: 300 ,
    responsive: [
        {
          breakpoint: 1441,
          settings: {
            slidesToShow: 3,
          }
        },
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 2,
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 1,
          }
        }   
    ]
         
  });
  $('.ecompro-slide').slick({
    infinite: true,
    slidesToShow: 4,
    slidesToScroll: 1,
    infinite: true,      
    speed: 300 ,
    responsive: [
      {
        breakpoint: 1441,
        settings: {
          slidesToShow: 3,
        }
      },       
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 2,
        }
      },
      {
        breakpoint: 481,
        settings: {
          slidesToShow: 1,
        }
      }   
    ]
  });
});