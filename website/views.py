from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

def home(request):
    records = Record.objects.all()

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
        'status': status,
        'records': records
    })

def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out.")

    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Directly authenticate and log the user in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Successfully registered and logged in.")

            return redirect('home')
    else:
        form = SignUpForm() 
        return render(request, "register.html", {'form': form})

    return render(request, "register.html", {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Find the record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {
            'customer_record': customer_record
        })
    else:
        messages.success(request, "Please login to view all data.")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        deleted_record = Record.objects.get(id=pk)
        deleted_record.delete()
        messages.success(request, "Customer has been deleted.")
        return redirect('home')
    else:
        messages.success(request, "Please login to complete this action.")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Customer record has been added.")
                return redirect('home')
        return render(request, 'add_record.html', {
            'form': form
        })
    else:
        messages.success(request, "Please login to access this page.")
        return redirect('home')
    
def edit_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer record has been updated')
            return redirect('home')
        
        return render(request, 'edit_record.html', {
            'form': form
        })
    else:
        messages.message(request, 'Please login to edit this record.')
        return redirect('home')