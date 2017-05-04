$('.next-step').click(function(){
  var next_tab = $('.nav-pills > .active').next('li');
  var progress_bar = $('.progress-bar')[0];
  var progress_bar_class = $(progress_bar).attr('class');
  var progress_bar_value = $(progress_bar).attr('aria-valuenow');
  var progress_int_value = parseInt(progress_bar_value) + 33;
  
  $(progress_bar).attr('aria-valuenow', progress_int_value);
  $(progress_bar).html(progress_int_value + '% completed' );
  $(progress_bar).width(progress_int_value+'%');
  
  new_bar(progress_bar, progress_bar_class);
  
  $(next_tab).find('a').attr('data-toggle', 'tab');
  $(next_tab).find('a').trigger('click');
  $(next_tab).removeClass('disabled');
});

$('.btn-danger').click(function(){
	  $('.nav-pills > .active').prev('li').find('a').trigger('click');
});

function new_bar(object, bar_class){
	$(object).removeClass(bar_class);
	if (bar_class.includes('danger')){
		$(object).addClass('progress-bar progress-bar-warning progress-bar-striped active');
	}
	else if (bar_class.includes('warning')){
		$(object).addClass('progress-bar progress-bar-info progress-bar-striped active');
	}
	else if (bar_class.includes('info')){
		$(object).addClass('progress-bar progess-bar-success progress-bar-striped active');
	}
}