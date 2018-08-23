from django.conf.urls import url
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
    # url(r'^products/(?<pk>\d+)$', views.ProductDetailView.as_view(), name='product_detail'),

    # url(r'^edit-profile$', views.edit_profile, name='edit_profile'),
    #####################
    # Category URLS
    url(r'^categories$', views.list_categories, name='list_categories'),
    url(r'^add_category$', views.add_category, name='add_category'),
    #####################
]