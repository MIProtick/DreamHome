from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authentication
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request=request, user=user)
            messages.success(request, "You've been successfully logged in!!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')
        
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Password validation
        if password == password2:
            # Check user
            if User.objects.filter(username=username).exists():
                messages.error(request, "This Username has been taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "This email is being used")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password, 
                    first_name=first_name, last_name=last_name)
                    # __AutoLogin after registration
                    # auth.login(request=request, user=user)
                    # messages.success(request, "Login Has been successfull")
                    # return redirect('index')
                    # __Redirect to login page
                    user.save()
                    messages.success(request, "Successfully registered, Please login !!")
                    return redirect('login')
        else:
            messages.error(request, "Password didn't match")
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You've been logged out!!")
        return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')

