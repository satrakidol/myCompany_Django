from django.shortcuts import render, HttpResponse, redirect
from .models import Employees, Customers, Products
from django.http import JsonResponse
from collections import Counter


# Create your views here.
def home(request):
    return render(request, 'home.html')


def employees(request):
    employees = Employees.objects.all()
    return render(request, 'employees.html', {'Employees': employees})


def customers(request):
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
    cart_counts = Counter(cart)  # e.g. {2: 3, 3: 1, 5: 1}

    products = Products.objects.filter(id__in=cart_counts.keys())

    cart_items = []
    for product in products:
        quantity = cart_counts[product.id]
        subtotal = product.price * quantity

        print("DEBUG add_to_cart: subtotal =", subtotal)

        cart_items.append({
            "product": product,
            "quantity": cart_counts[product.id],
            "subtotal": subtotal
        })

    # Calculate total quantity after building cart_items
    total_quantity1 = sum(item['quantity'] for item in cart_items)
    Total_cost = sum((item['subtotal'] for item in cart_items))

    print("DEBUG add_to_cart: Total_cost =", Total_cost)

    return render(request, "cart.html", {"cart_items": cart_items,
                                         "total_quantity1": total_quantity1,
                                         "subtotal": subtotal,
                                         "Total_cost": Total_cost})



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
    cart.append(product_id)
    request.session['cart'] = cart
    print("DEBUG add_to_cart: product_id =", product_id, "cart =", cart)

    cart_counts = Counter(cart)
   # print('cart_counts: 'cart_counts)
    total_quantity = sum(cart_counts.values())

    return JsonResponse({'cart_item_count': total_quantity})


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    cart = [pid for pid in cart if pid != product_id]  # removes ALL occurrences
    request.session['cart'] = cart
    return redirect('cart')


def reduce_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
    request.session['cart'] = cart
    return redirect('cart')




def checkoutMultipleProducts(request):
    cart = request.session.get('cart', [])
    cart_counts = Counter(cart)

    products = Products.objects.filter(id__in=cart_counts.keys())

    cart_items = []
    for product in products:
        quantity = cart_counts[product.id]
        subtotal = product.price * quantity
        cart_items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal,
        })

    print("DEBUG checkoutMultipleProducts: cart_items =", cart_items)

    total_price = sum(item['subtotal'] for item in cart_items)

    print("DEBUG checkoutMultipleProducts: total_price =", total_price)

    return render(request, "checkoutMultipleProducts.html", {
        "cart_items": cart_items,
        "total_price": total_price,
    })


'''def cart_item_count(request):
    cart = request.session.get('cart', [])
    counts = Counter(cart)
    total_quantity = sum(counts.values())  # sums quantities, not unique IDs
    return {'cart_item_count': total_quantity}'''

