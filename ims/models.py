import email
from tkinter import CASCADE
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now_add=True)
    qnty = models.IntegerField(blank=True, null=True)
    open_str = models.IntegerField(blank=True, null=True)
    str_qnty = models.IntegerField(blank=True, null=False)
    restock = models.IntegerField(default=0, blank=True, null=True)
    sales = models.IntegerField(default=0, blank=True, null=True)
    count = models.IntegerField(default=0, blank=True, null=True)
    variance = models.IntegerField(default=0, blank=True)
    available = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=100, blank=True)
    reorder_level = models.IntegerField(default=10, blank=True, null=False)
    price = models.IntegerField(blank=True, null=True)
    choices = (
        ('General', 'General'),
        ('Special', 'Special'),
    )
    mode_of_sales = models.CharField(max_length=50, choices=choices, default="General", blank=True, null=True)

    def __str__(self):
        return self.name
    
    
class Staff(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Entry(models.Model):
    product = models.ManyToManyField(Product)
    entry_date = models.DateField(auto_now_add=True)
    rep_name = models.ForeignKey(Staff, on_delete=models.CASCADE)



    
    
    

