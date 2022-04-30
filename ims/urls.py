from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cat', views.cat, name='cat'),
    path('brand', views.brand, name='brand'),
    path('product', views.product, name='product'),
    path('edit/<str:pk>/', views.UpdateProduct, name='edit'),
    path('update_brand/<str:pk>/', views.UpdateBrand, name='update_brand'),
    path('update_cat/<str:pk>/', views.UpdateCat, name='update_cat'),
    path('delete_product/<str:pk>/', views.DeleteProduct, name='delete_product'),
    path('delete_brand/<str:pk>/', views.DeleteBrand, name='delete_brand'),
    path('delete_cat/<str:pk>/', views.DeleteCat, name='delete_cat'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),
    path('staff/', views.staffPage, name='staffpage'),
    path('staffproduct/', views.StaffProduct, name='staffproduct'),
    path('productdetails/<str:pk>/', views.ProductDetails, name='productdetails'),
    path('report/', views.report, name='report'),
    path('productdetails_staff/<str:pk>/', views.StaffProductDetails, name='productdetails_staff'),
    path('count/<str:pk>/', views.recordCount, name='count'),
    path('upload', views.simple_upload, name= 'upload'),
    path('export_sales', views.export_sales_csv, name= 'export_sales'),
    path('export_count', views.export_count_csv, name= 'export_count'),
    path('export_restock', views.export_restock_csv, name= 'export_restock'),
    
]