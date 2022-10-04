from datetime import datetime
from tkinter import Image
from urllib import request
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from . import urls
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth, messages
from .models import Categorie, User, Product, Cart, Profile, Comment
from django.db.models import Q
from .forms import ImageForm

def login_page(request):
    return render(request, 'login.html')

def loginUser(request):
    if request.method == 'POST':
        name = request.POST['username']
        passw = request.POST['password']
        user = authenticate(password=passw, username=name)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('main')
        else:
            messages.info(request, 'Username or password error')
            return HttpResponseRedirect('/')

def register(request):
    return render(request, 'register.html')

def log_out(request):
    logout(request)
    return redirect('/')

def registerUser(request):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    if request.method == 'POST':
        if password == password2:
            if User.objects.filter(username=username).exists() == False:
                user =  User.objects.create_superuser(username=username, password=password)
                user.save()
                prof = Profile.objects.create(name=user, balance=0)
                prof.save()
                cart = Cart.objects.create(owner=user)
                cart.save()
                return HttpResponseRedirect('/')
            else:
                messages.info(request, message='Username already taken')
                return HttpResponseRedirect('register')
        else:
            messages.info(request, 'Password confirmation error')
            return HttpResponseRedirect('register')

def main(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    productGrid_content = Product.objects.filter(Q(name__icontains=q) | Q(category__title=q))
    categories = Categorie.objects.all()
    context = {'products': productGrid_content, 'categories': categories, 'user': request.user} 
    return render(request, 'main.html', context)

def profile(request):
    user = request.user
    prof = Profile.objects.get(name=user)
    context = {'prof': prof}
    return render(request, 'profile.html', context)

def edit_profile(request):
    prof = Profile.objects.get(name=request.user)

    if request.method == "POST":
        form = ImageForm(request.FILES, request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else:
        form = ImageForm()

    context = {'prof': prof, 'form': form, 'user': request.user}
    return render(request, 'edit_profile.html', context)

def change_profile(request):
    u = request.user
    user = Profile.objects.get(name=request.user)

    if request.method == "GET":
        new_surname = request.GET['new_surname']
        status = request.GET['status']
        email = request.GET['email']
        u.email = email
        user.surname = new_surname
        user.status = status
        user.save()
        messages.info(request, 'Profile changed')
        return redirect('profile')
    return redirect('profile')

def product(request):
    p = ''
    if request.GET.get('p') is not None:
        p = request.GET.get('p')
    product = Product.objects.get(name=p)
    rating = []

    for i in range(product.rating):
        rating += '1'

    comments = Comment.objects.filter(product=product)
    context = {'product': product, 'rating': rating, 'comments': comments}
    return render(request, 'product.html', context)

def add_comment(request, prod_name):
    if request.method == 'GET':
        comment_txt = request.GET['comment_text']
        rating = request.GET['rating']
        author = User.objects.get(username=request.user)
        date = datetime.now()
        print(prod_name)
        product = Product.objects.get(name=prod_name)
        comment = Comment.objects.create(product=product, author=author, text=comment_txt, rating=rating, date=date)
        comment.save()
        return redirect('http://127.0.0.1:8000/main/product?p='+str(prod_name))
    else:
        return redirect('main')

def add_to_cart(request, prod_name):
    cart = Cart.objects.get(owner=request.user)
    prod = Product.objects.get(name=prod_name)
    cart.product.add(prod)
    cart.save()
    return redirect('http://127.0.0.1:8000/main/product?p='+str(prod_name))

def cart(request):
    cart = Cart.objects.get(owner=request.user)
    products = cart.product.all()
    context = {'products': products, 'cart': cart}
    return render(request, 'cart.html', context)

def delete_from_cart(request, product):
    p = Product.objects.get(name=product)
    cart = Cart.objects.get(owner=request.user)
    cart.product.remove(p)
    cart.save()
    return redirect('cart')
    