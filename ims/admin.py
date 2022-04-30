from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Brand, Category, Product, Staff, ProductReport
from import_export.admin import ImportExportModelAdmin
from .resources import ProductResource

# Register your models here.



@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    

class ProductHistory(SimpleHistoryAdmin):
    list_display = ["id", "name", "status"]
    history_list_display = ["status"]
    search_fields = ['name', 'user__username']

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Staff)
admin.site.register(ProductReport, ProductHistory)
