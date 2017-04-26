def formset_data(formset, **kwargs):
    """
    Takes formset and relevant keyword arguments and creates dictionaries that are appended to data_array
    """
    data_array = []
    for form in formset:
        form_data = form.cleaned_data 
        name = form_data.get(kwargs['name'], '')
        start_date = form_data.get(kwargs['start_date'], '')
        end_date = form_data.get(kwargs['end_date'], '')
        startend_period = '%s to %s' % (start_date, end_date)
        if 'experience' in kwargs: #determines which formset was given
            experience = form_data.get(kwargs['experience'], '')
            job_title = form_data.get(kwargs['title'], '')
            formdata_dict = {
                'job_title': job_title,
                'company': name,
                'description': experience,
                'date': startend_period
                }
        else:
            school_type = form_data.get(kwargs['type'], '')
            formdata_dict = {
                'type': school_type,
                'school_name': name,
                'date': startend_period
                }
            print(formdata_dict)
            
        data_array.append(formdata_dict)

    return data_array
