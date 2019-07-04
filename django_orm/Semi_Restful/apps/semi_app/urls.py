from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.shows),
    url(r'^shows/new$', views.add_page),
    url(r'^shows/create$', views.add),
    url(r'^shows/(?P<id>\d+)$', views.info),
    url(r'^shows/(?P<id>\d+)/edit$', views.edit_page),
    url(r'^shows/(?P<id>\d+)/update$', views.edit),
    url(r'^shows/(?P<id>\d+)/destroy$', views.destroy)
]