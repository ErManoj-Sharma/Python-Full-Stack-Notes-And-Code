from django.shortcuts import render
from myApp.models import Student
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
class StudentView(ListView):
    model=Student
    #default template:student_list.html
    #default context:student_list
class StudentDetailView(DetailView):
    model=Student
    #default template:student_detail.html
    #default context:student
class StudentCreateView(CreateView):
    model=Student
    fields='__all__'
    #default template:student_form.html
class StudentUpdateView(UpdateView):
    model=Student
    fields=('name','marks')
    #default template:student_form.html
class StudentDeleteView(DeleteView):
    model=Student
    success_url=reverse_lazy('students')
    #students-reverse url to display student list
