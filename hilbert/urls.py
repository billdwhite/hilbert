from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    
    url(r'^tree/(?P<treename>\w+)/?(?P<N>\d+)?/data', 'apps.tree.views.data'),
    url(r'^tree/(?P<treename>\w+)/?(?P<N>\d+)?', 'apps.tree.views.index'),
    url(r'^', 'apps.tree.views.index'),
    
    ('^foo/(?P<id>\d+)/$', redirect_to, {'url': '/tree/'}),
)
