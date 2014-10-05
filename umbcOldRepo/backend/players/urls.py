from django.conf.urls import url

from players import views

urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
]