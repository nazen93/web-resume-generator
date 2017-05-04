from django.conf import settings
from docxtpl import DocxTemplate, Listing

def resume_generator(template_name, name, address, carrer_objective, skills, experience_array, education_array, additional_informations):
    """
    Takes template name (.docx template) and all submitted POST data, creates a dictionary out of the given arguments, renders the data on .docx template and returns the path to the generate file
    """
    skills = skills.split(',')
    if additional_informations:
        extra_informations = additional_informations.split(',')
    else:
        extra_informations = None
    template_path = settings.MEDIA_ROOT+'/'+template_name+'.docx'
    doc = DocxTemplate(template_path)
    context = {'name': name,
               'address': address,
               'carrer_objective': carrer_objective,
               'skills': skills,
               'experiences' : experience_array,
               'education' : education_array,
               'informations' : extra_informations
               }
    doc.render(context)
    file_path = settings.MEDIA_ROOT+'/'+name+'.docx'
    doc.save(file_path)
    return file_path