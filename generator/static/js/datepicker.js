/* Adds datepicker to the date field */
$(document).ready(function(){
	$('#experience-form').delegate('.datepicker', 'focus', function() {
	    $(this).datepicker();
	});
	
	$('#education-form').delegate('.datepicker', 'focus', function() {
	    $(this).datepicker();
	});
});