from docxtpl import DocxTemplate, Listing

def resume_generator(name, address, carrer_objective, skills, experience_array, education_array):
    skills = skills.split(',')
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
    doc.save('C:/Users/ADMIN/Desktop/test/kekorino.docx')
