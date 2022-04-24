
# Create your models here.
from django.db import models
from django.urls import reverse
class Student(models.Model):
    name=models.CharField(max_length=50)
    number=models.IntegerField()
    marks=models.FloatField()
    place=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    def  get_absolute_url(self):
        return  reverse('detail',kwargs={'pk':self.pk})
