from django.conf.urls import url

from apihtml import views

urlpatterns = [
    url(r'^api/$', views.api),
    url(r'^user_login/$', views.user_login),
    url(r'^user_logout/$', views.user_logout),
]
