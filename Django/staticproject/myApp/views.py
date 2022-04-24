from django.shortcuts import render

# Create your views here.
def my_view(request):
    myName = "Shreenath"
    favPlayer = "Dhoni"
    favAnimal = "Lion"
    favSub = "Python"
    d={"name":myName, "player":favPlayer, "animal":favAnimal, "subject":favSub}
    return render(request, "myApp/1.html", d)
