from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Post
class Contactform(forms.Form):
    name= forms.CharField(label='Name',max_length=50,required=True)
    email= forms.EmailField(label='Email')
    message= forms.CharField(label='Message',required=True)

class Registerform(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    password = forms.CharField(label='Password', max_length=100, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirm Password', max_length=100, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email','password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username

    def clean(self):
        data = super().clean()
        password = data.get('password')
        confirm = data.get('password_confirm')
        if password and confirm and password != confirm:
            raise forms.ValidationError('Password and confirm password did not match')
        return data


class Loginform(forms.Form):
    username=forms.CharField(label="Username",max_length=100,required=True)
    password=forms.CharField(label='Password',max_length=50,required=True)

    # def clean(self):
    #     cleaned_data=super().clean()
    #     username=cleaned_data.get('username')
    #     password=cleaned_data.get('password')
    #
    #     if username and password:
    #         user=authenticate(username=username,password=password)
    #         if user is None:
    #             raise forms.ValidationError('No user with this creds')



class Newpost(forms.ModelForm):
    title=forms.CharField(label='Title',max_length=25)
    content=forms.CharField(label='Content')
    class Meta:
        model=Post
        fields = ['title','content','category','img_url']

    def save(self, commit=...):

        post=super().save(commit)
        if not post.img_url:
            post.img_url='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/450px-No_image_available.svg.png'

        if commit:
            post.save()
        return post
