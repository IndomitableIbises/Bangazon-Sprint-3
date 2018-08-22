#Author:  Erin Agobert
#Purpose:  This file seeds the database using scripts from django-seed

from django.core.management.base import BaseCommand
from django_seed import Seed
seeder = Seed.seeder()
import random
from website.models import User, Category, Product, Payment, Order

class Command(BaseCommand):

  def handle(self, *args, **options):
    """ 
    This function seeds the website database:
      *args = database table name
      **options = # of rows to create in table
    """

    #Seeds User table
    seeder.add_entity(User, 5, {
      'password': lambda x: seeder.faker.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True),
      'last_login': lambda x: seeder.faker.date_time_this_month(before_now=True, after_now=False, tzinfo=None),
      'is_superuser': lambda x: seeder.faker.boolean(chance_of_getting_true=0),
      'username': lambda x: seeder.faker.user_name(),
      'first_name': lambda x: seeder.faker.first_name(),
      'email': lambda x: seeder.faker.email(),
      'is_staff': lambda x: seeder.faker.boolean(chance_of_getting_true=0),
      'is_active': 'True',
      'date_joined': lambda x: seeder.faker.date_time_this_year(before_now=True, after_now=False, tzinfo=None),
      'last_name': lambda x: seeder.faker.last_name(),
    })

    #Seeds Category table
    cat_name_list = ['electronics', 'books', 'movies', 'jewelry', 'clothing', 'furniture', 'shoes', 'supplies', 'beauty']

    seeder.add_entity(Category, 5, {
      'cat_name': lambda x: seeder.faker.word(ext_word_list=cat_name_list)
    })

    #Seeds Product table
    seeder.add_entity(Product, 25, {
      'title': lambda x: seeder.faker.catch_phrase(),
      'description': lambda x: seeder.faker.sentence(nb_words=5, variable_nb_words=True, ext_word_list=None),
      'price': lambda x: random.randint(1, 1000),
      'quantity': lambda x: random.randint(1, 10),
    })

    #Seeds Payment table
    seeder.add_entity(Payment, 10, {
      'name': lambda x: seeder.faker.credit_card_provider(card_type=None),
      'account_num': lambda x: seeder.faker.credit_card_number(card_type=None),
      'active': seeder.faker.boolean(chance_of_getting_true=95),
    })

    #Seeds Order table
    seeder.add_entity(Order, 20)

    inserted_pks = seeder.execute()