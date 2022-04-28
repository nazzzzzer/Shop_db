from django.db import models
from mda.models import mod
from mda.models.mod import Product
from mda.models.users import User


class Order(models.Model):
    user = models.ForeignKey(User, related_name='user',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    details = models.CharField(max_length=100,blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=3, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

    # class Meta:
    #     verbose_name_plural = 'order items'