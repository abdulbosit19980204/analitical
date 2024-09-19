var themeprimary = localStorage.getItem("themeprimary") || '#1a7cbc';
var themesecondary = localStorage.getItem("themesecondary") || '#f07521';
var themesuccess = localStorage.getItem("themesuccess") || '#83C31B';
var themeinfo = localStorage.getItem("themeinfo") || '#18a0fb';
var themewarning = localStorage.getItem("themewarning") || '#FFC261';


window.Codexdmeki = {
	themeprimary: themeprimary,
	themesecondary: themesecondary,
	themesuccess: themesuccess,
	themeinfo: themeinfo,
	themewarning: themewarning,
};




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
$('.themecolor-list').on( 'click', '.color1', function() {   
  $("#customstyle" ).attr("href", "../assets/css/style.css" );
  return false;
});
$('.themecolor-list').on( 'click', '.color2', function() {   
  $("#customstyle" ).attr("href", "../assets/css/color2.css" );
  return false;
});
$('.themecolor-list').on( 'click', '.color3', function() {   
  $("#customstyle" ).attr("href", "../assets/css/color3.css" );
  return false;
});
$('.themecolor-list').on( 'click', '.color4', function() {   
  $("#customstyle" ).attr("href", "../assets/css/color4.css" );
  return false;
});
$('.themecolor-list').on( 'click', '.color5', function() {   
  $("#customstyle" ).attr("href", "../assets/css/color5.css" );
  return false;
});
$('.themecolor-list').on( 'click', '.color6', function() {   
  $("#customstyle" ).attr("href", "../assets/css/color6.css" );
  return false;
});