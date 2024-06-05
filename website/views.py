from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Check to see if user is logged in
    status = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            status = 'success'
        else:
            messages.error(request,"An error has been occurred while logging in.")
            status = 'error'
    
    return render(request, "home.html", {
        'status': status
    })

def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out.")

    return redirect('home')

def register_user(request):
    return render(request, "register.html")