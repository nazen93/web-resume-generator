var add_another_job = document.getElementById('add-experience');
var add_another_school = document.getElementById('add-school');

var experience_form_amount = document.getElementById('id_experience-TOTAL_FORMS');
var experience_base_form = document.getElementById('experience-form');
var experience_base_HTML = name(experience_base_form.innerHTML, '0', '{arg}');

var education_form_amount = document.getElementById('id_education-TOTAL_FORMS');
var education_base_form = document.getElementById('education-form');
var education_base_HTML = name(education_base_form.innerHTML, '0', '{arg}');

add_another_job.addEventListener('click', function(){
	new_fields(experience_form_amount, experience_base_form, experience_base_HTML)
})

add_another_school.addEventListener('click', function(){
	new_fields(education_form_amount, education_base_form, education_base_HTML)
})


function new_fields(form_amount, base_form, base_HTML){
	var new_form_amount = parseInt(form_amount.value) + 1;
	var new_form = name(base_HTML, '{arg}', form_amount.value);
	form_amount.value = new_form_amount;
	base_form.insertAdjacentHTML('beforeend', new_form);
};

function name(str, replaceWhat, replaceTo){
    var re = new RegExp(replaceWhat, 'g');
    var new_string = str.replace(re, replaceTo);
	return new_string;
};

