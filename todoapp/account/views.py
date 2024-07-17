from django.shortcuts import render,redirect
from django.views import View
from .forms import RegForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class LoginView(View):
    def get(self,request):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user= authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"Login Successfull")
                return redirect("list")
            else:
                messages.error(request,"Login Failed. Invalid username/password")
                return redirect("Login")
        else:
            return render(request,"login.html",{"form":form_data})

    

class RegView(View):
    def get(self,request):
        form=RegForm()
        return render(request,"reg.html",{'form':form})
    def post(self,request):
        form_data=RegForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"User Registrtion Successfull")
            return redirect("log")
        else:
            messages.success(request,"User Registration Failed")
            return render(request,"reg.html",{"form":form_data})    


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('log')
