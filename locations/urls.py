from django.conf.urls import patterns, url

urlpatterns = patterns('locations.views',
    #url(r'^$', 'get', name='locations_get'),
    #url(r'^new/$', 'new', name='locations_new'),
    #url(r'^post/$', 'post', name='locations_post'),

    url(r'^$', 'get'),
    url(r'^new/$', 'new'),
    url(r'^post/$', 'post'),

    #url(r'^(\d+)/children/$', 'children_get', name="locations_children_get"),
    #url(r'^(\d+)/children/new/$', 'children_new', name="locations_children_new"),
    #url(r'^(\d+)/children/post/$', 'children_post', name="locations_children_post"),

    url(r'^(\d+)/$', 'get'),
    url(r'^(\d+)/new/$', 'new'),
    url(r'^(\d+)/post/$', 'post'),
    url(r'^(\d+)/edit/$', 'edit'),
    url(r'^(\d+)/put/$', 'put'),
    url(r'^(\d+)/delete/$', 'delete'),

)

