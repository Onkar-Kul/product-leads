from django.shortcuts import render


# Create your views here.

def registration_page(request):
    return render(request, 'registration.html')


def login_page(request):
    return render(request, 'login.html')


def home_page(request):
    pass


def dashboard(request):
    return render(request, 'dashboard.html')
