from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user

    return render(request, 'welcome.html', locals())