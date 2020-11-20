from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import  CreateUserForm
# Create your views here.


def home(request):
    return render(request,'home.html')
def signuppage(request):
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('loginpage')
			

		context = {'form':form}
		return render(request, 'signup.html', context)

def loginpage(request):

		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logout(request):

	return redirect('loginpage')

def index(request):
    return render(request,'index.html')
def admin(request):
    return render(request,'admin.html')
def computer(request):
    return render(request,'computer.html')
def mathematics(request):
    return render(request,'mathematics.html')
def science(request):
    return render(request,'science.html')
def politics(request):
    return render(request,'politics.html')
def gk(request):
    return render(request,'gk.html')
def sports(request):
	return render(request,'sports.html')
