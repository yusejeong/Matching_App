from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserChangeForm,CustomUserCreationForm

# Create your views here.
def index(request):
    return render(request, 'MuMa/index.html')
def signin(request):
    return render(request,'MuMa/login.html')
def signup(request):
    if request.user.is_authenticated:
        return redirect('MuMa:index')
    if request.method =="POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('MuMa:index')
    return render(request,'MuMa/signup.html')