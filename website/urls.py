from django.conf.urls import url
from django.urls import include, path
from django.views.generic import TemplateView


from . import views

app_name = "website"
urlpatterns = [
    #####################
    # Index/Home URLs
    url(r'^$', views.index, name='index'),
    #####################
    # Login/Register URLs
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    #####################
    #Product URLs
    url(r'^sell$', views.sell_product, name='sell'),
    url(r'^products$', views.list_products, name='list_products'),
    path('products/<int:pk>/', views.ProductDetailView, name='product_detail'),
    path('sell/<int:pk>/', views.ProductDetailView, name='product_post'),
    #####################
    # Profile URLs
    url(r'^edit_profile$', views.edit_profile, name='edit_profile'),
    url(r'^profile$', views.profile, name='profile'),
    #####################
    # Category URLS
    url(r'^categories$', views.list_categories, name='list_categories'),
    url(r'^add_category$', views.add_category, name='add_category'),
    #####################
    # Payment URLs
    url(r'^add_payment$', views.add_payment, name='add_payment'),
    url(r'^payment_success$', views.payment_success, name='payment_success'),
    url(r'^payment/(?P<pk>\d+)/delete$', views.delete_payment, name="delete_payment"),
    url(r'^payments$', views.list_payments, name="list_payments"),
    #####################
    # Order URLS
    url(r'^order$', views.order_view, name='order'),
    url(r'^delete_order_item/(?P<item_id>[0-9]+)/$', views.delete_order_item, name='delete_order_item'),
    url(r'^delete_order/(?P<pk>[0-9]+)/$', views.delete_order, name='delete_order'),
    url(r'^complete_order$', views.complete_order, name='complete_order'),
    url(r'^order_history$', views.order_history, name='order_history'),
    url(r'^order_detail/(?P<pk>[0-9]+)/$', views.order_detail, name='order_detail'),
    url(r'^thankyou$', TemplateView.as_view(template_name='thankyou.html'), name='thankyou'),
    #####################
]