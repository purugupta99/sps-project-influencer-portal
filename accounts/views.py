from django.shortcuts import render, redirect, reverse

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

import hashlib
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError

from django.contrib.auth import login, authenticate, logout

from accounts.forms import *
from accounts.models import *
from django.http import HttpResponseRedirect

# @login_required
# def index(request):
#     return render(request,'accounts/index.html')

# def sign_up(request):
#     context = {}
#     form = UserCreationForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             user = form.save()
#             login(request,user)
#             return render(request,'accounts/index.html')
#     context['form']=form
#     return render(request,'registration/sign_up.html',context)

def register(request):
    context = {}
    form = RegistrationForm()
    form2 = LoginForm()
    context['registration_form'] = form
    context['login_form'] = form2
    if request.POST:
        if 'submit1' in request.POST:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                p = form.save()
                email = form.cleaned_data.get('email')
                passwd = hashlib.sha256(form.cleaned_data.get('password1').encode()).hexdigest()
                print(p)
                print(email)
                uidb64 = urlsafe_base64_encode(force_bytes(p.pk))
                domain = get_current_site(request).domain

                return HttpResponseRedirect(reverse('accounts:home'))
            else :
                context['registration_form'] = form
            
        if 'submit2' in request.POST:
            # context = {}
            print(Users.objects.filter(email__contains='@'))
            form = LoginForm(request.POST)
            print(form)
            if form.is_valid():
                email = request.POST['email']
                passwd = request.POST['password']

                print(email, passwd)

                user = authenticate(email=email,password = passwd)
                if user:
                    # if user.is_verified == 1:
                    login(request,user)
                    # else :
                    #     context['email_verified'] = 0
                    #     return redirect('home')
                    print("logged in")
                    return HttpResponseRedirect(reverse('social_media:create_profile'))
            else:
                context['login_form'] = form

    return render(request,'index.html',context)

@login_required
def my_logout(request):
    print(request.user.id)
    logout(request)
    return redirect('accounts:home')