from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    
    url(r'^tree/(?P<treename>binarysearchtree)/data', 'apps.tree.views.data'),
    url(r'^tree/(?P<treename>binarysearchtree)', 'apps.tree.views.index'),

    url(r'^tree/(?P<treename>avltree)/data', 'apps.tree.views.data'),
    url(r'^tree/(?P<treename>avltree)', 'apps.tree.views.index'),

    url(r'^tree/(?P<treename>redblacktree)/data', 'apps.tree.views.data'),
    url(r'^tree/(?P<treename>redblacktree)', 'apps.tree.views.index'),

    ('^.*$', redirect_to, {'url': '/tree/binarysearchtree'}),
)
