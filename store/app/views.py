from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import os

# Create your views here.
def log(req):
    if 'shop' in req.session:
        return redirect(admdash)
    if 'user' in req.session:
        return redirect (uhome)
    if req.method=="POST":
        email = req.POST['email']
        psw = req.POST['psw']
        print(email,psw)
        data = authenticate(username=email, password=psw)
        if data:
            login(req, data)
            if data.is_superuser:
                req.session['shop']=email
                return redirect(admdash)
            else:
                req.session['user']=email
                return redirect(uhome)
        else:
            messages.warning(req, "Incorrect username or password.")
            return redirect(log) 
    return render(req,'login.html')

def reg(req):
    if req.method=="POST":
        name=req.POST['name']
        email=req.POST['email']
        psw=req.POST['psw']
        data=User.objects.create_user(first_name=name,email=email,username=email,password=psw)
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
            pid=req.POST['pid']
            name=req.POST['name']
            disc=req.POST['disc']
            file=req.FILES['img']
            cat_id=req.POST['cat_id']
            cate=Category.objects.get(pk=cat_id)
            data=Product.objects.create(pid=pid,name=name,disc=disc,img=file,cat_id=cate)
            data.save()
            return redirect(addws)
        pass
        categories = Category.objects.all()
        return render(req, 'shop/addproduct.html', {'categories': categories})
    return redirect(log)

def editp(req, pid):
    if 'shop' in req.session:
        pro=Product.objects.get(pid=pid)
        if req.method == 'POST':
            name = req.POST['name']
            disc = req.POST['disc']
            file = req.FILES.get('img')
            if file:
                Product.objects.filter(pid=pid).update(name=name, disc=disc)
                data = Product.objects.get(pid=pid)
                data.img = file
                data.save()
            else:
                Product.objects.filter(pid=pid).update(name=name, disc=disc)
            weight_instance = Weight.objects.filter(product__pid=pid).first()
            if weight_instance:
                return redirect('edit_weight', pid=pro.pk) 
            else:
                return redirect('add_weight')
        else:
            data = get_object_or_404(Product, pid=pid)
            return render(req, 'shop/editproduct.html', {'data': data})
    return redirect('log')

def addws(req):
    if 'shop' in req.session:
        if req.method=='POST':
            stock=req.POST['stock']
            price=req.POST['price']
            offer_price=req.POST['offer_price']
            product_weight=req.POST['weight']
            product=req.POST['productname']
            pw=Product.objects.get(pk=product)
            data=Weight.objects.create(stock=stock,product_weight=product_weight,product=pw,price=price,offer_price=offer_price)
            data.save()
            return redirect(viewp)
        products=Product.objects.all()
        return render(req, 'shop/addweight.html',{'products':products})
    return redirect(log)

def editws(req, pid):
    if 'shop' in req.session:
        product = get_object_or_404(Product, pk=pid)
        data = Weight.objects.filter(product=product)

        if req.method == 'POST':
            weight_id = req.POST.get('weight_id')
            weight = get_object_or_404(Weight, id=weight_id)

            # Update fields with form data
            weight.product_weight = req.POST['product_weight']
            weight.stock = req.POST['stock']
            weight.price = req.POST['price']
            weight.offer_price = req.POST['offer_price']
            weight.save()

            return redirect(viewp)  # Ensure 'viewp' is a valid URL or view name

        return render(req, 'shop/editweight.html', {'data': data})

    return redirect('log') 


def viewp(req):
    category_id = req.GET.get('category', None)
    categories = Category.objects.all()
    if category_id:
        products = Product.objects.filter(cat_id=category_id)
    else:
        products = Product.objects.all()
    return render(req,'shop/viewproduct.html', {'products': products,'categories': categories,})

def delp(req,pid):
    data=Product.objects.get(pid=pid)
    file=data.img.url
    file=file.split('/')[-1]
    os.remove('media/'+file)
    data.delete()
    return redirect(admdash)

def update_banner(req):
    return render(req,'shop/dash.html')

def add_cat(req):
    if 'shop' in req.session:
        if req.method=='POST':
            cat_name=req.POST['category_name']
            cat_name=cat_name.lower()
            cat_image = req.FILES['category_image']
            try:
                data=Category.objects.get(name=cat_name,cat_image=cat_image)
            except:
                data= Category.objects.create(cat_name=cat_name,cat_image=cat_image)
                data.save()
                print(data)
            return redirect(addp)
        categories= Category.objects.all
        return render(req,'shop/addcategory.html',{'categories':categories})
    else:
        return render(log)
    
def dele_cat(req,cat_id):
    if 'shop' in req.session:
        category = get_object_or_404(Category,id=cat_id)
        category.delete()
        return redirect(add_cat)
    return redirect(log) 

def uhome(req):
        if 'user' in req.session:
            category=Category.objects.all()
            return render(req,'user/userhome.html',{'category':category})
        return redirect(log)
         
def product_list(req, category_id):
    selected_category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(cat_id=selected_category)
    product_weights = Weight.objects.filter(product__in=products)
    selected_weights = {}

    if req.method == "POST":
        selected_product_id = int(req.POST.get("product_id"))
        selected_weight = req.POST.get("weight")
        selected_weights[selected_product_id] = selected_weight
        # Redirect to the single product page with the selected product and weight
        return redirect('single_product', pid=selected_product_id)

    context = {
        'products': products,
        'selected_category': selected_category,
        'product_weights': product_weights,
        'selected_weights': selected_weights,
    }
    return render(req, 'user/product_list.html', context)

def search_products(req):
    query = req.GET.get('q', '')  
    results = Product.objects.filter(name__icontains=query)    
    return render(req, 'user/search_results.html', {'query': query, 'results': results})

def single_product(req, pid):
    product = get_object_or_404(Product, pk=pid)
    weights = Weight.objects.filter(product=product)
    selected_weight = req.GET.get('weight', None)

    if selected_weight:
        weight_details = weights.filter(product_weight=selected_weight).first()
    else:
        weight_details = None

    context = {
        'product': product,
        'weights': weights,
        'weight_details': weight_details
    }
    return render(req, 'user/single.html', context)

def add_to_cart(req, pid):
    pass

def buy_now(req, pid):
    pass
