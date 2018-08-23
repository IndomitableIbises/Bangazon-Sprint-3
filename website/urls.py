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
    #Product URLs
    url(r'^sell$', views.sell_product, name='sell'),
    url(r'^products$', views.list_products, name='list_products'),
    path('products/<int:pk>/', views.ProductDetailView, name='product_detail'),
    #####################
    # Profile URLs
    url(r'^edit_profile$', views.edit_profile, name='edit_profile'),
    url(r'^profile$', views.profile, name='profile'),
    #####################
    # Category URLS
    url(r'^categories$', views.list_categories, name='list_categories'),
    url(r'^add_category$', views.add_category, name='add_category'),
]