from django.contrib import admin
from myApp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    l=['name','roll','marks','dob','email']
admin.site.register(Student,StudentAdmin)