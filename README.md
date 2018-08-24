# Welcome to Bangazon

This web application is the source code for the Bangazon e-commerce web site. It is powered by Python and Django.

Students, you are inheriting a basic implementation that provides the following features:

1. User registration 
1. User login 
1. User logout 
1. Adding a product 
1. Listing products

Please consult the backlog of issues and work with your product owner to implement the top priority tickets for your sprints.

## To begin work

1. The team lead should clone this repository, then push it to your team's Github repo.
1. Alert your manager when this is complete and all backlog issues will be imported into your project.
1. Each teammate should clone the repository.
1. In the `djangazon` directory that gets created, run the migrations with `python manage.py migrate`

## Helpful Resources

### Django Models and Migrations

Using the requirements above create a [model](https://docs.djangoproject.com/en/1.10/topics/db/models/) for each resource, and use [migrations](https://docs.djangoproject.com/en/1.10/topics/migrations/) to ensure your database structure is up to date.

### Templates

[Django template language](https://docs.djangoproject.com/en/1.10/ref/templates/language/)

### Form Helpers

Django, like Angular, has many built-in [helper tags and filters](https://docs.djangoproject.com/en/1.10/ref/templates/builtins/) when building the site templates. We strongly recommend reading this documentation while building your templates.


## URLS
- '/' - homepage
- '/login' - login page and link to registration
- '/category' - all categories, with three products in each category
- '/account' - account settings
- '/category' - to page with all categories and three itmes from each category
- '/category/<categoryID>' - to page with all products within a category
- '/product/<searchTerm>' - to page with all products that match a search term
- '/product/<productID>' - to detail page for a single product
  
  
  
  ## Order
  With no products, orders or payment -
- /order will show a blank screen
-order history will say there is no order history

  With completed orders -
-/order_history will display past orders and allow redirect to order detail of any order
-/order_detail will show the details of a past order on redirect

  With open order and products but no payment -
-/order will display, products will display if in shopping cart many-to-many table
-no payment will appear and no submit button to allow advance to complete scree

  With open order, products and a payment linked to the active user -
-/order will show payment options and allow you to complete the order and move to a thank you screen with a redirect to home.
