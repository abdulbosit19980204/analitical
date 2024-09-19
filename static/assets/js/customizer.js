// Customizer
$("body").append('<div class="customizer-layer"></div><div class="customizer-action"><i data-feather="settings"></i></div><div class="theme-cutomizer"> <div class="customizer-header"> <h4>Theme Setting</h4> <div class="close-customizer"><i data-feather="x"></i></div></div><div class="customizer-body"> <div class="cutomize-group"> <h6 class="customizer-title">Theme Color</h6> <ul class="customizeoption-list themecolor-list"> <li class="color1"></li><li class="color2"></li><li class="color3"></li><li class="color4"></li><li class="color5"></li><li class="color6"></li></ul> </div><div class="cutomize-group"> <h6 class="customizer-title">Sidebar Mode</h6> <ul class="customizeoption-list sidebaroption-list"> <li class="sidebarlight-action">light</li><li class="sidebardark-action">dark</li><li class="sidebargradient-action">gradient</li></ul> </div><div class="cutomize-group"> <h6 class="customizer-title">Layout Direction</h6> <ul class="customizeoption-list"> <li class="ltr-action">ltr</li><li class="rtl-action">rtl</li></ul> </div><div class="cutomize-group mb-0"> <h6 class="customizer-title">Layout mode</h6> <ul class="customizeoption-list"> <li class="light-action">light</li><li class="dark-action">dark </li></ul> </div></div></div>');


//*** Light & Dark action  ***//
$('.action-dark').click(function(){   
	$(this).toggleClass('action-light');
	$('.icon-dark').toggle('');
	$('.icon-light').toggle('');
	$('body').toggleClass('darkmode');
});


//*** Customizer Action ***//
$('.customizer-action').click(function(){
	$('.theme-cutomizer , .customizer-layer').toggleClass('active');
});

$('.customizer-header').click(function(){
	$('.theme-cutomizer , .customizer-layer').toggleClass('active');
});

$('.customizer-layer').click(function(){
	$(this).removeClass('active');
	$('.theme-cutomizer').removeClass('active');
});

//*** Dark Mode ***//
$('.dark-action').click(function(){
	$('body').addClass('darkmode');
});

$('.light-action').click(function(){
	$('body').removeClass('darkmode');
});

$('.customizeoption-list li').click(function(){
	$(this).addClass('active-mode')
	$(this).siblings().removeClass('active-mode');
});


//*** Direction Mode ***//
$('.ltr-action').click(function(){
	$('body').removeClass('rtlmode');
});
$('.rtl-action').click(function(){
	$('body').addClass('rtlmode');
});


//*** Sidebar Mode ***//
$('.sidebardark-action').click(function(){
	$('.codex-sidebar').addClass('sidebar-dark');
	$('.codex-sidebar').removeClass('sidebar-gradient');
});
$('.sidebarlight-action').click(function(){
	$('.codex-sidebar').removeClass('sidebar-dark');
	$('.codex-sidebar').removeClass('sidebar-gradient');
});
$('.sidebargradient-action').click(function(){
	$('.codex-sidebar').addClass('sidebar-gradient');
});


//** Theme color mode  ***//
$('.themecolor-list').on('click','.color1', function() {   
  $("#customstyle" ).attr("href", "../assets/css/style.css" );
  return false;
});
$('.themecolor-list').on('click','.color2', function() {   
  $("#customstyle" ).attr("href", "../assets/css/color2.css" );
  return false;
});
$('.themecolor-list').on('click','.color3', function() {   
  $("#customstyle" ).attr("href", "../assets/css/color3.css" );
  return false;
});
$('.themecolor-list').on('click','.color4', function() {   
  $("#customstyle" ).attr("href", "../assets/css/color4.css" );
  return false;
});
$('.themecolor-list').on('click','.color5', function() {   
  $("#customstyle" ).attr("href", "../assets/css/color5.css" );
  return false;
});
$('.themecolor-list').on('click','.color6', function() {   
  $("#customstyle" ).attr("href", "../assets/css/color6.css" );
  return false;
});