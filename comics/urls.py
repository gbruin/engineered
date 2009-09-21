from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^$', views.latest),
    (r'^(?P<strip_id>\d+)/$', views.strip),
    (r'^random/$', views.random),
)
