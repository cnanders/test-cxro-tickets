from django.conf.urls import patterns, url

urlpatterns = patterns('tickets.views',
    url(r'^$', 'get', name='tickets_get'),
    url(r'^new$', 'new', name='tickets_new'),
    url(r'^post$', 'post', name='tickets_post'),

    url(r'^(\d+)/comments$', 'comments_get', name="comments_get"),
    url(r'^(\d+)/comments/new$', 'comments_new', name="comments_new"),
    url(r'^(\d+)/comments/post$', 'comments_post', name="comments_post"),




)
