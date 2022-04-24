

# Create your models here.
from django.db import models
from django.urls import reverse
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=50)
    esal=models.IntegerField()
    edesig=models.CharField(max_length=40)
    eexp=models.IntegerField()
    def __str__(self):
        return self.ename
    def get_absolute_url(self):
        return reverse('employeedetail',kwargs={'pk':self.pk})
