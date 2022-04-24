from django.shortcuts import render
from myApp.models import Student
from myApp.forms import StudentForms
# Create your views here.
def Student_View(request):
    f=StudentForms()
    if request.method=='POST':
        f=StudentForms(request.POST)
        if f.is_valid():
            f.save(commit=True) # to save the changes we use commit = True
    d={'form':f}
    return render(request,'myApp/1.html',d)

def Output_View(request):
    s=Student.objects.all()
    d={'stud':s}
    return render(request,'myApp/2.html',d)

