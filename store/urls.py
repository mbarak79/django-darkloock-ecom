
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cart/', views.cart, name='cart'),
    path('about/', views.about, name='about'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact_us', views.contact, name='contact_us'),
    path('shop', views.shop, name='shop'),
    path('product_detail', views.product_details, name='product_detail'),
   

] 

