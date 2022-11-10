from django.shortcuts import render,redirect

from liveapp.form import studentRegister
from liveapp.models import student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def Navbar(request):
    template_name="navbar.html"
    return render(request,template_name)

@login_required(login_url='logged')
def Register(request):
    if request.method=="POST":
        
        form=studentRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data')
    form=studentRegister()
    template_name="form.html"
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='logged')
def Data(request):
    obj=student.objects.all()
    template_name='data.html'
    context={'obj':obj}
    return render(request,template_name,context)

def Delete(request,id):
    obj=student.objects.get(id=id)
    obj.delete()
    return redirect('data')

def update(request,id):
     obj=student.objects.get(id=id)
     if request.method=="POST":
        form=studentRegister(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('data')
     form=studentRegister(instance=obj)
     context={'form':form}
     template_name="update.html"
     return render(request,template_name,context)

def signup(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    form=UserCreationForm()
    context={'form':form}
    template_name="signup.html"
    return render(request,template_name,context)

def logIn(request):  
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('Password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)

    template_name="login.html"
    return render(request,template_name)      

def log_out(request):
    logout(request)
    return redirect('logged')






