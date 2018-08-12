from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^welcome/(?P<id>\d+)$', views.welcome),
    url(r'^logout$', views.logout)
]