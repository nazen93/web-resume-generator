import mimetypes
import os

from wsgiref.util import FileWrapper
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.forms.formsets import formset_factory
from django.utils.encoding import smart_str
from django.urls import reverse

from .forms import BasicInformationsForm, ExperienceInformationsForm, EducationInformationsForm, AdditionaInformationsForm
from .generator import resume_generator
from .data_function import formset_data

def index(request):	
	experience_formset = formset_factory(ExperienceInformationsForm)
	education_formset = formset_factory(EducationInformationsForm)
	if request.method == "POST":
		basic_information_form = BasicInformationsForm(request.POST)
		experience_forms = experience_formset(request.POST, prefix='experience')
		education_forms = education_formset(request.POST, prefix='education')
		additional_informations_form = AdditionaInformationsForm(request.POST)
		if basic_information_form.is_valid() and experience_forms.is_valid() and education_forms.is_valid() and additional_informations_form.is_valid():
			name = request.POST.get('name', '')
			mail = request.POST.get('mail', '')
			address = request.POST.get('address', '')
			contact = '%s \n %s' % (address, mail)
			carrer_objective = request.POST.get('carrer_objective', '')
			skills = request.POST.get('skills', '')
			additional_informations = request.POST.get('informations', '')
			
			experience_kwargs = {'title': 'job_title',
								'name': 'company_name',
								'experience': 'company_experience',
								'start_date': 'start_date',
								'end_date': 'end_date'}
			
			education_kwargs = {'name': 'school_name',
								'type': 'school_type',
								'start_date': 'enrollment_date',
								'end_date': 'graduation_date'}
			
			experience_array = formset_data(experience_forms, **experience_kwargs)			
			education_array = formset_data(education_forms, **education_kwargs)
			
			file_path = resume_generator('resume_template1', name, contact, carrer_objective, skills, experience_array, education_array, additional_informations) #generates the resume with the given informations and returns a path to the created file
			request.session['path'] = file_path
			
			return redirect('success')
		
	else:
		basic_information_form = BasicInformationsForm()
		experience_forms = experience_formset(prefix='experience')
		education_forms = education_formset(prefix='education')
		additional_informations_form = AdditionaInformationsForm()
	
	context = {'basic_form': basic_information_form,
			'experience_formset': experience_forms,
			'education_formset': education_forms,
			'additional_informations': additional_informations_form}
	
	return render(request, 'generator/generator.html', context)

def success(request):
	if request.method == 'POST':
		if 'path' in request.session:
			file_path = request.session['path']
			filename = os.path.basename(file_path)
			chunk_size = 8192
			response = StreamingHttpResponse(FileWrapper(open(file_path, 'rb'), chunk_size),
					                           content_type=mimetypes.guess_type(file_path)[0])
			response['Content-Length'] = os.path.getsize(file_path)    
			response['Content-Disposition'] = "attachment; filename=%s" % filename
			return response
		
	return render(request, 'generator/success.html')
