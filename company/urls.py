from django.conf.urls import url

from company import views

urlpatterns = [
    url(r'^companylist/$', views.companylist),
]
