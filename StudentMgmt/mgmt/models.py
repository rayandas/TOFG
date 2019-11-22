from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,User

class Faculty(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    department = models.CharField(max_length=100)
    photo=models.FileField()
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.user.username})
'''
class Staff(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    department = models.CharField(max_length=100)
    photo=models.FileField()
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.user.username})
'''

class Parent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    department = models.CharField(max_length=100)
    photo=models.FileField()
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.user.username})
        

class SelectedSubject(models.Model):
    subject=models.ForeignKey(to=Subject, related_name="studies", null=True, blank=True)
    student=models.ForeignKey(to=Student, related_name="selected", null=True, blank=True)

    def percentage(self):
        p,a=self.present(),self.absent()
        s=p+a
        if s!=0:
            return str(round(p*100.0/s,2))+"%"
        else:
            return 'N.A'
    def present(self):
        a=self.attendance.all()
        return a.filter(present=True).count()
    def absent(self):
        a=self.attendance.all()
        return a.filter(present=False).count()
    def eligiblity(self):
        if self.percentage()=='N.A':
            return False
        return float(self.percentage()[:-1])>60
    def timesheet(self):
        return self.attendance.all().order_by('Date')

    

class AttendanceRecord(models.Model):
    selected_subject=models.ForeignKey(to=SelectedSubject, related_name="attendance", null=True, blank=True)
    Date=models.DateField(null=True)
    present=models.BooleanField()


# Create your models here.
