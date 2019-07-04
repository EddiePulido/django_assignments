from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^checkout$', views.checkout),
    url(r'^checkout_page$', views.checkout_page)
]