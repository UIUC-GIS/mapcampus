from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from tastypie.api import Api

from apps.api.res import BuildingResource, EdgeResource, NodeResource, RouteResource

v1_api = Api(api_name='v1')
v1_api.register(BuildingResource())
v1_api.register(EdgeResource());
v1_api.register(NodeResource());
v1_api.register(RouteResource())

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^analytics/', TemplateView.as_view(template_name='analytics.html')),
    url(r'^contact/', TemplateView.as_view(template_name='contact.html')),
    url(r'^edit/', TemplateView.as_view(template_name='edit.html')),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
) + staticfiles_urlpatterns()
