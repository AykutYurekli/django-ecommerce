from django.db import models
from django.conf import settings
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.total_price()
        return total

    def __str__(self):
        return f"Cart of {self.user.username}"


class CartItem(models.Model):

    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.amount

    def __str__(self):
        return f"{self.product.name} | Amount: {self.amount}"
