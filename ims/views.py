import imp
from django import contrib
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, Entry, Category, Brand, Staff
from .forms import CatForm, BrandForm, CountForm, ProductForm, CreateUserForm, ReorderForm, RestockForm, SalesForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users,admin_only
from django.contrib.auth.models import Group
import json
from django.core import serializers

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')


            messages.success(request, 'Account successfully created for ' + username)
            return redirect('login')
    context = {
        'form':form
    }
    return render(request, 'ims/register.html',context)
    
@unauthenticated_user
def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or Password is not correct')

    return render(request, 'ims/login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')


def staffPage(request):
    products = Product.objects.all()
    cats = Category.objects.all()
    brands = Brand.objects.all()
    total_products = products.count()
    total_cats = cats.count()
    total_brands = brands.count()

    context = {
        'products':products,
        'cats':cats,
        'brands':brands,
        'total_products':total_products,
        'total_cats':total_cats,
        'total_brands':total_brands
    }
    return render(request, 'ims/staff.html', context)

@login_required(login_url=('login'))
@admin_only
def dashboard(request):
    products = Product.objects.all()
    cats = Category.objects.all()
    brands = Brand.objects.all()
    staffs = Staff.objects.all()
    
    total_staffs = staffs.count()
    total_products = products.count()
    total_cats = cats.count()
    total_brands = brands.count()

    context = {
        'products':products,
        'cats':cats,
        'brands':brands,
        'total_products':total_products,
        'total_cats':total_cats,
        'total_brands':total_brands,
        'staffs':staffs,
        'total_staffs':total_staffs
    }
    return render(request, 'ims/dashboard.html', context)

@login_required(login_url=('login'))
@allowed_users(allowed_roles=['admin'])
def brand(request):
    brands = Brand.objects.all()
    form = BrandForm()
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, (brands.name) + ' successfully created')
            return redirect('brand')
    context = {
        'form':form,
        'brands':brands
    }
    return render(request, 'ims/brand.html', context)

@login_required(login_url=('login'))
@allowed_users(allowed_roles=['admin'])
def cat(request):
    cats = Category.objects.all()
    form = CatForm()
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, (cats.name) + ' successfully created')
            return redirect('cat')
    context = {
        'form':form,
        'cats':cats
    }
    return render(request, 'ims/cat.html',context)

@login_required(login_url=('login'))
@allowed_users(allowed_roles=['admin'])
def product(request):
    products = Product.objects.all()
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,  'successfully created')
            return redirect('product')
    context = {
        'form':form,
        'products':products
    }
    return render(request, 'ims/product.html', context)

@login_required(login_url=('login'))
@allowed_users(allowed_roles=['admin'])
def UpdateProduct(request, pk):
    products = Product.objects.get(id=pk)
    form = ProductForm(instance=products)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=products)
        if form.is_valid():
            form.save()
            print("Edited")
            messages.success(request, 'successfully updated')
            return redirect('product')
    context = {
        'form':form,
        'products':products
    }
    return render(request, 'ims/add_new.html', context)


@login_required(login_url=('login'))
@allowed_users(allowed_roles=['admin'])
def UpdateBrand(request, pk):
    brands = Brand.objects.get(id=pk)
    form = BrandForm(instance=brands)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brands)
        if form.is_valid():
            form.save()
            messages.success(request, (brands.name) + ' successfully updated')
            return redirect('brand')
    context = {
        'form':form,
    }
    return render(request, 'ims/add_new.html', context)


@login_required(login_url=('login'))
@allowed_users(allowed_roles=['admin'])
def UpdateCat(request, pk):
    cats = Category.objects.get(id=pk)
    form = CatForm(instance=cats)
    if request.method == 'POST':
        form = CatForm(request.POST, instance=cats)
        if form.is_valid():
            form.save()
            messages.success(request, (cats.name) + ' successfully updated')
            return redirect('cat')
    context = {
        'form':form,
    }
    return render(request, 'ims/add_new.html', context)


@login_required(login_url=('login'))
@allowed_users(allowed_roles=['admin'])
def DeleteProduct(request, pk):
    products = Product.objects.get(id=pk)
    if request.method == 'POST':
        products.delete()
        messages.success(request, 'successfully Deleted')
        return redirect('product')

    context = {
        'name':products
    }
    return render(request, 'ims/delete.html', context)


@login_required(login_url=('login'))
@allowed_users(allowed_roles=['admin'])
def DeleteBrand(request, pk):
    brands = Brand.objects.get(id=pk)
    if request.method == 'POST':
        brands.delete()
        messages.success(request, 'successfully Deleted')
        return redirect('brand')

    context = {
        'name':brands
    }
    return render(request, 'ims/delete.html', context)


@login_required(login_url=('login'))
@allowed_users(allowed_roles=['admin'])
def DeleteCat(request, pk):
    cats = Category.objects.get(id=pk)
    if request.method == 'POST':
        cats.delete()
        messages.success(request, 'successfully Deleted')
        return redirect('cat')

    context = {
        'name':cats
    }
    return render(request, 'ims/delete.html', context)

@login_required(login_url=('login'))
@allowed_users(allowed_roles=['admin'])
def restock(request, pk):
    products = Product.objects.get(id=pk)
    form = RestockForm(request.POST or None, instance=products)
    if form.is_valid():
        products = form.save(commit=False)
        products.save()

        return redirect('product')

    context = {
        'products' : products,
        'form' : form
    }

    return render(request, 'ims/productdetails.html', context)

@login_required(login_url=('login'))
@allowed_users(allowed_roles=['admin','staff'])
def StaffProduct(request):
    products = Product.objects.all()
           
    context = {
        'products':products,
    }
    return render(request, 'ims/staffproduct.html', context)

def StaffProductDetails(request, pk):
    products = Product.objects.get(id=pk)
    sales_form = SalesForm(request.POST or None, instance=products)
    count_form = CountForm(request.POST or None, instance=products)
    if sales_form.is_valid() or count_form.is_valid():
        products = sales_form.save()
        products = count_form.save()
        products.save()
        messages.success(request, 'successfully updated')
            
        return redirect('/productdetails_staff/'+str(products.id))
    
    context ={
        'products' : products,
        'sales_form' : sales_form,
        'count_form' : count_form
    }
    return render(request, 'ims/productdetails_staff.html', context)


def ProductDetails(request, pk):
    products = Product.objects.get(id=pk)
    sales_form = SalesForm(request.POST or None, instance=products)
    reorder_form = ReorderForm(request.POST or None, instance=products)
    count_form = CountForm(request.POST or None, instance=products)
    if sales_form.is_valid() or reorder_form.is_valid() or count_form.is_valid():
        products = sales_form.save(commit=False)
        products = reorder_form.save(commit=False)
        products = count_form.save(commit=False)
        products.save()
        messages.success(request, 'successfully updated')
            
        return redirect('/productdetails/'+str(products.id))
        
    context = {
        'products' : products,
        'reorder_form' : reorder_form,
        'count_form' : count_form,
        'sales_form' : sales_form
    }

    return render(request, 'ims/productdetails.html', context)

def report(request):
    return render(request, 'ims/report.html')






 



