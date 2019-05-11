from django.conf.urls import url

from data_analysis import views

urlpatterns = [
    url(r'^accident_echart/$', views.accident_echart),
    url(r'^event_echart/$', views.event_echart),
]
