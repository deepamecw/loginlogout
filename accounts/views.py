from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .models import * 
import datetime
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request,'Account was created for'+user)
            return redirect('login')
   
    context = {'form':form}
    return render(request,'accounts/register.html',context)
    
def loginPage(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user) 
                return redirect('home')
            else:
                messages.info(request,"username or password is incorrect")
                		

          
    context = {}
    return render(request,"accounts/login.html",context)	
def logoutpage(request):
    logout(request)
    return redirect('login')	
    
    

def home(request):
    date = datetime.date.today()
    return render(request,'accounts/home.html',{'date':date})    
@login_required(login_url = 'login')
def home(request):
    return render(request,'accounts/home.html')  
def python(request):
    return render(request,'accounts/python.html') 
    
    
    

