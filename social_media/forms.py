from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from django.forms import Form

from social_media.models import Social_Media
 
class ProfileForm(forms.Form):
    CHOICES = (('Instagram', 'Instagram'), ('Facebook', 'Facebook'), ('Youtube', 'Youtube'))
    hobbies = forms.CharField(label='Hobbies', widget=forms.Textarea())
    interests = forms.CharField(label='Interests', widget=forms.Textarea())
    username = forms.CharField(label='Username', widget=forms.TextInput())
    account_type = forms.CharField(label='Account_Type', widget=forms.Select(choices=CHOICES))
    