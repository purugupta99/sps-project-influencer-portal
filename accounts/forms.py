from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from django.forms import ModelForm

from accounts.models import Users

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60,widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(max_length=60,widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    class Meta:
        model = Users
        fields = ('username','email','password1','password2')
        
class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    email = forms.EmailField(max_length=60,widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    
    class Meta:
        model = Users
        fields = ('email','password')
        
    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        print(authenticate(email=email, password=password))
        print(email, password)
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Invalid Login')
