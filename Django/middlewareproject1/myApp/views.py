from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def view1(request):
    print("Inside View Function")
    return HttpResponse("<h1>Output on browser</h1>")

from django.http import HttpResponse
def view2(request):
    a=int(input("Enter the 1st value : "))
    b=int(input("Enter the 2nd value : "))
    print(a/b)
    print("Inside view function")
    return HttpResponse("<h1>Successfully landed on the page</h1>")


