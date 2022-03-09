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
        fields = ('name', 'category', 'brand', 'str_qnty', 'price')

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'}),
            'brand' : forms.Select(attrs={'class':'form-control'}),
            'str_qnty' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.TextInput(attrs={'class':'form-control'}),
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')

        for product in Product.objects.all():
            if product.name == name:
                raise forms.ValidationError(name + ' is already created')
        return name


class SalesForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['mode_of_sales', 'sales',]

        widgets= {
            'mode_of_sales': forms.Select(attrs={'class':'form-control'}),
            'sales' : forms.TextInput(attrs={'class':'form-control'})
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
        fields = ('restock', 'price')

        widgets = {
            'restock' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.TextInput(attrs={'class':'form-control'})
        }

class ReorderForm(ModelForm):
    class Meta:
        model = Product
        fields = ('reorder_level',)

        widgets = {
            'reorder_level' : forms.TextInput(attrs={'class':'form-control'})
        }