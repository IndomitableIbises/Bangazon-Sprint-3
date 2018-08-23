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
    url(r'^sell$', views.sell_product, name='sell'),
    url(r'^products$', views.list_products, name='list_products'),
    url(r'^edit_profile$', views.edit_profile, name='edit_profile'),
    url(r'^profile$', views.profile, name='profile'),
    # Category URLS
    url(r'^categories$', views.list_categories, name='list_categories'),
    url(r'^add_category$', views.add_category, name='add_category'),
]