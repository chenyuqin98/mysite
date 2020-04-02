from django.urls import path

from . import views

app_name = 'wx_login'
urlpatterns = [
    path('', views.wx_login, name='wx_login'),
    path('wx_regist/', views.wx_regist, name='wx_regist')
]
