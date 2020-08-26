from django.db import models
from accounts.models import Users

# Create your models here.
class Social_Media(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE) 
    Username = models.CharField(max_length=30)
    Account_Type = models.CharField(max_length=9)

class Profile_Information(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, unique=True) 
    Interests = models.CharField(max_length=2000)
    Hobbies = models.CharField(max_length=2000)