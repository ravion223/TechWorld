from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import forms

# Create your views here.

def sign_up_view(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authentication_system:sign-up')
    else:
        form = forms.SignUpForm()
    
    return render(
        request,
        'authentication_system/sign-up.html',
        {'form': form}
    )


def sign_in_view(request):
    if request.method == 'POST':
        form = forms.SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_page:main-page')  # Update with your redirect path
    else:
        form = forms.SignInForm()
    
    return render(request, 'authentication_system/sign-in.html', {'form': form})


def logout_view(request):
    logout(request)
    print("Redirecting to sign-in")
    return redirect('authentication_system:sign-in')