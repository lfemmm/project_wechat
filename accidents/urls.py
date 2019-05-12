from django.conf.urls import url

from accidents import views

urlpatterns = [
    url(r'^addaccident/$', views.addaccident),
    url(r'^accidentslist/$', views.accidentslist),
    url(r'^accidentdetail/(?P<pk>\d+)/$', views.accidentdetail),
    url(r'^types/$', views.typeslist),
    url(r'^ranks/$', views.rankslist),
]
