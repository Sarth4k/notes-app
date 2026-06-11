from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print("IS VALID:", form.is_valid())
        print("ERRORS:", form.errors)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('task-home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
