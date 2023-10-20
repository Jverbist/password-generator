from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    # list of characters
    characters = list('abcdefghijklmnopqrstuvwxyz')
    # if structure to check if they want uppercase
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    # if structure to check if they want special character
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    # if structure to check if they want numbers
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    # define length by input form
    length = int(request.GET.get('length', 12))
    # create empty string for thepassword variable
    thepassword = ''
    # generate random password
    for x in range(length):
        thepassword += random.choice(characters)



    return render(request, 'generator/password.html', {'password':thepassword})



