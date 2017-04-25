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
	
class EducationInformationsForm(forms.Form):
	schools = [('highschool', 'Highschool'), ('college', 'College')]
	school_type = forms.CharField(widget=forms.Select(choices=schools))
	school_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter your school's name"}))
	enrollment_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': "Enter your enrollment date",
																'class': 'datepicker'}))
	graduation_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': "Enter your graduation's date",
																'class': 'datepicker'}))
	