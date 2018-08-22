from django.conf.urls import url

from . import views

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^sell$', views.sell_product, name='sell'),
    url(r'^products$', views.list_products, name='list_products'),
    # url(r'^edit-profile$', views.edit_profile, name='edit_profile'),
    # Category URLS
    url(r'^categories$', views.list_categories, name='list_categories'),
    url(r'^order$', views.order_view, name='order'),
    url(r'^delete_order_item/(?P<item_id>[0-9]+)/$', views.delete_order_item, name='delete_order_item'),
    url(r'^delete_order/(?P<order_id>[0-9]+)/$', views.delete_order, name='delete_order'),
]