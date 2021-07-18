from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib import auth
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
import datetime
# from .models import

# Create your views here.
User = get_user_model()

def votersignup(request):
    # reglimit = datetime.date(2021, 7, 14)
    # tday = datetime.date.today()
    # if tday >= reglimit:
    #     messages.warning(request, 'Sorry, the registration period has ended!')
    #     return redirect('signend')
    # else:
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['password'] == data['confirm_password']:
                voter = form.save(commit=False)
                voter.set_password(voter.password)
                voter.save()
                messages.success(request, 'You have been registered successfully!')
                return redirect('login')
            else:
                return render(request, 'voter_account/signup.html', {'form':form, 'error':'Passwords must match'})
    else:
        form = SignupForm()

    return render(request, 'voter_account/signup.html', {'form':form})


def signend(request):
    return render(request, 'voter_account/signend.html')


def voterlogin(request):
    if request.method == 'POST':
        usernme = request.POST.get('username')
        passwrd = request.POST.get('password')
        user = authenticate(request, username=usernme, password=passwrd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'Invalid username or password! Please confirm and try again.')
            return render(request, 'voter_account/login.html')
    else:
        return render(request, 'voter_account/login.html')

@login_required(login_url='/voter_account/signup')
def voterlogout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
