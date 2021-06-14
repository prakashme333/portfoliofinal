$(document).ready(function(){
  $(window).scroll(function(){
     if(this.scrollY>20){
         $('.navbar').addClass("sticky");
     }else{
      $('.navbar').removeClass("sticky");
     }
     if(this.scrollY>50){
        $('.scroll-up-btn').addClass("show");
     }else{
        $('.scroll-up-btn').removeClass('show');
     }
  }) 
//slide up action
$('.scroll-up-btn').click(function(){
   $('html').animate({scrollTop: 0});
   // removing smooth scroll on slide-up button click
   $('html').css("scrollBehavior", "auto");
});


// toggle menu/navbar script
  $('.menu-btn').click(function(){
   $('.navbar .menu').toggleClass("active");
   $('.menu-btn i').toggleClass("active");
}); 
});