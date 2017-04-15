from django.shortcuts import render
from django import forms

# Create your views here.

class ResumeForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
	address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your address'}))
	mail = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter your e-mail'}))
	carrer_objective = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your carrer objective'}))
	skills = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter you skills'}))
	company_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter your company's name"}))
	company_experience = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your duties'}))
	working_period = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Enter your working period'}))