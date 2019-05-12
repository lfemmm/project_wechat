from django.conf.urls import url

from apihtml import views

urlpatterns = [
    url(r'^api/$', views.api),
    url(r'^user_login/$', views.user_login),
    url(r'^user_logout/$', views.user_logout),
    url(r'^user_information/$', views.user_information),
    url(r'^user_updateinformation/$', views.user_updateinformation),

    url(r'^get_company/$', views.get_company),

    url(r'^accident_type/$', views.accident_type),
    url(r'^accident_rank/$', views.accident_rank),
    url(r'^accidents_list/$', views.accidents_list),
    url(r'^accident_detail/$', views.accident_detail),
    url(r'^accident_add/$', views.accident_add),

    url(r'^event_type/$', views.event_type),
    url(r'^events_list/$', views.events_list),
    url(r'^event_detail/$', views.event_detail),
    url(r'^event_add/$', views.event_add),

    url(r'^accident_analysis/$', views.accident_analysis),
    url(r'^event_analysis/$', views.event_analysis),
]
