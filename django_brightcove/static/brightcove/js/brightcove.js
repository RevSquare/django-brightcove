/* Compatibility with Grappelli */
// grp jQuery namespace
var grp = grp || {
    "jQuery": jQuery.noConflict(true)
};

(function ($) {
    var Brightcove = {
        init: function () {
            $('.brightcove_widget_refresh').on("click", function(e){
                var that = this;
                $(that).find('.fa').addClass('fa-spin');
                $('.brightcove_widget select').load($(this).attr('href'), function () {
                    $(that).find('.fa').removeClass('fa-spin');
                });
                e.preventDefault();
            });
        }
    };
    
    $(function () {
        Brightcove.init();
    });
}(grp.jQuery));
