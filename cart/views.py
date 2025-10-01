from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart, CartItem
from products.models import Product
from django.contrib.auth.decorators import login_required
from orders.models import Order, OrderItem


def get_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
    
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)

    return cart


@login_required
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = get_cart(request)

    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.amount += 1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            cart=cart,
            product=product,
            amount=1
        )
    return redirect('cart:cart_detail')

@login_required
def cart_remove(request, item_id):
    try:
        item = CartItem.objects.get(id=item_id, cart__user=request.user)
        item.delete()

    except CartItem.DoesNotExist:
        pass

    return redirect('cart:cart_detail')



@login_required
def cart_detail(request):
    
    cart = get_cart(request)

    return render(
        request, 'cart/cart_detail.html',{'cart': cart}
    )



@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)

    order = Order.objects.create(user=request.user)

    for item in cart.items.all():
        OrderItem.objects.create(
            order=order,
            product=item.product,
            amount=item.amount,
            price=item.product.price
        )
    cart.items.all().delete()

    return redirect("orders:order_detail",order_id=order.id)
