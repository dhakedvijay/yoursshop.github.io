from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def Detail(request):
    return render(request,'LoginApp/detail.html')

def SignUp(request):
    sign=SignUpForm()
    if request.method=='POST':
        sign=SignUpForm(request.POST)
        if sign.is_valid():
            try:
                email=sign.cleaned_data['email']
                pas=sign.cleaned_data['password']
                user = User.objects.create_user(email,email,pas)
                user.save()
                return redirect('LoginApp:login')
            except:
                pass
    return render(request,'LoginApp/signup.html',{'sign':sign})

def Login(request):
    login=LoginForm()
    print("1")
    if request.method=='POST':
        print("2")
        login=LoginForm(request.POST)
        if login.is_valid():
            print("3")
            try:
                email=login.cleaned_data['email']
                pas=login.cleaned_data['password']
                print("4")

                user = authenticate(request,username=email, password=pas)
                print("5")
                if user:
                    print("6")
                    print(user)
                    login(request, user)
                    print("7")
                    return redirect('Shop:allproduct')

            except:
                pass
    return render(request,'LoginApp/login.html',{'login':login})
