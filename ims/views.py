from urllib import response
from django import contrib
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Product, Category, Brand, Staff, ProductReport, Debtor
from .forms import CatForm, BrandForm, CountForm, ProductForm, CreateUserForm, ReorderForm, RestockForm, SalesForm, ProductUpdateForm, ProductReportForm, DebtForm, DebtUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from .resources import ProductResource
from tablib import Dataset
from django.core.paginator import Paginator
import csv
from django.http import HttpResponse, JsonResponse
import datetime
from .filters import reportFilter
from datetime import date
from dateutil.relativedelta import relativedelta

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
    paginator = Paginator(Product.objects.all(), 5)
    page = request.GET.get('page')
    product_page = paginator.get_page(page)
    nums = "a" *product_page.paginator.num_pages
    
    context = {
        'products':products,
        'product_page':product_page,
        'nums':nums,
    }
    return render(request, 'ims/staffproduct.html', context)

@login_required(login_url=('login'))
@admin_only
def dashboard(request):
    products = Product.objects.all()
    cats = Category.objects.all()
    brands = Brand.objects.all()
    staffs = Staff.objects.all()
    reports = ProductReport.history.order_by('-quantity_sold')[:7]
    report = ProductReport.history.order_by('-quantity_restocked')[:7]
    pr = Product.objects.order_by('-available')[:7]
    
    total_staffs = staffs.count()
    total_products = products.count()
    total_cats = cats.count()
    total_brands = brands.count()

    context = {
        'pr':pr,
        'reports':reports,
        'report':report,
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
            messages.success(request, 'successfully created')
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
            messages.success(request, 'successfully created')
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
    paginator = Paginator(Product.objects.all(), 5)
    page = request.GET.get('page')
    product_page = paginator.get_page(page)
    nums = "a" *product_page.paginator.num_pages
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,  'successfully created')
            return redirect('product')
    context = {
        'form':form,
        'products':products,
        'product_page':product_page,
        'nums':nums,
    }
    return render(request, 'ims/product.html', context)

@login_required(login_url=('login'))
@allowed_users(allowed_roles=['admin'])
def UpdateProduct(request, pk):
    products = Product.objects.get(id=pk)
    form = ProductUpdateForm(instance=products)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, instance=products)
        if form.is_valid():
            form.save()
            print("Edited")
            messages.success(request, (products.name) + ' successfully updated')
            return redirect('product')
    context = {
        'form':form,
    }
    return render(request, 'ims/edit.html', context)


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
    return render(request, 'ims/edit.html', context)


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
    return render(request, 'ims/edit.html', context)


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
    if sales_form.is_valid():
        products = sales_form.save(commit=False)
        products.quantity -= products.quantity_sold
        products.available = products.quantity
        products.total_price = products.quantity_sold*products.price
        products.save()
        sales_report = ProductReport(
            id = products.id,
            last_updated = products.last_updated,
            name = products.name,
            quantity_sold = products.quantity_sold,
            count = products.count,
            quantity_restocked = products.quantity_restocked,
            available = products.available,
            variance = products.variance,
            price = products.price,
            total_price = products.total_price
        )
        sales_report.save()
        messages.success(request, 'successfully updated')    
        return redirect('staffpage')
    
    context ={
        'products' : products,
        'sales_form' : sales_form,      
    }
    return render(request, 'ims/productdetails_staff.html', context)

def recordCount(request, pk):
    products = Product.objects.get(id=pk)
    count_form = CountForm(request.POST or None, instance=products)
    if count_form.is_valid():
        products = count_form.save(commit=False)
        products.variance = products.count - products.available
        products.save()
        count_report = ProductReport(
            id = products.id,
            last_updated = products.last_updated,
            name = products.name,
            quantity_sold = products.quantity_sold,
            count = products.count,
            quantity_restocked = products.quantity_restocked,
            available = products.available,
            variance = products.variance,
            price = products.price,
            total_price = products.total_price
        )
        count_report.save()
        messages.success(request, 'successfully updated')
        return redirect('staffpage')
    context ={
        'products' : products,
        'count_form' : count_form,      
    }
    return render(request, 'ims/count.html', context) 
        

def ProductDetails(request, pk):
    products = Product.objects.get(id=pk)
    restock_form = RestockForm(request.POST or None, instance=products)
    reorder_form = ReorderForm(request.POST or None, instance=products)
    if restock_form.is_valid() or reorder_form.is_valid():
        products = restock_form.save(commit=False)
        products.quantity += products.quantity_restocked
        products.available = products.quantity
        products = reorder_form.save(commit=False)
        products.save()
        restock_form = RestockForm()
        reorder_form = ReorderForm()
        restock_report = ProductReport(
            id = products.id,
            last_updated = products.last_updated,
            name = products.name,
            quantity_sold = products.quantity_sold,
            count = products.count,
            quantity_restocked = products.quantity_restocked,
            available = products.available,
            variance = products.variance,
            price = products.price,
            total_price = products.total_price
        )
        restock_report.save()
        messages.success(request, 'successfully updated')
        return redirect('product')
    
    
    context = {
        'products' : products,
        'restock_form' : restock_form,
        'reorder_form' : reorder_form  
    }
    return render(request, 'ims/productdetails.html', context)

def report(request):
    form = ProductReportForm(request.POST or None)
    reports = ProductReport.objects.all()
    sim_report = ProductReport.history.all()
    if request.method == 'POST':
        reports = ProductReport.objects.filter(last_updated__range=[  form['start_date'].value(),form['end_date'].value()])
    paginator = Paginator(ProductReport.history.all(), 5)
    page = request.GET.get('page')
    sim_report_page = paginator.get_page(page)
    nums = "a" *sim_report_page.paginator.num_pages
    refil = reportFilter(request.GET, queryset=sim_report)
    sim_report = refil.qs
    
    
    context = {
        'reports' : reports,
        'sim_report': sim_report,
        'sim_report_page': sim_report_page,
        'nums': nums,
        'refil': refil,
        'form': form,
    }
    return render(request, 'ims/report.html', context)

def simple_upload(request):
    if request.method == 'POST':
        product_resource = ProductResource()
        dataset = Dataset()
        new_product = request.FILES['myfile']
        
        imported_data = dataset.load(new_product.read().decode(), format='csv', headers=False)
        print(imported_data)
        result = product_resource.import_data(dataset, dry_run=True)  # Test the data import
        
        if not result.has_errors():
            product_resource.import_data(dataset, dry_run=False)  # Actually import now
            
    return render(request, 'ims/upload.html')


@login_required(login_url=('login'))
@allowed_users(allowed_roles=['admin','staff'])
def debtors(request):
    products = Product.objects.all()
    debts = Debtor.objects.all()
    debt_report = Debtor.history.all()
    debt_form = DebtForm()
    if request.method == 'POST':
        debt_form = DebtForm(request.POST)
        if debt_form.is_valid():
            debt_form.save()
            messages.success(request, 'successfully created')
            return redirect('debt')

        
    context = {
        'products': products,
        'debts': debts,
        'debt_report': debt_report,
        'debt_form': debt_form
    }
    return render(request, 'ims/debt.html', context)


def UpdateDebt(request, pk):
    debts = Debtor.objects.get(id=pk)
    form = DebtUpdateForm(instance=debts)
    if request.method == 'POST':
        form = DebtUpdateForm(request.POST, instance=debts)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully updated')
            return redirect('debt')
    context = {
        'form':form,
    }
    return render(request, 'ims/edit.html', context)

def DeleteDebt(request, pk):
    debts = Debtor.objects.get(id=pk)
    if request.method == 'POST':
        debts.delete()
        messages.success(request, 'successfully Deleted')
        return redirect('debt')

    context = {
        'debts':debts
    }
    return render(request, 'ims/delete.html', context)
    


def export_sales_csv(request):
    
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition']='attachment; filename = Sales History'+str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Staff', 'Product', 'Price', 'Sold', 'Price Sold', 'Available', 'Date'])
    
    reports = ProductReport.history.all()
    
    for report in reports:
        writer.writerow([report.history_user, report.name, report.price, report.quantity_sold, report.total_price, report.available, report.last_updated])
    
    return response

def export_count_csv(request):
    
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition']='attachment; filename = Count History'+str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Staff', 'Product', 'Available', 'Count', 'Variance', 'Date'])
    
    reports = ProductReport.history.all()
    
    for report in reports:
        writer.writerow([report.history_user, report.name, report.available, report.count, report.variance, report.last_updated])
    
    return response

def export_restock_csv(request):
    
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition']='attachment; filename = Restock History'+str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Staff', 'Product', 'Available', 'Restocked', 'Date'])
    
    reports = ProductReport.history.all()
    
    for report in reports:
        writer.writerow([report.history_user, report.name, report.available, report.quantity_restocked, report.last_updated])
    
    return response




 



