from django import forms
from .models import Taks
class TaskForm(forms.ModelForm):
	class Meta:
		model =  Taks
		fields = ['title','description','important']
		widgets = {
			'title' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Escribe un titulo'}),
			'description' : forms.Textarea(attrs={'class': 'form-control','placeholder':'Escribe una descripcion'}),
			'important' : forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),

		}