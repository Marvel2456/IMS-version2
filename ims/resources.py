from import_export import resources
from .models import Product

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('name',)
        exclude = ('id',)
        fields = ('name', 'quantity_restocked', 'price')
        