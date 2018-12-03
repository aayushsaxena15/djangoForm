from django.urls import path

from . import views
from django.conf.urls import url
from django.contrib import admin
from .views import articlespage, successpage
urlpatterns = [
     url(r'^$', articlespage, name='homepage'),
     url(r'^success$', successpage, name='successpage'),  
]
