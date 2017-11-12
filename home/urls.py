from django.conf.urls import url, include
from . import views


app_name='Home'
urlpatterns = [
    url(r'^$', views.Home.as_view(), name='index'),


]