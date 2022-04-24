from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from myApp.models import Employee
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
class EmployeeView(ListView):
    model=Employee
    #default template :employee_list.html
    #default context:employee_list
class EmployeeDetailView(DetailView):
    model=Employee
    #default template :employee_detail.html
    #default context:employee
class EmployeeCreateView(CreateView):
    model=Employee
    fields="__all__"
    #default template :employee_form.html
class EmployeeUpdateView(UpdateView):
    model=Employee
    fields=('ename','esal','eexp')
    #default template :employee_form.html
class EmployeeDeleteView(DeleteView):
    model=Employee
    success_url=reverse_lazy("employeelist")
    #default template :employee_confirm_delete.html
    #default context:employee
