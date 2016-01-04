
	$(document).ready(function($) {
	    
	  var allPanels = $('.details > dd').hide();
	    
	  $('.details > dt > a').click(function() {
	    allPanels.slideUp();
	    $(this).parent().next().slideDown();
	    return false;
	  });

	})(jQuery);
