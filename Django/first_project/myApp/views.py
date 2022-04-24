from django.shortcuts import render
from django.http import HttpResponse

# Create your views here./ added view 1 with http response
def view1(request):             # view
    s = "Welcome to Python Webdevelopment"
    return HttpResponse(s)

