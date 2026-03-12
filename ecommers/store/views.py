from django.shortcuts import redirect, render
from .models import Category, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})        

def about(request):
    return render(request, 'about.html')

def login_user(request):    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Has iniciado sesión exitosamente.")
            return redirect('home')
        else:
            messages.error(request, "Credenciales inválidas. Por favor, inténtalo de nuevo.")
            return redirect('login') 
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect('home')   

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Tu cuenta ha sido creada exitosamente.")
            return redirect('home')
    else:       
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

def category(request, foo):
    foo = foo.lower().replace('-', ' ')
    try:
       if foo == 'all':
            products = Product.objects.all()
            category_name = "Todos los productos"
       else:
            category = Category.objects.get(name__iexact=foo)
            products = Product.objects.filter(category=category)
            category_name = category.name.title()
       return render(request, 'category.html', {'products': products, 'category': category_name})
    except:
        messages.error(request, "Categoría no válida o no existe.")
        return redirect('home')
