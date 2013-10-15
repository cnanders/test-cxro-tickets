# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from artists.models import *
from artists.forms import *
from extra.shortcuts import auth_or_403


# list, detail, create, update, delete (new form, edit form)

@login_required
def artists_get(request):
    artists = Artist.objects.all()
    form = ArtistForm()
    return render( request, 'artists/get.html', {'artists': artists,
                                                 'form': form})


def artists_get_detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    has_perm = request.user.has_perm('artists.read_artist', artist)

    return render(
        request,
        'artists/get_detail.html',
        {
            'artist': artist,
            'has_perm': has_perm,
        }
    )

@login_required
@require_POST
def artists_post(request):
    form = ArtistForm(request.POST)
    if form.is_valid():
        artist = form.save(commit=False)
        artist.user = request.user
        artist.save()
        # redirect
        return HttpResponseRedirect(reverse('artists_get'))
    else:
        return render(request, 'artists/new.html', {'form': form})


@login_required()
@require_POST
def artists_put(request, artist_id):

    # Create a form to edit an existing Article, but use POST data to populate
    # the form.

    artist = get_object_or_404(Artist, pk=artist_id)
    auth_or_403(request, 'artists.change_artist', artist)
    form = ArtistForm(request.POST, instance=artist)
    if form.is_valid():
        form.save()
        # redirect to lists or detail
        return HttpResponseRedirect(reverse('artists_get'))
    else:
        return render(
            request,
            'artists/edit.html',
            {
                'form': form,
                'artist_id': artist_id,
            }
        )

@login_required()
@require_POST
def artists_delete(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    auth_or_403(request, 'artists.delete_artist', artist)
    artist.delete()
    return HttpResponseRedirect(reverse('artists_get'))


@login_required()
def artists_new(request):
    #form = ArtistForm(
    #    initial = {
    #        'user': request.user.id
    #    },
    #)
    form = ArtistForm()
    return render(
        request,
        'artists/new.html',
        {
            'form': form,
        }
    )

@login_required()
def artists_edit(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    auth_or_403(request, 'artists.change_artist', artist)
    form = ArtistForm(instance=artist)
    return render(
        request,
        'artists/edit.html',
        {
            'form': form,
            'artist': artist
        }
    )


def albums_form_new(request, artist_id):

    #form = AlbumForm(
    #    initial ={
    #        'artist': artist_id
    #    }
    #)
    # form.artist = artist_id
    # form.artist = artist

    #return HttpResponse(artist)
    #return HttpResponse(serializers.serialize('json', artist))

    artist = get_object_or_404(Artist, pk=artist_id)
    form = AlbumForm()
    return render(
        request,
        'albums/form_new.html',
        {
            'form': form,
            'artist': artist,
        }
    )

@login_required
@require_POST
def albums_post(request, artist_id):

    #form = AlbumForm(
    #    request.POST,
    #    initial ={
    #        'user': request.user.id
    #    }
    #)

    artist = get_object_or_404(Artist, pk=artist_id)
    form = AlbumForm(request.POST)
    if form.is_valid():
        album = form.save(commit=False)
        album.artist = artist
        album.user = request.user
        album.save()
        # redirect
        return HttpResponseRedirect(reverse('artists_get'))
    else:
        return render(
            request,
            'albums/form_new.html',
            {
                'form': form,
                'artist': artist
            }
        )


def albums_get(request, artist_id):
    return None