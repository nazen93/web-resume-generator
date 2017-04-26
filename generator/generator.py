from django.conf import settings
from docxtpl import DocxTemplate, Listing

def resume_generator(template_name, name, address, carrer_objective, skills, experience_array, education_array):
    skills = skills.split(',')
    template_path = settings.MEDIA_ROOT+'/'+template_name+'.docx'
    doc = DocxTemplate('C:/Users/ADMIN/Desktop/test/test.docx')
    context = {'name': name,
               'address': address,
               'carrer_objective': carrer_objective,
               'skills': skills,
               'experiences' : experience_array,
               'education' : education_array,
               'informations' : ["Drivers license", "uber hacker"]
               }
    doc.render(context)
    doc.save(settings.MEDIA_ROOT+'/'+template_name+name+'.docx')
