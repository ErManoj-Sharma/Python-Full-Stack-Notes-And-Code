
from django.shortcuts import render
# Create your views here.

# Create your views here.
def template_view(request):
   name="manoj"
   id=1
   place='bhilwara'
   context={'key1':name,'key2':id,'key3':place}
   return render(request, 'myApp/1.html',context)