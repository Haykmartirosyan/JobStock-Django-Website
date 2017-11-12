from django.conf.urls import url
from . import views


app_name = 'Accounts'
urlpatterns = [
    url(r'^$', views.Login_view, name='index'),
]