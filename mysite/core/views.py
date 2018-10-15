from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def slide4(request):
    return render(request, "slide 4.html", {})  # 'form': form})


def slide5(request):
    return render(request, "slide 5.html", {})


def slide7(request):
    return render(request, "slide 7.html", {})


def slide8(request):
    return render(request, "slide 8.html", {})


def slide9(request):
    return render(request, "slide 9.html", {})


def slide10(request):
    return render(request, "slide 10.html", {})


def slide11(request):
    return render(request, "slide 11.html", {})