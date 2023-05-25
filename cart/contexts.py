from django.shortcuts import get_object_or_404
from items.models import Items


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    Item_to_count = 0

    for id, quantity in cart.items():
        Item_to_buy = get_object_or_404(Items, pk=id)
        total += quantity * Item_to_buy.price
        Item_to_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'Item_to_buy': Item_to_buy})

    return {
        'cart_items': cart_items,
        'total': total,
        'Item_to_count': Item_to_count}
