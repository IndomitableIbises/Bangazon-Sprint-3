from django.contrib.auth.models import User
from django.db import models

"""
created by: pzc
purpose of module: model for profile
notes: this model has a one-to-one relationship with the user model
"""

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    class Meta:
        db_table = "profile"
