from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, HiddenInput
from locations.models import Location

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=20)
    #choices=(
    #    'Not started',
    #    'In progress',
    #    'Done',
    #    'Deferred'
    #),

class Priority(models.Model):
    name = models.CharField(max_length=10)
    def __unicode__(self):
        return self.name

class Ticket(models.Model):
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)
    user = models.ForeignKey(User, related_name='ticket')
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    assignee = models.ForeignKey(User,
                                 null=True,
                                 related_name='assigned_ticket')
    priority = models.ForeignKey(Priority)


class Comment(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    ticket = models.ForeignKey(Ticket)


class Attachment(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField()
    ext = models.TextField()
    name = models.TextField()
    comment = models.ForeignKey(Comment)


class TicketForm(ModelForm):

    # How can I show part of the form to some people and not others? I think
    # I need to manually build the form.  That kind of sucks.  For now I wont
    # deal with this

    class Meta:
        model = Ticket
        # fields = ['name']
        # widgets = {'user': HiddenInput}
        exclude = ['user', 'date', 'assignee']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'date', 'ticket']

