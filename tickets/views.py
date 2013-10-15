from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from tickets.models import *


@login_required
def get(request):
    tickets = Ticket.objects.all()
    form = TicketForm()
    return render(
        request,
        'tickets/get.html',
        {
            'tickets': tickets,
        }
    )

@login_required
@require_POST
def post(request):
    form = TicketForm(request.POST)
    comment_form = CommentForm(request.POST)
    if form.is_valid() and comment_form.is_valid():
        ticket = form.save(commit=False)
        ticket.user = request.user
        ticket.save()
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.ticket = ticket
        comment.save()
        # redirect
        return HttpResponseRedirect(reverse('tickets_get'))
    else:
        return render(request, 'tickets/new.html', {'form': form})


@login_required()
def new(request):
    form = TicketForm()
    comment_form = CommentForm()
    return render(request, 'tickets/new.html', {'form': form,
                                                'comment_form': comment_form})

# Comment

@login_required
@require_POST
def comments_post(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.ticket = ticket
        comment.save()
        return HttpResponseRedirect(reverse('tickets_get'))
    else:
        return render(request, 'comments/new.html', {'form': form})

@login_required()
def comments_get(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    return render(request, 'comments/get.html', {'ticket': ticket,})

@login_required()
def comments_new(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    form = CommentForm()
    return render(request, 'comments/new.html', {'form': form,
                                                 'ticket': ticket,})



