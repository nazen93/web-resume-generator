from django.shortcuts import render
from django.http import HttpResponse

from .forms import ResumeForm
from .generator import resume_generator
# Create your views here.

def index(request):	
	if request.method == "POST":
		form = ResumeForm(request.POST)
		if form.is_valid():
			name = request.POST.get('name', '')
			mail = request.POST.get('mail', '')
			address = request.POST.get('address', '')
			contact = '%s \n %s' % (address, mail)
			carrer_objective = request.POST.get('carrer_objective', '')
			skills = request.POST.get('skills', '')
			company_name = request.POST.get('company_name', '')
			company_experience = request.POST.get('company_experience', '')
			working_period = request.POST.get('working_period', '')
			experience_dict = {
				'comapny': company_name,
				'description': company_experience,
				'date': working_period
				}
			resume_generator(name, contact, carrer_objective, skills, experience_dict)
			return HttpResponse('prawilnie ziomus')
	else:
		form = ResumeForm()
	
	context = {'form': ResumeForm}
	
	return render(request, 'generator/index.html', context)
