from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html', {'password':'Qwerty1234'})

def password(request):
    characters = list('abcdefghijklmnoprstquvwyxz')

    length = 10

    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/password.html', {'password':thepassword})

