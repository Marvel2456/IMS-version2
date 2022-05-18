from unicodedata import category
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

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
    name = models.CharField(max_length=150, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=False)
    batch_no = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    reorder_level = models.IntegerField(default=10, blank=True, null=False)

    choices = (
        ('Available', 'Item is currently available'),
        ('Restocking', 'Currently out of stock'),
    )
    status = models.CharField(max_length=20, choices=choices, default="Available", blank=True, null=True)# Available, Restocking
    last_updated = models.DateField(auto_now=True,)
    timestamp = models.DateTimeField(auto_now_add=True,)
    choices = (
        ('General', 'General'),
        ('Promo', 'Promo'),
    )
    mode_of_sales = models.CharField(max_length=50, choices=choices,default="General", blank=True, null=True)
    quantity_sold = models.IntegerField(default=0, blank=True, null=True)
    total_price = models.IntegerField(default=0, blank=True, null=True)
    quantity_restocked = models.IntegerField(default=0, blank=True, null=True)
    count = models.IntegerField(default=0, blank=True, null=True)
    store = models.IntegerField(default=0)
    variance = models.IntegerField(default=0)
    available = models.IntegerField(default=0)
    history = HistoricalRecords()
    
    
    def __str__(self):
        return self.name
    
class ProductReport(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=False)
    batch_no = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    reorder_level = models.IntegerField(default=10, blank=True, null=True)
    

    choices = (
        ('Available', 'Item is currently available'),
        ('Restocking', 'Currently out of stock'),
    )
    status = models.CharField(max_length=20, choices=choices, default="Available", blank=True, null=True)# Available, Restocking
    last_updated = models.DateField(auto_now_add=True, auto_now=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    choices = (
        ('General', 'General'),
        ('Promo', 'Promo'),
    )
    mode_of_sales = models.CharField(max_length=50, choices=choices,default="General", blank=True, null=True)
    quantity_sold = models.IntegerField(default=0, blank=True, null=True)
    total_price = models.IntegerField(default=0, blank=True, null=True)
    amount = models.IntegerField(default=0, blank=True, null=True)
    quantity_restocked = models.IntegerField(default=0, blank=True, null=True)
    count = models.IntegerField(default=0, blank=True, null=True)
    store = models.IntegerField(default=0, blank=True, null=True)
    variance = models.IntegerField(default=0, blank=True, null=True)
    available = models.IntegerField(default=0, blank=True, null=True)
    history = HistoricalRecords()
    
    def __str__(self):
        return self.name
    
    
class Staff(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Debtor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    customer_name = models.CharField(max_length=1000)
    amount_paid = models.FloatField()
    amount_owed = models.FloatField()
    payment_completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
    
    def __str__(self):
        return self.customer_name
