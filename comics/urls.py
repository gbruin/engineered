from django.conf.urls.defaults import *
from feeds import LatestEntries
import views

feeds = {
    'latest': LatestEntries,
}

urlpatterns = patterns('',
    (r'^$', views.latest),
    url('^contact/$', views.contact, name='contact_view'),
    url('^random/$', views.random, name='random_view'),
    url(r'^archive/$', views.archive, name='archive_view'),
    url(r'^(?P<strip_id>\d+)/$', views.strip, name='strip_view'),
    # enable feeds (RSS)
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds}, name='feeds_view'),
)
