from django import forms
from .models import Employee


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
         model = Employee
         fields = ['full_name', 'image', 'email', 'password', 'address','phone',]

class EmployeeListForm(forms.ModelForm):
    class Meta:
         model = Employee
         fields = ['id','full_name', 'image', 'email', 'password', 'address','phone',]
   