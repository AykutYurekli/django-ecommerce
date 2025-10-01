from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem
from .models import Order, OrderItem
from .form import OrderCreateForm


@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)

    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save() 

            for item in cart.items.all():
                OrderItem.objects.create(order=order,product=item.product,amount=item.amount,price=item.product.price)

            cart.items.all().delete()

            return redirect("orders:order_detail", order_id=order.id)

    else:
        form = OrderCreateForm()

    return render(request, "orders/checkout.html", {"form": form, "cart": cart})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    total = order.total_price()

    return render(request, "orders/order_detail.html", {"order": order,"total": total})
