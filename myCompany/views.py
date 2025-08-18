from django.shortcuts import render, HttpResponse
from .models import Employees, Customers, Products


# Create your views here.
def home(request):
    return render(request, 'home.html')


def employees (request):
    employees = Employees.objects.all()
    return render(request, 'employees.html', {'Employees': employees})


def customers (request):
    customers = Customers.objects.all()
    return render(request, 'customers.html', {'Customers': customers})


def products (request):
    products = Products.objects.all()
    return render(request, 'products.html', {'Products': products})


def buy_product(request, product_id):
    product = Products.objects.get(id=product_id)
    return render(request, 'buy_confirmation.html', {'product': product})


def cart(request):
    products = Products.objects.all()
    return render(request, 'cart.html', {'Products': products})


def checkout(request):
    products = Products.objects.all()
    return render(request, 'checkout.html', {'Products': products})
