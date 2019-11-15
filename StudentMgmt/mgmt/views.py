from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.urls import reverse,reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect,render_to_response
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.views.generic import DetailView, ListView
from django.db.models import Q
from django.forms import DateField, SelectDateWidget
from django.http import HttpResponse
from django import forms
from .forms import FacultyForm, StaffForm, ParentForm, UserForm
from .models import Faculty, Staff, Parent
import datetime


class dates(forms.Form):
    date = DateField(widget=
    SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),
    initial=datetime.date.today
    )

def home(request):
    return render(request,'home.html')

def homepage(request):
    return render(request,'login/home.html')

def loginFirst(request):
    return redirect("login") 

@login_required
def Timesheet(request):
    return render(request, 'login/timesheet.html',{'student':request.user.student})

@login_required
def PublicTimesheet(request,id):
    return render(request, 'login/timesheet.html', {'student':Student.objects.get(id=id)})

@login_required
def requestverdict(request):
    if request.POST.get('accept'):
        result = 1
    else:
        result = 2
    r=LeaveRequest.objects.get(id=request.POST.get('request_id'))
    r.status=result
    r.verdict=request.POST.get('reason')
    r.save()
    records=LeaveRecord.objects.get(faculty=r.faculty)
    if r.type==1:
        records.sick_leave-=1
    elif r.type==2:
        records.casual_leave-=1
    elif r.type==2:
        records.earned_leaves-=1
    records.save()

    return redirect("RequestList")

@login_required






class Detail(DetailView):
    model = User
    template_name = 'detail.html'

class FacultyFormView(View):
    form_class = FacultyForm
    template_name = 'register.html'
    def get(self,request,id):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})
    def post(self,request,id):
        print("check")
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = User.objects.get(pk=self.kwargs['id'])
            user.save()
            redirect("details",username = user.user.username)
        return render(request,self.template_name,{'form':form})

class StaffFormView(View):
    form_class=StaffForm
    template_name='register.html'
    def get(self,request,id):
        form= self.form_class(None)
        return render(request,self.template_name,{'form':form})
    def post(self,request,id):
        print("check")
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.user=User.objects.get(pk=self.kwargs['id'])
            user.save()
            redirect("detail",username=user.user.username)
        return render(request,self.template_name,{'form':form})        

class ParentFormView(View):
    form_class=ParentForm
    template_name='register.html'
    def get(self,request,id):
        form= self.form_class(None)
        return render(request,self.template_name,{'form':form})
    def post(self,request,id):
        print("check")
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.user=User.objects.get(pk=self.kwargs['id'])
            user.save()
            redirect("detail",username=user.user.username)
        return render(request,self.template_name,{'form':form})


class UserFormView(View):
    form_class=UserForm
    template_name='register.html'
    def get(self,request):
        form= self.form_class(None)
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            password=form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            # if self.kwargs['teacher'] :
            #     return redirect("teacherform",user=user.id)
            # else:
            return redirect("studentform",id=user.id)

        return render(request,self.template_name,{'form':form})


# Create your views here.
