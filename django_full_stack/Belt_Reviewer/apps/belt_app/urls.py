from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^books$', views.books),
    url(r'^books/(?P<id>\d+)$', views.book_page),
    url(r'^books/add$', views.add_page),
    url(r'^add_book$', views.add_book),
    url(r'^add_review$', views.add_review),
    url(r'^delete_review/(?P<id>\d+)$', views.delete_review),
    url(r'^user/(?P<id>\d+)$', views.user_page),
    url(r'^update_password$',views.update_password),
    url(r'^update_user$', views.update_user)
]

