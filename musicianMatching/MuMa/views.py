from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'MuMa/index.html')
def signin(request):
    return render(request,'MuMa/login.html')