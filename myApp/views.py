from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature, Blog
from django.contrib.auth.models import User,  auth
from django.contrib.messages import info
# Create your views here.


def index(request):
    return HttpResponse(
        "Hello, world. You're at the my app index page.: -)"
    )


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

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

def blog(request, id):
    blog = Blog.objects.filter(id=id)
    return render (request, 'Blog.html', {'blog':blog})


def newBlog(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        if len(title) < 5:
            info(request, "title must be more than 4 chars")
            return redirect("newblog")
        elif len(description) < 10:
            info(request, "description must be more than 10 chars")
            return redirect("newblog")
        else:
            Blog(title=title, description=description).save()
            return redirect('home')
    else:
        return render(request, 'NewBlog.html')