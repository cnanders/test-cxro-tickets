from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse

urlpatterns = patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', name="login"),
    url(r'^logout/$', 'logout',
        kwargs={'next_page': '/artists'}, name="logout"
    ),
)

urlpatterns += patterns('accounts.views',
    url(r'^register/$', 'register', name="register")
)

