from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^$', views.index),
    (r'^(?P<strip_id>\d+)/$', views.strip),
)
