from django.db import models
from django.forms import ModelForm, HiddenInput

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True, null=True)
    parent = models.ForeignKey("Location", null=True)
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class LocationForm(ModelForm):

    # How can I show part of the form to some people and not others? I think
    # I need to manually build the form.  That kind of sucks.  For now I wont
    # deal with this

    class Meta:
        model = Location
        # fields = ['name']
        # widgets = {'user': HiddenInput}
        exclude = ['parent',]
