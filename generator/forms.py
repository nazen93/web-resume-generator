from django.shortcuts import render
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# Create your views here.

class BasicInformationsForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
	address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your address'}))
	mail = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter your e-mail'}))
	carrer_objective = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your carrer objective'}))
	skills = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter you skills'}))

	
class ExperienceInformationsForm(forms.Form):
	job_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter your position's title"}))
	company_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter your employer's name"}))
	company_experience = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your duties'}))
	start_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Enter your working period',
																'class': 'datepicker'}))
	end_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Enter your working period',
																'class': 'datepicker'}))
	
	def clean(self):
		cleaned_data = super(ExperienceInformationsForm, self).clean()
		start_date = cleaned_data.get('start_date')
		end_date = cleaned_data.get('end_date')
		if start_date > end_date:
			msg = 'Start date cannot be bigger than the end date'
			self.add_error('start_date', msg)


class EducationInformationsForm(forms.Form):
	schools = [('highschool', 'Highschool'), ('college', 'College')]
	school_type = forms.CharField(widget=forms.Select(choices=schools))
	school_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter your school's name"}))
	enrollment_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': "Enter your enrollment date",
																'class': 'datepicker'}))
	graduation_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': "Enter your graduation's date",
																'class': 'datepicker'}))
	
	def clean(self):
		cleaned_data = super(EducationInformationsForm, self).clean()
		enrollment_date = cleaned_data.get('enrollment_date')
		graduation_date = cleaned_data.get('graduation_date')
		if enrollment_date > graduation_date:
			msg = 'Enrollment date cannot be bigger than graduation date'
			self.add_error('enrollment_date', msg)

	
class AdditionaInformationsForm(forms.Form):
	informations = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter any additional informations'}))