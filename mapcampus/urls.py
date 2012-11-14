from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template
from tastypie.api import Api

from apps.api.res import EdgeResource, NodeResource

import settings

v1_api = Api(api_name='v1')
v1_api.register(EdgeResource())
v1_api.register(NodeResource())

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^contact/', direct_to_template, {'template': 'contact.html'}),
    url(r'^edit/', direct_to_template, {'template': 'edit.html'}),
    url(r'^$', direct_to_template, {'template': 'home.html'}),
) + staticfiles_urlpatterns()
