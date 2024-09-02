from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, "user/landing-page.html",context=None)

def userSignup(request):
    return render(request, "user/signup.html",context=None)

def userLogin(request):
    return render(request, "user/login.html",context=None)