from django.forms import ModelForm, HiddenInput
from artists.models import Album, Artist


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        # fields = ['name']
        # widgets = {'user': HiddenInput}
        exclude = ['user']


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        #fields = ['name', 'artist']
        #widgets = {'artist': HiddenInput}
        #fields = ['name', 'artist']
        exclude = ['artist', 'user']

