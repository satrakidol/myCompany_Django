from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name='home'),
    path("employees/", views.employees, name='employees'),
    path("customers/", views.customers, name='customers'),
    path("products/", views.products, name='products'),
    path("cart/", views.cart, name='cart'),
    path("checkout/", views.checkout, name='checkout'),
    path('buy/<int:product_id>/', views.buy_product, name='buy_product')
]
