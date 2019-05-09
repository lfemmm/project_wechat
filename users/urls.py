from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^userinformation/$', views.userinformation),
    url(r'^updateinformation/$', views.updateinformation),
]
