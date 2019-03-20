from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import MerchSerializer
from rest_framework import status


class ProjectsList(APIView):
    def get(self, request, format=None):
        all_projects = Projects.objects.all()
        serializers = MerchSerializer(all_projects, many=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', locals())


@login_required(login_url='/accounts/login')
def home(request):
    current_user = request.user
    all_projects = Image.objects.all()

    return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UploadForm()

        my_projects = Image.objects.all()
        my_profile = Projects.objects.all()
    return render(request, 'profile.html', locals())


@login_required(login_url='/accounts/login')
def upload_form(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by = current_user
            image.save()

            return redirect('home')
    else:
        form = UploadForm()
    return render(request, 'post.html', {'uploadform': form})


@login_required(login_url='/accounts/login')
def edit_prof(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by = current_user
            image.save()

            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'profile_edit.html', {'profileform': form})


@login_required(login_url='/accounts/login')
def logout_view(request):
    logout(request)
