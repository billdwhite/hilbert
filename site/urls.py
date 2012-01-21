from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settsiteings.STATIC_ROOT}),
    url(r'^data/', include('site.apps.data.urls')),
    url(r'^$', include('site.apps.treevis.urls')),
    # url(r'^$', 'site.views.home', name='home'),
    # url(r'^site/', include('site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
