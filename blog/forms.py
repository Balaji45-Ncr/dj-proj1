from django import forms


class Contactform(forms.Form):
    name= forms.CharField(label='Name',max_length=50,required=True)
    email= forms.EmailField(label='Email')
    message= forms.CharField(label='Message',required=True)