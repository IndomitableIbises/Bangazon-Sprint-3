from django.db import models
from django.contrib.auth.models import User
from .payment import Payment
from .product import Product
from django.urls import reverse



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, blank=True, null=True, on_delete=models.PROTECT)
    completed_date = models.DateField(blank=True, null=True)
    shopping_cart = models.ManyToManyField(Product)

    class Meta:
        db_table = 'Order'

    def __str__(self):
        return self.id