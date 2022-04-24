from django.contrib import admin
from myApp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    l=['eid','ename','edesig','edob','eexp','esal']
admin.site.register(Employee,EmployeeAdmin)
