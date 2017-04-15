from docxtpl import DocxTemplate, Listing

def resume_generator(name, address, carrer_objective, skills, experience_dict):
    skills = skills.split(',')
    doc = DocxTemplate('C:/Users/ADMIN/Desktop/test/test.docx')
    context = {'name': name,
               'address': address,
               'carrer_objective': carrer_objective,
               'skills': skills,
               'experiences' : [{'job' : 'Python developer',
                                 'company' : experience_dict['comapny'],
                                 'date' : experience_dict['date'],
                                 'description' : experience_dict['description']},
                                {'job' : 'Python developer',
                                 'company' : 'Januszsoft',
                                 'date' : '03.2016-06.2016',
                                 'description' : 'I like train'}],
               'education' : [{'degree' : 'kozak',
                               'name' : 'SP11',
                               'date' : '2015-2017'}],
               'informations' : ["Drivers license", "uber hacker"]
               }
    doc.render(context)
    doc.save('C:/Users/ADMIN/Desktop/test/kekorino.docx')
