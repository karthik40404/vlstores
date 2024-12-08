from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def log(req):
    if req.method=="POST":
        email=req.POST['email']
        psw=req.POST['psw']
        data=authenticate(email=email,password=psw)
        data.save()
        return redirect(admdash)
    else:
        return render(req,'login.html')

def reg(req):
    if req.method=="POST":
        name=req.POST['name']
        email=req.POST['email']
        psw=req.POST['psw']
        data=User.objects.create_user(username=name,email=email,password=psw)
        data.save()
        return redirect(log)
    else:
        return render(req,'registraion.html')

def admdash(req):
    return redirect(req,'dash.html')

def logout(req):
     logout(req)
     req.session.flush()
     return redirect(log)