from django.contrib import admin
from .models import Brand, Category, Product, Entry, Staff

# Register your models here.


class EntryCreateAdmin(admin.ModelAdmin):
    list_display = ['rep_name','entry_date',]

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Staff)
admin.site.register(Entry, EntryCreateAdmin)
