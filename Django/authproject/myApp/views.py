from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from myApp.forms import signUpForm
def home_view(request):
    return render(request,'myApp/home.html')

@login_required
def java_view(request):
    return render(request,'myApp/javaexam.html')
@login_required
def python_view(request):
    return render(request,'myApp/pythonexam.html')
@login_required
def aptitude_view(request):
    return render(request,'myApp/aptitudeexam.html')
def logout_view(request):
    return render(request,'myApp/logout.html')
def signup_view(request):
    form=signUpForm()
    if request.method=="POST":
        form=signUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    d={'form':form}
    return render(request,'myApp/signup.html',d)
