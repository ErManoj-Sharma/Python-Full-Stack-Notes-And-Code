from django import forms

class StudentForm(forms.Form):
    sid=forms.IntegerField()
    sname=forms.CharField()
    smarks=forms.FloatField()
    splace=forms.CharField()