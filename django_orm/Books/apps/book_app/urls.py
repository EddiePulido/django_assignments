from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$',views.authors),
    url(r'^books/(?P<id>\d+)$',views.book_page),
    url(r'^authors/(?P<id>\d+)$',views.author_page),
    url(r'^add_author$', views.add_author),
    url(r'^add_book$',views.add_book),
    url(r'^add_author_to_book$',views.add_author_to_book),
    url(r'^add_book_to_author$',views.add_book_to_author)
]
