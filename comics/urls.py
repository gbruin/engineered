from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^$', views.latest),
    (r'^random/$', views.random),
    url(r'^(?P<strip_id>\d+)/$', views.strip, name='strip_view'),
)
