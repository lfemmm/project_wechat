from django.conf.urls import url

from accidents import views

urlpatterns = [
    url(r'^addaccident/$', views.addaccident),
    url(r'^accidentslist/$', views.accidentslist),
    url(r'^accidentdetail/(?P<id>\d+)/$', views.accidentdetail),
]
