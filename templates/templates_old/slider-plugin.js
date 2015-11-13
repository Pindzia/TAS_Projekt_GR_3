// karuzela

$(function() {
	$.fn.carousel = function(options) {
		options = $.extend({
			display_li      : 3,
			animate_delay   : 700,
			pause_time      : 5000,
			auto            : true,
			onScroll        : function() {}
		}, options);

		return this.each(function() {
			var $t = $(this);

			var $ul = $('ul', this);
			var $li = $ul.find('li');
			var item_width = $li.first().outerWidth(true);
			var $prev = $t.find('.prev');
			var $next = $t.find('.next');
			var interval = null;

			var scrollPrev = function()
			{
				if (!$ul.is(':animated')) {
					var $li = $ul.find('li');
					$ul.css('margin-left',-item_width);
					$li.first().before($li.last());
					$ul.animate({'margin-left' : '0'}, options.animation_time, function(){
						options.onScroll();
					});
					clearInterval(interval);
					if (options.auto) interval = setTimeout(function() {scrollNext()}, options.pause_time);
				}
			}

			var scrollNext = function()
			{
				var $li = $ul.find('li');
				$ul.animate({'margin-left' : '-=' + item_width}, options.animation_time, function(){
					$li.last().after($li.first());
					$ul.css({'margin-left' : 0});
					options.onScroll();
				});
				clearInterval(interval);
				if (options.auto) interval = setTimeout(function() {scrollNext()}, options.pause_time);

			}					

			$prev.bind('click', scrollPrev);
			$next.bind('click', scrollNext);

			if (options.auto) interval = setTimeout(function() {scrollNext()}, options.pause_time);
		});
	}
});