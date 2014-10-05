from django.conf.urls import url

from game import views

urlpatterns = [
    url(r'^$', views.game, name='game'),
    url(r'^search/$', views.searchGame, name='searchGame'),
    url(r'^add/$', views.addToGame, name='addToGame'),
    url(r'^status/$', views.SendGameStatus, name='SendGameStatus'),
]