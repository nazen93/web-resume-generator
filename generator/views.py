from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.forms.formsets import formset_factory
from .forms import BasicInformationsForm, ExperienceInformationsForm, EducationInformationsForm
from .generator import resume_generator
from .data_function import formset_data

def index(request):	
	print('luuul')
	print(settings.MEDIA_ROOT+'/'+'resume_template1.docx')
	experience_formset = formset_factory(ExperienceInformationsForm)
	education_formset = formset_factory(EducationInformationsForm)
	if request.method == "POST":
		basicinformation_form = BasicInformationsForm(request.POST)
		experience_forms = experience_formset(request.POST, prefix='experience')
		education_forms = education_formset(request.POST, prefix='education')
		if basicinformation_form.is_valid() and experience_forms.is_valid() and education_forms.is_valid():
			name = request.POST.get('name', '')
			mail = request.POST.get('mail', '')
			address = request.POST.get('address', '')
			contact = '%s \n %s' % (address, mail)
			carrer_objective = request.POST.get('carrer_objective', '')
			skills = request.POST.get('skills', '')
			
			experience_kwargs = {'title': 'job_title',
								'name': 'compoany_name',
								'experience': 'company_experience',
								'start_date': 'start_date',
								'end_date': 'end_date'}
			
			education_kwargs = {'name': 'school_name',
								'type': 'school_type',
								'start_date': 'enrollment_date',
								'end_date': 'graduation_date'}
			
			experience_array = formset_data(experience_forms, **experience_kwargs)			
			education_array = formset_data(education_forms, **education_kwargs)
			
			resume_generator('resume_template1', name, contact, carrer_objective, skills, experience_array, education_array)
			return HttpResponse("it's done!")
	else:
		basicinformation_form = BasicInformationsForm()
		experience_forms = experience_formset(prefix='experience')
		education_forms = education_formset(prefix='education')
	
	context = {'basic_form': basicinformation_form,
			'experience_formset': experience_forms,
			'education_formset': education_forms}
	
	return render(request, 'generator/index.html', context)
