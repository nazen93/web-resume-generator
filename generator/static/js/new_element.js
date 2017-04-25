var add_another = document.getElementsByClassName('more');
var wut = add_another[0];
var form_amount = document.getElementById('id_form-TOTAL_FORMS');
var base_form = document.getElementById('exp-form');
var base_HTML = name(base_form.innerHTML, '0', '{arg}');

wut.addEventListener('click', new_fields)

function new_fields(){
	var new_form_amount = parseInt(form_amount.value) + 1;
	var new_form = name(base_HTML, '{arg}', form_amount.value);
	form_amount.value = new_form_amount;
	base_form.innerHTML = base_form.innerHTML+new_form;	
};

function name(str, replaceWhat, replaceTo){
    var re = new RegExp(replaceWhat, 'g');
    var new_string = str.replace(re, replaceTo);
	return new_string;
};

$(function datepicker() {
	$('#exp-form').delegate('.datepicker', 'focus', function() {
		$(this).datepicker().triggerHandler("focus");
	});
  });

$('#exp-form').delegate('.datepicker', 'focus', function() {
    $(this).datepicker();
});