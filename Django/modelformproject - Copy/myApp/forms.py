from django import forms
from myApp.models import Student
class StudentForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # fields=[f1,f2,f3,f4]
        # exculdes=[f3,f5]
