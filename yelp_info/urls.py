from django.conf.urls import patterns, include, url
from django.contrib import admin
from yelp_info import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/', include(admin.site.urls)),
    url(r'^$', views.get_template, name="show_page")
)
