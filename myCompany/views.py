from django.shortcuts import render, HttpResponse, redirect
from .models import Employees, Customers, Products
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')


def employees (request):
    employees = Employees.objects.all()
    return render(request, 'employees.html', {'Employees': employees})


def customers (request):
    customers = Customers.objects.all()
    return render(request, 'customers.html', {'Customers': customers})


def products(request):
    products = Products.objects.all()
    return render(request, 'products.html', {'Products': products})


def buy_product(request, product_id):
    product = Products.objects.get(id=product_id)
    return render(request, 'buy_confirmation.html', {'product': product})


def cart(request):
    cart = request.session.get('cart', [])
    products = Products.objects.filter(id__in=cart)
    return render(request, 'cart.html', {'Products': products})



#def checkout(request):
   # products = Products.objects.all()
  #  return render(request, 'checkout.html', {'Products': products})


def checkout(request, product_id):
    selected_products = []
    product = Products.objects.get(id=product_id)
    selected_products.append(product)
    #products = Products.objects.all()
    return render(request, 'checkout.html', {'selected_products': selected_products})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id not in cart:
        cart.append(product_id)
    request.session['cart'] = cart

    return JsonResponse({'cart_item_count': len(cart)})


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
    request.session['cart'] = cart
    return redirect('cart')





