from django.shortcuts import (
    render, redirect, HttpResponse, reverse, get_object_or_404
)
from django.contrib import messages
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from products.models import Product
from discount_codes.forms import DiscountForm
from discount_codes.models import DiscountCode


def view_cart(request):
    """
    A view to return the cart content page.
    """

    context = {
        'discount_form': DiscountForm(),
    }

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, item_id):
    """
    Add quantity of product to cart.
    """

    product = get_object_or_404(Product, pk=item_id)
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


def get_discount_code(request, code):
    """
    Verify whether the user-inputted code
    is valid. If valid, return the discount
    amount, otherwise, return 0.
    """

    try:
        discount_code = DiscountCode.objects.get(code=code)
        messages.info(request, "Successfully added coupon")
        return discount_code.discount
    except ObjectDoesNotExist:
        messages.error(request, "This code does not exist")
        return 0


def add_discount(request, *args, **kwargs):
    """
    Handle user submission of a discount code
    via the discount code form, updating the
    session's discount code if the input is valid.
    """

    discount_form = DiscountForm(request.POST or None)
    discount = request.session.get('discount')
    if discount_form.is_valid():
        code = discount_form.cleaned_data.get('code').upper()
        discount_code = get_discount_code(request, code)
        request.session['discount'] = discount_code
        return redirect(reverse('view_cart'))


def remove_discount(request):
    """
    Remove discount from session.
    """
    
    del request.session['discount']
    messages.info(request, "Successfully removed coupon")
    return redirect(reverse('view_cart'))
