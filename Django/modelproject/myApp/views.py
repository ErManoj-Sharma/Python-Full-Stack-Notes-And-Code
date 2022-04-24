from django.shortcuts import render
from myApp.models import Student
# Create your views here.
def myview(request):
    s = Student.objects.all()
    print(type(s))
    d = {'stud': s}
    return render(request, 'myApp/1.html', d )
def myview1(request):
    s = Student.objects.all()
    print(type(s))
    d = {'stud': s}
    return render(request, 'myApp/2.html', d )