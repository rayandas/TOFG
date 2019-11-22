from django.contrib.auth.models import User
from django import forms
from .models import Faculty,Parent
from django.urls import reverse
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields =  ['Username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class FacultyForm(forms.ModelForm):
    
    class Meta:
        model = Faculty
        fields = ['photo', 'department']
'''
class StaffForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields = ['photo','department']    
'''
class ParentForm(forms.ModelForm):

    class Meta:
        model = Parent
        fields = ['photo','department']   

class StudentForm(forms.ModelForm):

    DOB = forms.DateField(widget=forms.SelectDateWidget(years=[i for i in range(1920,2010)]),input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y','%d/%m/%y'])

    class Meta:
        model = Student
        fields = ['photo','DOB','branch','year','tenth_marks','inter_marks','current_marks']




