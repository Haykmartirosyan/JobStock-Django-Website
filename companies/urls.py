from django.conf.urls import url
from . import views


app_name='Companies'
urlpatterns = [
    url(r'^$', views.Companies_view, name='index'),
    url(r'^(?P<pk>\d+)/$', views.company_detail.as_view(), name="single-company"),
]