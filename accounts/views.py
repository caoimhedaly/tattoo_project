from django.shortcuts import render, redirect,  get_object_or_404
from .forms import  AddictForm, ArtistForm, SignUpForm
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from accounts.models import Artist


def get_index(request):
    return render(request, 'index.html')
    
def read_profile(request):
    return render(request, 'profile2.html')
    
    


    
def register_artist(request):
    
    if request.method == "POST":
        user_form = SignUpForm(request.POST)
        artist_form = ArtistForm(request.POST, request.FILES)
        
        if user_form.is_valid() and artist_form.is_valid():
            user = user_form.save()
            artist = artist_form.save(commit=False)
            artist.user = user
            artist.save()
            
            u = user_form.cleaned_data['username']
            p = user_form.cleaned_data['password1']
            user = authenticate(username=u, password=p)
            
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                user_form.add_error(None, "Can't log in now, try later.")
    else:
        user_form =SignUpForm()
        artist_form = ArtistForm()

    return render(request, "registration/signup.html", {'user_form': user_form, 'profile_form': artist_form})
    

def register_lover(request):
    
    if request.method == "POST":
        user_form = SignUpForm(request.POST)
        addict_form = AddictForm(request.POST, request.FILES)
        
        if user_form.is_valid() and addict_form.is_valid():
            user = user_form.save()
            addict = addict_form.save(commit=False)
            addict.user = user
            addict.save()
            
            u = user_form.cleaned_data['username']
            p = user_form.cleaned_data['password1']
            user = authenticate(username=u, password=p)
            
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                user_form.add_error(None, "Can't log in now, try later.")
    else:
        user_form = SignUpForm()
        addict_form =AddictForm()

    return render(request, "registration/signup.html", {'user_form': user_form, 'profile_form':addict_form})
    
    
def artist_detail(request, id):
   
      artist = get_object_or_404(Artist, pk=id)
      return render(request, 'ecommerce/artist_profile.html', {'artist':artist})
    

