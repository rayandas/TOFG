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
