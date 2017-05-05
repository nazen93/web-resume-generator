/* Adds datepicker to the date field */
$('#experience-form').delegate('.datepicker', 'focus', function() {
    $(this).datepicker();
});

$('#education-form').delegate('.datepicker', 'focus', function() {
    $(this).datepicker();
});