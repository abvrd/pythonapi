from django.conf.urls import patterns, include, url

urlpatterns = patterns('api.views',
    url(r'^$', 'home'),
    url(r'^home$', 'home'),
    url(r'^feed$', 'feed'),
    url(r'^movies', 'movies'),
)