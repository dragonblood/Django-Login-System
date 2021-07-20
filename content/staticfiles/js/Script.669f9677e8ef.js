

/* Please ❤ this if you like it! */


(function($) { "use strict";

	$(function() {
		var header = $(".start-style");
		$(window).scroll(function() {    
			var scroll = $(window).scrollTop();
		
			if (scroll >= 10) {
				header.removeClass('start-style').addClass("scroll-on");
			} else {
				header.removeClass("scroll-on").addClass('start-style');
			}
		});
	});		
		
	//Animation
	
	// $(document).ready(function() {
	// 	$('body.hero-anime').removeClass('hero-anime');
	// });

	//Menu On Hover
		
	$('body').on('mouseenter mouseleave','.nav-item',function(e){
			if ($(window).width() > 750) {
				var _d=$(e.target).closest('.nav-item');_d.addClass('show');
				setTimeout(function(){
				_d[_d.is(':hover')?'addClass':'removeClass']('show');
				},1);
			}
	});	
	
	//Switch light/dark
	
	$("#switch").on('click', function () {
		if ($("body").hasClass("dark")) {
			$("body").removeClass("dark");
			$("#switch").removeClass("switched");
		}
		else {
			$("body").addClass("dark");
			$("#switch").addClass("switched");
		}
	});  
	
  })(jQuery); 
  
$(document).on("submit", "#post-form", function(e) {
  e.preventDefault();
  $.ajax({
    type: "POST",
    url: "/atlus",
    data: {
      title: "vipul",
      info: $("#info").val(),
      csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      action: "post"
    },
    success: function(json) {
      document.getElementById("post-form").reset();
      $(".posts").prepend(
        '<div class="col-md-6">' +
          '<div class="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">' +
          '<div class="col p-4 d-flex flex-column position-static">' +
          '<h3 class="mb-0">' +
          json.title +
          "</h3>" +
          '<p class="mb-auto">' +
          json.info +
          "</p>" +
          "</div>" +
          "</div>" +
          "</div>"
      );
    },
    error: function(xhr, errmsg, err) {
      $("#results").html(
        "<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " +
          errmsg +
          " <a href='#' class='close'>&times;</a></div>"
      ); // add the error to the dom
      console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
  });
});
