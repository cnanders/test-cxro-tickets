from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Artist(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Aerosmith, Taylor Swift, etc.",
        unique=True,
    )
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']



class Album(models.Model):
    artist = models.ForeignKey(Artist)
    # artists = models.ManyToManyField(Artist)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User)

class Song(models.Model):
    name = models.CharField(
        max_length=100,
    )
    album = models.ForeignKey(Album)
    user = models.ForeignKey(User)


# This is a comment and I want to see what happens when I type more than 80
# characters.  Wow, look at that!  It wrapped automatically.  That is really
# freaking sweet.  Note that this wrap is not a soft wrap.  It is an actual
# wrap, which means if I were to copy+paste this into something there would
# be line breaks