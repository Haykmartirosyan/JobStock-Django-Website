from django.conf.urls import url
from . import views


app_name = 'Accounts'
urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^$', views.signin, name='login'),
]