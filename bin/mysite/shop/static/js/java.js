$(document).ready(function () {
    size_li = $(".my_list_magazins").size();
    x=10;
    $('.my_list_magazins li:lt('+x+')').show();
    $('#loadMore').click(function () {
        x= (x+5 <= size_li) ? x+5 : size_li;
        $('.my_list_magazins li:lt('+x+')').show();
        $('#showLess').show();
        $('#loadMore').hide();
        if(x == size_li){
            $('#loadMore').hide();
        }
    });
    $('#showLess').click(function () {
        x=(x-5<0) ? 2 : x-5;
        $('.my_list_magazins li').not(':lt('+x+')').hide();
        $('#loadMore').show();
        $('#showLess').show();
        if(x == 2){
            $('#showLess').hide();
        }
    });
});

$(document).ready(function($) {
        
      var allPanels = $('.details > dd').hide();
        
      $('.details > dt > a').click(function() {
        allPanels.slideUp();
        $(this).parent().next().slideDown();
        return false;
      });

    })(jQuery);