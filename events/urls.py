from django.conf.urls import url

from events import views

urlpatterns = [
    url(r'^addevent/$', views.addevent),
    url(r'^eventslist/$', views.eventslist),
    url(r'^eventdetail/(?P<id>\d+)/$', views.eventdetail),
    # url(r'^eventdetail/$', views.eventdetail),
]
