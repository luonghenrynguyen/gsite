from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, '/registration/login.html')
def logout(request):
    return render(request, '/registration/logged_out.html')    