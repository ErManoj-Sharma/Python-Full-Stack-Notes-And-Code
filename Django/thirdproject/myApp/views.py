from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    s = "<h1>This is 1st Response</h1>"
    return HttpResponse(s)
def view2(request):
    s = "<h1>This is 2nd Response<h1>"
    return HttpResponse(s)
