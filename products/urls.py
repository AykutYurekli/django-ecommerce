from django.urls import path

from . import views
app_name = 'products'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/shoe/', views.product_category_shoe, name='product_category_shoe'),
    path('category/hat/', views.product_category_hat, name='product_category_hat'),
    path('category/tshirt/', views.product_category_tshirt, name='product_category_tshirt'),
    path('category/accessories/', views.product_category_accessories, name='product_category_accessories'),
    path('category/beret/', views.product_category_beret, name='product_category_beret'),
    path('category/sweatshirt/', views.product_category_sweatshirt, name='product_category_sweatshirt'),
    path('category/shirt/', views.product_category_shirt, name='product_category_shirt'),
    path('category/short/', views.product_category_short, name='product_category_short'),
    path('category/pant/', views.product_category_pant, name="product_category_pant"),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/', views.product_detail, name='product_detail'),

]