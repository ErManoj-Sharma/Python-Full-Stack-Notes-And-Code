from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=30)
    edesig = models.CharField(max_length=30)
    edob = models.DateField()
    eexp = models.FloatField()
    esal = models.IntegerField()
    def __str__(self):
        return str(self.eid)