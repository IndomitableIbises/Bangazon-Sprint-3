from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

# Create your models here.
class Payment(models.Model):
    """Payment

    Author: Hayley Landsberg
    
    This class represents the Payment resource in the database.
    """
    
    name = models.CharField(max_length=250)
    account_num = models.IntegerField()
    active = models.BooleanField() 
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'payment'

        def __str__(self):
            return self.name

        # def get_absolute_url(self):
        #     return reverse("website:payment_detail", kwargs={"pk": self.pk}) 
