from django.shortcuts import render
from myApp.models import Student
# Create your views here.
def fakerView(request):
    s=Student.objects.all()



    d={'stud':s}
    return render(request,'myApp/output.html', d)


