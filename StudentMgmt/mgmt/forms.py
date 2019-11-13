from django.contrib.auth.model import user
from django import forms
from .models import Faculty,Staff,Parent
from django.core.urlresolvers import reverse
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields =  ['Username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_faculty', 'is_staff', 'is_parent']

class FacultyForm(forms.ModelForm):
    
    class Meta:
    model = Faculty
    fields = ['photo', 'department']

class StaffForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields = ['photo','department']    

class ParentForm(forms.ModelForm):

    class Meta:
        model = Parent
        fields = ['photo','child_name', 'child-department']        
