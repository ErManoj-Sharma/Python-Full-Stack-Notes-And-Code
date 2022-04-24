import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studentfbvproject.settings')
django.setup()
from faker import Faker
from myApp.models import Student
f=Faker()
def populate(n):
    for i in range(n):
        fno=f.random_int(min=1,max=20)
        fname=f.name()
        fmarks=f.random_int(min=1,max=100)
        faddr=f.address()
        e=Student.objects.get_or_create(sno=fno,sname=fname,smarks=fmarks,saddr=faddr)

populate(20)
