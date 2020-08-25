from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from django.forms import ModelForm

from social_media.models import Social_Media
 
class ProfileForm(forms.ModelForm):
    CHOICES = (('Instagram', 'Instagram'), ('Facebook', 'Facebook'), ('Youtube', 'Youtube'))
    username = forms.CharField(label='Username', widget=forms.TextInput())
    account_type = forms.CharField(label='Account_Type', widget=forms.Select(choices=CHOICES))
    
    class Meta:
        model = Social_Media
        fields = ()
