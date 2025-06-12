from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Contactform(forms.Form):
    name= forms.CharField(label='Name',max_length=50,required=True)
    email= forms.EmailField(label='Email')
    message= forms.CharField(label='Message',required=True)

class Registerform(forms.ModelForm):
    username=forms.CharField(label='Username',max_length=100,required=True)
    email=forms.EmailField(label='Email',max_length=100,required=True)
    password=forms.CharField(label='Password',max_length=100,required=True)
    password_confirm=forms.CharField(label='Confirm_Password',max_length=100,required=True)

    class Meta:
        model=User
        fields=['username','email']


    def clean(self):
        data=super().clean()
        password=data.get('password')
        cnfm_pwd=data.get('password_confirm')

        if password and cnfm_pwd and password!=cnfm_pwd:
            raise forms.ValidationError('Password and confirm_password did not match')