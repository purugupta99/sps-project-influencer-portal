from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

from uuid import uuid4
# Create your models here.

def Rename_Image_User(instance, filename):
    print(instance)
    print(filename)
    ext = filename.split('.')[-1]
    # if instance.pk:
    return 'User_Image/'+'{}.{}'.format(uuid4().hex, ext)

class MyAccountManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(
            email = email,
            username = username,
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        
        return user
    def create_superuser(self,username,email,password):
        user = self.create_user(
            username=username,
            email = email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        
        return user


class Users(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=250) # For AbstractUser
    username = models.CharField(max_length=150, blank=True,unique=True) # For AbstractUser
    date_joined = models.DateTimeField(auto_now_add=True) # For AbstractUser
    last_login = models.DateTimeField(auto_now=True, null=True) # For AbstractUser
    is_admin = models.BooleanField(default=False)  # For AbstractUser
    is_active = models.BooleanField(default=True) # For AbstractUser
    is_staff = models.BooleanField(default=False) # For AbstractUser
    is_superuser = models.BooleanField(default=False) # For AbstractUser
    # id = models.BigAutoField()
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    prefix = models.CharField(max_length=20, blank=True, null=True)
    suffix = models.CharField(max_length=150, blank=True, null=True)
    password = models.CharField(max_length=255) # Required
    user_type = models.CharField(max_length=11,default='NORMAL_USER')
    home_phone = models.CharField(max_length=150, blank=True, null=True)
    cell_phone = models.CharField(max_length=150, blank=True, null=True)
    job_title = models.CharField(max_length=150, blank=True, null=True)
    company = models.CharField(max_length=150, blank=True, null=True)
    website = models.CharField(max_length=150, blank=True, null=True)
    blog = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    dob = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    login_session_key = models.CharField(max_length=255, blank=True, null=True)
    is_social_signup = models.SmallIntegerField(default=0)
    social_type = models.CharField(max_length=9, blank=True, null=True)
    social_id = models.CharField(max_length=250, blank=True, null=True)
    user_image = models.ImageField(upload_to=Rename_Image_User,blank=True,null=True)
    user_image_thumb = models.TextField(blank=True, null=True)
    user_token = models.CharField(max_length=250, blank=True, null=True)
    is_verified = models.SmallIntegerField(default=0)
    is_blocked = models.SmallIntegerField(default=0)
    is_deactivated = models.SmallIntegerField(default=0)
    last_activity = models.DateTimeField(blank=True, null=True)
    is_account_closed = models.SmallIntegerField(blank=True, null=True)
    account_closed_datetime = models.DateTimeField(blank=True, null=True)
    account_close_type = models.CharField(max_length=150, blank=True, null=True)
    account_close_reason = models.TextField(blank=True, null=True)
    stripe_user_id = models.CharField(max_length=100, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = MyAccountManager()
    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_Label):
        return True
    

