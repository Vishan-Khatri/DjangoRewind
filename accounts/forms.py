from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name  = forms.CharField(max_length=50, required=True)
    email      = forms.EmailField(required=True)
    college    = forms.CharField(max_length=200, required=True)

    class Meta:
        model  = User
        fields = ['username','first_name','last_name','email','password1','password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model   = UserProfile
        exclude = ['user']
        widgets = {'bio': forms.Textarea(attrs={'rows': 3})}
