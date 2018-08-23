from django.conf.urls import url
from django.urls import path

from . import views

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #####################
    # Login/Register URLs
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    #####################
    #  Product URLs
    url(r'^sell$', views.sell_product, name='sell'),
    url(r'^products$', views.list_products, name='list_products'),
    #####################
    # Profile URLs
    url(r'^edit_profile$', views.edit_profile, name='edit_profile'),
    url(r'^profile$', views.profile, name='profile'),
    #####################
    # Category URLS
    url(r'^categories$', views.list_categories, name='list_categories'),
    url(r'^add_payment$', views.add_payment, name='add_payment'),
    url(r'^payment_success$', views.payment_success, name='payment_success'),
    url(r'^payment/(?P<pk>\d+)/delete$', views.delete_payment, name="delete_payment"),
    url(r'^payments$', views.list_payments, name="list_payments"),
    url(r'^add_category$', views.add_category, name='add_category'),

]