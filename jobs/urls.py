from django.conf.urls import url
from . import views


app_name='Jobs'
urlpatterns = [
    url(r'^$', views.Jobs_view, name='index'),
    url(r'^(?P<pk>\d+)/$', views.job_detail.as_view(), name="single-job"),

]