$(document).ready(function(){

	var progress_bar = $('.progress-bar')[0];
	
	$('.next-step').click(function(){
		var next_tab = $('.nav-pills > .active').next('li');
		var progress_bar_class = $(progress_bar).attr('class');
		var progress_bar_value = $(progress_bar).attr('aria-valuenow');
		var progress_int_value = parseInt(progress_bar_value) + 33;
	  
		/* Checks if the progress bar's value is not over 100 */
		if (progress_int_value <= 100){
		/* Adds new value to the argument aria-valuenow, changes the inner HTML and the width of the progress bar  */
		  $(progress_bar).attr('aria-valuenow', progress_int_value);
		  $(progress_bar).html(progress_int_value + '% completed' );
		  $(progress_bar).width(progress_int_value+'%');
	  
		  new_bar(progress_bar, progress_bar_class, progress_int_value);
		};
	  
	  /* Redirects to another tab, adds data-toggle argument and removes class disabled */
		$(next_tab).find('a').attr('data-toggle', 'tab');
		$(next_tab).find('a').trigger('click');
		$(next_tab).removeClass('disabled');
		});
	
	$('.previous-step').click(function(){
		var progress_bar_class = $(progress_bar).attr('class');
		var progress_bar_value = $(progress_bar).attr('aria-valuenow');
		var progress_int_value = parseInt(progress_bar_value) - 33;
		
		if (progress_int_value >= 0){
			$(progress_bar).attr('aria-valuenow', progress_int_value);
		$(progress_bar).html(progress_int_value + '% completed' );
		$(progress_bar).width(progress_int_value+'%');
		
		new_bar(progress_bar, progress_bar_class, progress_int_value)
		};
		
		$('.nav-pills > .active').prev('li').find('a').trigger('click');
	});

	function new_bar(object, bar_class, value){
		/* Takes progress bar, current progress bar class and it's value as an arguments, 
		removes the current class and adds the new one accordingly to the value of the bar */
		$(object).removeClass(bar_class);
		if (value == 33){
			$(object).addClass('progress-bar progress-bar-warning progress-bar-striped active');
		}
		else if (value == 66){
			$(object).addClass('progress-bar progress-bar-info progress-bar-striped active');
		}
		else if (value == 99){
			$(object).addClass('progress-bar progess-bar-success progress-bar-striped active');
		}
	};
});