from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib.messages import info
# Create your views here.


def index(request):
    return HttpResponse(
        "Hello, world. You're at the my app index page.: -)"
    )


def home(request):
    features = Feature.objects.all()
    return render(request, 'home.html', {'features': features})

def logout(request):
    auth.logout(request)
    return redirect("login")

def myAnotherRoute(request):
    return HttpResponse("Hello, world. You're welcome at my another route. :-")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if len(username) < 5 or len(password) < 5 or len(repassword) < 5:
            info(request, ' username and password must be more than 4 chars')
            return redirect('register')

        elif User.objects.filter(username=username).exists():
            info(request, ' username already used ')
            return redirect('register')
        elif password == repassword:
            User.objects.create_user(
                username=username, password=password).save()
            return redirect('login')
        else:
            info(request, "Password and repasword must be same")
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if len(username) < 5 or len(password) < 5:
            info(request, ' username and password must be more than 4 chars')
            return redirect('login')
        elif user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            info(request, "Invalid credentials")
            return redirect("login")
    else:
        return render(request, 'login.html')
