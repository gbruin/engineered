from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^$', views.latest),
    url('^contact/$', views.contact, name='contact_view'),
    url('^random/$', views.random, name='random_view'),
    url(r'^archive/$', views.archive, name='archive_view'),
    url(r'^(?P<strip_id>\d+)/$', views.strip, name='strip_view'),
)
