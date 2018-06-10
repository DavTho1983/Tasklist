from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                email = user.email
                auth.login(request, user)
                msg = EmailMessage('Thanks for signing up!',
                       'Hi and thanks for signing up. We hope you have many hours of fun scheduling tasks with Tasklist. \n\nRegards, \n\nThe Tasklist Team', to=[email, ])
                msg.send()
                return redirect('home')
        else:  #<---- I think you need this one too
            return render(request, 'accounts/signup.html', {'error':"Passwords didn't match"})
    else:
        #if it's a GET
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method =='POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method =='POST':
        auth.logout(request)
        return redirect('home')
