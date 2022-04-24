from django.shortcuts import render
from myApp.models import Employee
# Create your views here.;
def EmpolyeeView(request):
    e = Employee.objects.all()
    d = {'emp': e}
    return render(request, 'myApp/1.html', d)
