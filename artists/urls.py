from django.conf.urls import patterns, url

from artists import views

# 7 endpoints for each model (5 for REST + 2 forms)
# list, detail, create, update, delete
# new form, edit form.
#
# I could adopt a pattern that all HTTP verbs != GET put the HTTP verb in the URL
# which would at least reflect the RESTful concept in the limitation of browsers
# only accepting GET and POST.  I think maybe I like this because /post, /id/put,
# and /id/delete will never be seen by the user since they quickly redirect after
# they do their thing.  What would the views be called?
#
# list: 		/				get
# detail: 		/id				get_detail
# create: 		/post			post
# update: 		/id/put			put
# delete: 		/id/delete		delete
# new form: 	/form			form_new                (not REST)
# edit form: 	/id/form		form_edit               (not REST)
#
# this requires four template files: get.html, get_detail.html, new.html,
# and edit.html located at templates/model_name

urlpatterns = patterns('',
    # list GET to /
    url(
        r'^$',
        views.artists_get,
        name='artists_get'
    ),
    # detail GET to /id
    url(
        r'^(?P<artist_id>\d+)/$',
        views.artists_get_detail,
        name='artists_get_detail'
    ),
    # create (nonREST) should be POST to /
    url(
        r'^post$',
        views.artists_post,
        name='artists_post'
    ),
    # update (nonREST) should be PUT to /id
    url(
        r'^(?P<artist_id>\d+)/put/$',
        views.artists_put,
        name='artists_put'
    ),
    # delete (nonREST) should be DELETE to /id
    url(
        r'^(?P<artist_id>\d+)/delete/$',
        views.artists_delete,
        name="artists_delete"
    ),
     # form (new) GET to /new
    url(
        r'^new/$',
        views.artists_new,
        name="artists_new"
    ),
     # form (edit) GET to /id/edit
    url(
        r'^(?P<artist_id>\d+)/edit/$',
        views.artists_edit,
        name="artists_edit"
    ),

    # albums
    url(
        r'^(?P<artist_id>\d+)/albums/post/$',
        views.albums_post,
        name='albums_post'
    ),
    url(
        r'^(?P<artist_id>\d+)/albums/new/$',
        views.albums_form_new,
        name='albums_new'
    ),
    url(
        r'^(?P<artist_id>\d+)/albums/$',
        views.albums_get,
        name='albums_get'
    ),


    #url(r'^(?P<artist_id>\d+)/albums/$', views.albums_index, name='albums_index'),
    #url(r'^(?P<artist_id>\d+)/albums/(?P<album_id>\d+)$', views.albums_detail, name='albums_detail'),
    #url(r'^(?P<artist_id>\d+)/albums/(?P<album_id>\d+)/tracks$', views.tracks_index, name='tracks_index'),
    #url(r'^(?P<artist_id>\d+)/albums/(?P<album_id>\d+)/tracks/(?P<track_id>\d+)$', views.tracks_detail, name='tracks_detail'),
)