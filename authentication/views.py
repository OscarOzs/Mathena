from django.shortcuts import render

def login(request):
    return render(request, 'authentication/login.html')

def register(request):
    return render(request, 'authentication/register.html')
