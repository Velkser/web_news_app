from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User

# Create your views here.
def signup(request: HttpRequest):
    """_summary_

    Args:
        request (HttpRequest): Запрос посланый юзером

    Returns:
        render: создается новая страничка которая и открывается
        redirect: юзер перенаправляется на домашнюю страничуку если он нажал кнопку залогинится и все прошло успешно
    """    
    form = RegisterForm()
    err = ''

    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']

        form = RegisterForm(request.POST)
        if not User.objects.filter(email=email).exists() and not User.objects.filter(username=username).exists():
            if form.is_valid():
                    user = form.save()
                    login(request, user)
                    print("login")
                    return redirect(to="home")
            
            else:
                err = 'not valid'
                print("error")
        else:
            err = 'такой пользователь уже существует'
            print("user error")


    return render(request, template_name="auth_temp/register.html", context={"form": form, "errors": err}) 


def login_user(request):
    form = LoginForm(request.POST)
    err = ''
    if request.method == 'POST':
        password = request.POST["password"]
        username = request.POST["username"]

        if form.is_valid():
            user = authenticate(request=request, username=username, password=password)             
            if user is not None:
                logout(request=request)

                login(request, user)
                redirect(to="home")
            else:
                form = LoginForm()
                err = "неверный логин или пароль"
                
    return render(request, template_name="auth_temp/login.html", context={"form": form, "errors": err})


def logout_user(request):
    logout(request)

    print("разлогин")
    return redirect(to="home")


def question(request):
    return render(request, 'auth_temp/question.html')

