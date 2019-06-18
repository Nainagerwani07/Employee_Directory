from django import forms
from .models import Employee_dir

class Employee_dir_data(forms.ModelForm):
	class Meta:
		model=Employee_dir
		fields='__all__'