from django import forms
from django.core import validators
class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    def clean(self):
        print("one clean mtd for all validations")
        data = super().clean()
        n=data['name']
        if len(n)<=0:            # n[0].lower()!='s'
            raise forms.ValidationError("Name must be of greather or equal to 1")
        r=data['rollno']
        if r<=0:
            forms.ValidationError('rollno must be positive ')
class SignupForm(forms.Form):
    name=forms.CharField()
    pwd=forms.CharField(widget=forms.PasswordInput)
    rpwd=forms.CharField(widget=forms.PasswordInput,label="Reenter the password")
    email=forms.EmailField()
    def clean(self):
        data=super().clean()
        pwd=data['pwd']
        rpwd=data['rpwd']
        if pwd!= rpwd:
            raise forms.ValidationError('Password Mismatch')



















# 1 method : by custom validator
#def  starts_with(data):
#    if data[0].lower()!='s':
#        raise forms.ValidationError('name must starts with s ')



# 2method by django validotors
#from django.core import validators
 #   feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(5)])

# 3 method
    #def clean_name(self):
         #   n=self.cleaned_data['name']
          #  if len(n)<5:
          #      raise forms.ValidationError("min no of char should be greather than 5 ")
          #  return n
        #def clean_rollno(self):
        #    r = self.cleaned_data['rollno']
        #if r<=0 :
        #        raise forms.ValidationError("Roll no must be positive ")
        #    return r




