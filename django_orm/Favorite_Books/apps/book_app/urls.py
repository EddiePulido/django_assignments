from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^books$', views.show_books),
    url(r'^books/(?P<id>\d+)$', views.book_page),
    url(r'^add/(?P<id>\d+)$', views.add_favorite),
    url(r'^add_book$', views.add_book),
    url(r'^update$', views.update),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^unfavorite/(?P<id>\d+)$', views.unfavorite)
]