# Author: Raf
from django.db import models


'''
Category Model
Model for Category include the following:
    cat_name is a string defaulted to ""
'''

class Category(models.Model):
    Name = models.CharField(default="", max_length=100)

    class Meta:
        db_table = "Category"

    def __str__(self):
        return self.Name