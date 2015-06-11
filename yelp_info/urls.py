from django.conf.urls import patterns, include, url
from django.contrib import admin
from yelp_info.models import Episode

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/', include(admin.site.urls))
)
