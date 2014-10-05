from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from players import views as playerViews
import players

from game import views as gameViews
import game

admin.autodiscover()


router = DefaultRouter()
router.register(r'players', playerViews.PlayerViewSet)
router.register(r'games', gameViews.GameViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),

    url(r'^user/', include('players.urls')),
    url(r'^game/', include('game.urls')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),

    url(r'^admin/', include(admin.site.urls)),
)
