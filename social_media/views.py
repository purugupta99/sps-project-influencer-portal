from django.shortcuts import render, reverse
from .models import Social_Media, Profile_Information
from .forms import ProfileForm
from django.http.response import HttpResponseRedirect


def create_profile(request):
    if request.user.is_authenticated == False:
        return HttpResponseRedirect(reverse('accounts:home'))
    if(request.method == "POST"):
        form = ProfileForm(request.POST)
        if(form.is_valid()):
            account_type = request.POST['account_type']
            uname = request.POST['username']
            interests = request.POST['interests']
            hobbies = request.POST['hobbies']
            obj = Social_Media.objects.filter(user=request.user, Account_Type=account_type, Username=uname)
            # print(obj)
            profile = None
            try:
                profile = Profile_Information.objects.get(user=request.user)
            except:
                print(profile)
            if(not profile):
                profile = Profile_Information.objects.create(user=request.user, Interests=interests, Hobbies=hobbies)
                if(interests == "" and hobbies == ""):
                    raise Exception("Interests and Hobbies both left empty")
            else:
                profile.Interests = profile.Interests+" "+interests
                profile.Hobbies = profile.Hobbies + " "+hobbies
            Profile_Information.save(profile)
            if(not obj): 
                obj = Social_Media.objects.create(user=request.user, Username=uname, Account_Type=account_type)
                Social_Media.save(obj)
                return HttpResponseRedirect(reverse('social_media:profile'))
            else:
                raise Exception('Already Added '+account_type+' in the Profile.')

    form = ProfileForm()
    context={}
    context['form'] = form
    return render(request, 'create_profile.html', context)

def view_profile(request):
    context = {}
    context['accounts'] = Social_Media.objects.filter(user=request.user)
    context['profile'] = Profile_Information.objects.get(user=request.user)
    return render(request, 'profile.html', context)