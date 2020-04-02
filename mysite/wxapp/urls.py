from django.urls import path

from . import views

# app_name = 'wxapp'
urlpatterns = [
    path('', views.wxapp, name='wxapp'),
    path('search/', views.search, name='search'),
]