from django.conf.urls import url

from echart import views

urlpatterns = [
    url(r'^accident_echart/$', views.accident_echart),
]
