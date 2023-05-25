from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required()
def cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


@login_required()
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart if already there"""
    """Add a quantity of the specified product to the cart if already there"""
    quantity = 1

    cart = request.session.get('cart', {})

    if id in cart.keys():
        cart[id] += quantity
    else:
        cart[id] = quantity  # Modificación aquí

    request.session['cart'] = cart
        
    messages.success(
        request,
        "Item added to cart!",
        extra_tags="alert-success")
    return redirect('articles_to_sell')


@login_required()
def adjust_cart(request, id):
    """Removes item from cart"""
    cart = request.session.get('cart', {})
    
    if cart[id]:
        cart[id] -= 1
    if cart[id] == 0:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('cart'))
