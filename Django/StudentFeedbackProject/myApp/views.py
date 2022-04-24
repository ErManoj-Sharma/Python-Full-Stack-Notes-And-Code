from django.shortcuts import render
from myApp.forms import FeedBackForm,SignupForm
# Create your views here.

def feedbackView(request):
    f=FeedBackForm()
    if request.method=="POST":
        f=FeedBackForm(request.POST)
        if f.is_valid():
            email=f.cleaned_data['email']
            rollno=f.cleaned_data['rollno']
            name = f.cleaned_data['name']
            feedback=f.cleaned_data['feedback']
            d={'name':name,'rollno':rollno,'email':email,'feedback':feedback}
            return render(request,'myApp/output.html',d)
    d={'form':f}
    return render(request, 'myApp/feedback.html',d)

def signupView(request):
    s=SignupForm()
    if request.method=="POST":
        s=SignupForm(request.POST)
        if s.is_valid():
            name=s.cleaned_data['name']
            pwd=s.cleaned_data['pwd']
            rpwd = s.cleaned_data['rpwd']
            email=s.cleaned_data['email']
            d={'name':name,'pwd':pwd,'email':email,'rpwd':rpwd}
            return render(request,'myApp/signup_output.html',d)
    d={'form':s}
    return render(request,'myApp/signup_input.html',d)


