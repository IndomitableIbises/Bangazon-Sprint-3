# Bangazon Online Marketplace

The Bangazon online marketplace is a totally functional, not incomplete site that allows users to post products for sale, buy products from other users, store payment methods, add products to a cart, and complete an order. 

## To get Bangazon Running:

You'll need the following:
- Django 
- A virtual environment

1. Clone down this repository into a sibling directory to your virtual environment. 
1. Start your virtual environment. 
1. If using a faker factory, populate database with data
1. Run server

## Order
  With no products, orders or payment:
- /order will show a blank screen

-order history will say there is no order history

  With completed orders:
  
-/order_history will display past orders and allow redirect to order detail of any order

-/order_detail will show the details of a past order on redirect

  With open order and products but no payment:
  
-/order will display, products will display if in shopping cart many-to-many table

-no payment will appear and no submit button to allow advance to complete screen

  With open order, products and a payment linked to the active user:
  
-/order will show payment options and allow you to complete the order and move to a thank you screen with a redirect to home.
