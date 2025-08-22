from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name='home'),
    path("employees/", views.employees, name='employees'),
    path("customers/", views.customers, name='customers'),
    path("products/", views.products, name='products'),
    path("cart/", views.cart, name='cart'),
    #path("checkout/", views.checkout, name='checkout'),
    path('buy/<int:product_id>/', views.buy_product, name='buy_product'),
    path('checkout/<int:product_id>/', views.checkout, name='checkout'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path("checkoutMultipleProducts/", views.checkoutMultipleProducts, name='checkoutMultipleProducts')

]
