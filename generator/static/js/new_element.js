document.addEventListener("DOMContentLoaded", function() {

	var add_another_job = document.getElementById('add-experience');
	var add_another_school = document.getElementById('add-school');
	
	/*  Gets the data about experience formset */
	var experience_form_amount = document.getElementById('id_experience-TOTAL_FORMS');
	var experience_base_form = document.getElementById('experience-form');
	var experience_base_HTML = name(experience_base_form.innerHTML, '0', '{arg}');
	
	/*  Gets the data about education formset */
	var education_form_amount = document.getElementById('id_education-TOTAL_FORMS');
	var education_base_form = document.getElementById('education-form');
	var education_base_HTML = name(education_base_form.innerHTML, '0', '{arg}');
	
	add_another_job.addEventListener('click', function(){
		new_fields(experience_form_amount, experience_base_form, experience_base_HTML)
	})
	
	add_another_school.addEventListener('click', function(){
		new_fields(education_form_amount, education_base_form, education_base_HTML)
	})
	
	
	function name(str, replaceWhat, replaceTo){
		/* Takes string/html object, string to be replaced and the value to what is should be changed as an arguments
		and retuns the new string */
	    var re = new RegExp(replaceWhat, 'g');
	    var new_string = str.replace(re, replaceTo);
		return new_string;
	};
	
	function new_fields(form_amount, base_form, base_HTML){
		/* Changes the value of TOTAL_FORMS, creates the new form and appends it to the end of the previous form */
		var new_form_amount = parseInt(form_amount.value) + 1;
		var new_form = name(base_HTML, '{arg}', form_amount.value);
		form_amount.value = new_form_amount;
		base_form.insertAdjacentHTML('beforeend', new_form);
	};

});

