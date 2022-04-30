from django.forms import ModelForm, fields, widgets
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CatForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')

        for category in Category.objects.all():
            if category.name == name:
                raise forms.ValidationError(name + 'already exist')
        return name

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['name']

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')

        for brand in Brand.objects.all():
            if brand.name == name:
                raise forms.ValidationError(name + 'already exist')
        return name

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields =  ('name', 'category', 'brand', 'quantity', 'batch_no', 'unit', 'price', 'status')

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'category' : forms.Select(attrs={'class':'form-control', 'placeholder':'Category'}),
            'brand' : forms.Select(attrs={'class':'form-control', 'placeholder':'Brand'}),
            'quantity' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quantity'}),
            'batch_no' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Batch no'}),
            'unit' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unit'}),
            'price' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Price'}),
            'status' : forms.Select(attrs={'class':'form-control', 'placeholder':'Status'}),
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')

        for product in Product.objects.all():
            if product.name == name:
                raise forms.ValidationError(name + ' is already created')
        return name

class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'brand', 'quantity', 'batch_no', 'unit', 'price', 'status')
        
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'category' : forms.Select(attrs={'class':'form-control', 'placeholder':'Category'}),
            'brand' : forms.Select(attrs={'class':'form-control', 'placeholder':'Brand'}),
            'quantity' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quantity'}),
            'batch_no' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Batch no'}),
            'unit' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unit'}),
            'price' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Price'}),
            'status' : forms.Select(attrs={'class':'form-control', 'placeholder':'Status'}),
        }


class SalesForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ 'mode_of_sales', 'quantity_sold',]

        widgets= {
            'mode_of_sales': forms.Select(attrs={'class':'form-control'}),
            'quantity_sold' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.TextInput(attrs={'class':'form-control'})
        }

class CountForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['count',]

        widgets = {
            'count' : forms.TextInput(attrs={'class':'form-control'})
        }

class RestockForm(ModelForm):
    class Meta:
        model = Product
        fields = [ 'quantity_restocked',]

        widgets = {
            'quantity_restocked' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.TextInput(attrs={'class':'form-control'})
        }

class ReorderForm(ModelForm):
    class Meta:
        model = Product
        fields = ['reorder_level']

        widgets = {
            'reorder_level' : forms.TextInput(attrs={'class':'form-control'})
        }
        
class ProductReportForm(forms.ModelForm):
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)
    class Meta:
        model = ProductReport
        fields = ['start_date', 'end_date']