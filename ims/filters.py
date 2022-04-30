from dataclasses import field
import django_filters
from django_filters import DateFilter
from .models import *

class reportFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="timestamp", lookup_expr='gte')
    # end_date = DateFilter(field_name="timestamp", lookup_expr='lte') 
    class Meta:
        model = ProductReport
        fields = ['last_updated']
        exclude = [
            # 'last_updated',
            'name',
            'quantity_sold',
            'count',
            'quantity_restocked',
            'available',
            'variance',
            'price',
            'total_price',
            'category',
            'brand',
            'timestamp',
            'quantity',
            'store',
            'batch_no',
            'unit',
            'reorder_level',
            'mode_of_sales',
            'status',
            'amount',
        ]