
from django.core.management.base import BaseCommand
from django_seed import Seed
seeder = Seed.seeder()
import random
from website.models import User, Profile, Category, Product, Order, Payment

class Command(BaseCommand):

  def handle(self, *args, **options):
    """ 
    This function seeds the website database:
      *args = database table name
      **options = # of rows to create in table
    """

    seeder.add_entity(User, 5)
    seeder.add_entity(Profile, 5)
    seeder.add_entity(Category, 5)
    seeder.add_entity(Product, 25)
    seeder.add_entity(Order, 20)
    seeder.add_entity(Payment, 20)

    inserted_pks = seeder.execute()