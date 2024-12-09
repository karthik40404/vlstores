from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def log(req):
    if 'shop' in req.session:
        return redirect(admdash)
    if req.method=="POST":
        email = req.POST['email']
        psw = req.POST['psw']
        print(email,psw)
        data = authenticate(username=email, password=psw)
        if data:
            login(req, data)
            if data.is_superuser:
                req.session['shop'] = email
                return redirect(admdash)
        else:
            messages.warning(req, "Incorrect username or password.")
            return redirect(log) 
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
    return render(req,'shop/dash.html')

def lout(req):
     logout(req)
     req.session.flush()
     return redirect(log)

def addp(req):
    return render(req,'shop/addproduct.html')

def editp(req):
    return render(req,'shop/editproduct.html')

def delp(req):
    return render(req,'shop/deleteproduct.html')