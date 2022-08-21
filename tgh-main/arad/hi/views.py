from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    context = {
        'username': 'HI im arad',
    }   
    return render(request, 'hello/home.html', context)