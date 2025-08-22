from collections import Counter


def cart_count(request):
    cart = request.session.get('cart', [])
    print("DEBUG raw cart:", cart)
    counts = Counter(cart)
    total_quantity = sum(counts.values())  # total items in cart
    print("DEBUG cart counts:", counts, "total:", total_quantity)

    return {'cart_item_count': total_quantity}
