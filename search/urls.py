from . import views
from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from .views import SearchUserDetails


urlpatterns = [
    path('search', views.SearchUserDetails, name='search'),
]
