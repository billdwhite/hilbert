from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'bintree.json$', 'apps.data.views.bintree_json'),
    url(r'avltree.json$', 'apps.data.views.avltree_json'),
    url(r'redblacktree.json$', 'apps.data.views.redblacktree_json'),
)
