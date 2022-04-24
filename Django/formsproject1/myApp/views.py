
from django.shortcuts import render
from myApp.forms import StudentForm
# Create your views here.

def FormView(request):
    f=StudentForm()
    if request.method=="POST":
        f=StudentForm(request.POST)
        print('post is correct')
        if f.is_valid():
            sid = f.cleaned_data['sid']
            print(sid)
            sname = f.cleaned_data['sname']
            smarks = f.cleaned_data['smarks']
            splace = f.cleaned_data['splace']
            d = {'id1':sid,'name': sname,'marks': smarks,'place':splace}
            return render(request,'myApp/output.html',d)
    d={'form':f}
    return render(request,'myApp/input.html',d)