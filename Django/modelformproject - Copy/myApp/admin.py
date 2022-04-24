from django.contrib import admin
from myApp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    l=['roll','name','place']
admin.site.register(Student,StudentAdmin)


