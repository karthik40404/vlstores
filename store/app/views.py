from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

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
    if 'shop' in req.session:
        if req.method == 'POST':
            pass
        categories = Category.objects.all()
        return render(req, 'shop/addproduct.html', {'categories': categories})
    return redirect(log)

def editp(req):
    return render(req,'shop/editproduct.html')

def delp(req):
    return render(req,'shop/deleteproduct.html')

def update_banner(req):
    return render(req,'shop/dash.html')

def add_cat(req):
    if 'shop' in req.session:
        if req.method=='POST':
            cat_name=req.POST['category_name']
            cat_name=cat_name.lower()
            try:
                data=Category.objects.get(name=cat_name)
            except:
                data= Category.objects.create(cat_name=cat_name)
                data.save()
                print(data)
            return redirect(addp)
        categories= Category.objects.all
        return render(req,'shop/addcategory.html',{'categories':categories})
    else:
        return render(log)
    
def dele_cat(req,cat_id):
    if 'shop' in req.session:
        category = get_object_or_404(Category, id=cat_id)
        category.delete()
        messages.success(req, "Category deleted successfully.")
        return redirect(add_cat)
    return redirect(log) 