from django import forms
from django.db import models
from django.forms.widgets import NumberInput
class Form1(forms.Form):
	name = forms.CharField()
	comment = forms.CharField(widget=forms.Textarea)
	email = forms.EmailField()
	agree = forms.BooleanField()
	# date = forms.DateField(forms.widgets=(attrs={'type':'date'}))
	birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
	time=forms.DateTimeField(widget=NumberInput(attrs={'type': 'time'}))
	rating = forms.ChoiceField(widget=forms.RadioSelect, choices={(1,1),(2,2),(3,3),(4,4),(5,5)})
	

class model1(models.Model):
     id = models.AutoField(primary_key=True)