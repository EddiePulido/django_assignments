from django.conf.urls import url
from . import views # the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$',views.new),
    url(r'^create$',views.create),
    url(r'^(?P<number>\d+)$', views.number),
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^(?P<number>\d+)/delete$', views.destroy)
]