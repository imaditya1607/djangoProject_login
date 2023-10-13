from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def homepage(request):
    return render(request, 'homepage.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        pass1 = request.POST.get("pass")
        user = authenticate(request, username=uname, password=pass1)
        if user is not None:
            return render(request, 'homepage.html')
        else:
            return HttpResponse("please try again with correct details ")
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        if pass1 == pass2:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect("login")

        else:
            return HttpResponse("Password doesn't Match")

    return render(request, 'signup.html')


def logouthome(request):
    logout(request)
    return redirect('login')
