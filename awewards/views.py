from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', locals())


def welcome(request):
    all_projects = Image.objects.all()

    return render(request, 'welcome.html', locals())


def profile_path(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UploadForm()

        my_projects = Image.objects.all()
        my_profile = Profile.objects.all()
    return render(request, 'profile.html', locals())
