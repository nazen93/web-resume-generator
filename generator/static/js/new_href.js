/* Gets the index value of the current carousel slide and replaces the href with it */
$(document).ready(function(){
	$('#myCarousel').on('slide.bs.carousel', function(e) {
	  var active = $(e.target).find('.carousel-inner > .item.active');
	  var current_href = $('#select-template').attr('href');
	  var current_index = $('div.active').index() + 1;
	  var new_href = current_href.replace(/[0-9]/, current_index);
	  $('#select-template').attr('href', new_href);
	});
});
