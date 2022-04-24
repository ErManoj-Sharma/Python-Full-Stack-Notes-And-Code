from django.contrib import admin

# Register your models here.
from django.contrib import admin
from myApp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    l=['eid','ename','esal','edesig','eexp']
admin.site.register(Employee,EmployeeAdmin)
