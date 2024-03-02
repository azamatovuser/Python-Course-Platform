from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from apps.account.models import Account



def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            login(request, user)
            messages.success(request, 'Siz saytga kirdingiz!')
            return redirect('main:index')
    ctx = {
        'form': form
    }
    return render(request, 'account/login.html', ctx)


def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    ctx = {
        'form': form
    }
    return render(request, 'account/register.html', ctx)


# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('main:index')
#     return render(request, 'account/logout.html')