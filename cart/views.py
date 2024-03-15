from django.shortcuts import (
    render, redirect, HttpResponse, reverse, get_object_or_404
)
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """
    A view to return the cart content page.
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add quantity of product to cart.
    """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        if product.stock >= cart[item_id] + quantity:
            cart[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity \
                    to {cart[item_id]}')
        else:
            messages.error(
                request, f'Error {product.name} has only \
                {product.stock} units left, you have {cart[item_id]} \
                    in your cart')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjust the quantity of a product on the cart page.
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        if quantity > product.stock:
            messages.error(
                request, f'Error {product.name} has only \
                {product.stock} units left')
        else:
            cart[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity \
                to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
    Remove a product from the cart.
    """

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
