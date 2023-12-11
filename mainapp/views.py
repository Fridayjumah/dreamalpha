from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .form import SighupForm


# Create your views here.

def index(request):

    return render(request,'html/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            messages.info(request, 'Invalid email or password')
            return redirect('/login')
    else:
        return render(request,'html/login.html')
    
def signup(request):
    if request.method =='POST':
        form =  SighupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            messages.info(request,'username,password,or email invalid')
            return redirect('/signup')

    else:
        form = SighupForm()
    
    return render(request,'html/signup.html',{'form':form})

def home(request):

    return render(request,'html/home.html')

def logout(request):
    auth.logout(request)
    return redirect('/index')