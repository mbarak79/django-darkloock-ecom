from django.shortcuts import render, redirect
from .forms import SignUp
from django.contrib.auth import authenticate, login

# Create your views here.


def signup(request):
    
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username)
            login(request, user)
            return redirect('/')

    else:
        form = SignUp()

    return render(request, 'registration/signup.html',{'form':form})

        
