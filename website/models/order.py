from django.db import models
from django.urls import reverse
from . import models


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT)
    completed_date = models.DateField(blank=True, null=True)
    shopping_cart = models.ManyToManyField(Product, on_delete=models.PROTECT)
