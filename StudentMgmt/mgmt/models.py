from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,User

class Faculty(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    department = models.CharField(max_length=100)
    photo=models.FileField()
    def get_absolute_url(self):
        return reverse('detail', kwargs={'username': self.user.username})

class Staff(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    department = models.CharField(max_length=100)
    photo=models.FileField()
    def get_absolute_url(self):
        return reverse('detail', kwargs={'username': self.user.username})

class Parent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    department = models.CharField(max_length=100)
    photo=models.FileField()
    def get_absolute_url(self):
        return reverse('detail', kwargs={'username': self.user.username})
        

# Create your models here.
