from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cat', views.cat, name='cat'),
    path('brand', views.brand, name='brand'),
    path('product', views.product, name='product'),
    path('add_product', views.AddProduct, name='add_product'),
    path('add_brand', views.AddBrand, name='add_brand'),
    path('add_cat', views.AddCategory, name='add_cat'),
    path('update_product/<str:pk>/', views.UpdateProduct, name='update_product'),
    path('update_brand/<str:pk>/', views.UpdateBrand, name='update_brand'),
    path('update_cat/<str:pk>/', views.UpdateCat, name='update_cat'),
    path('delete_product/<str:pk>/', views.DeleteProduct, name='delete_product'),
    path('delete_brand/<str:pk>/', views.DeleteBrand, name='delete_brand'),
    path('delete_cat/<str:pk>/', views.DeleteCat, name='delete_cat'),
    path('count/<str:pk>/', views.count, name='count'),
    path('sales/<str:pk>/', views.sales, name='sales'),
    path('reorder/<str:pk>/', views.reorder, name='reorder'),
    path('restock/<str:pk>/', views.restock, name='restock'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),
    path('staff/', views.staffPage, name='staffpage'),
    path('staffproduct/', views.StaffProduct, name='staffproduct'),
    path('productdetails/<str:pk>/', views.ProductDetails, name='productdetails'),
    path('report/', views.report, name='report')
    
]