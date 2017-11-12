from django.conf.urls import url
from . import views


app_name = 'Candidates'
urlpatterns = [
    url(r'^$', views.Candidates_view, name='index'),
    url(r'^(?P<pk>\d+)/$', views.candidate_details.as_view(), name='candidate_details'),

]