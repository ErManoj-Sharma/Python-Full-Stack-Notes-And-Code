from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
   s="<h1> first response  </h1"
   return HttpResponse(s)
def view2(request):
    a=int(input("enter no :"))
    b=int(input("enter no :"))
    c=a+b
    return HttpResponse(str(c))
def view3(request):
    s = "<h1> third response  </h1"
    return HttpResponse(s)
