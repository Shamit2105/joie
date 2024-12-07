from django.db import models
from items.models import Item
from users.models import User
from django.core.exceptions import ValidationError

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField()
    address = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.clean()
        self.item.quantity -= self.quantity
        if self.item.quantity < 0:
            raise ValueError("Insufficient stock.")
        self.item.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} by {self.customer.username} for {self.item.title}"
