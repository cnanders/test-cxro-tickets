from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from locations.models import *
from extra.shortcuts import auth_or_403
from django.contrib import messages

@login_required
def get(request, id=None):
    if id:
        model_set = Location.objects.filter(parent_id__exact=id)
    else:
        model_set = Location.objects.filter(parent_id__exact=None)
    return render(request, 'locations/get.html', {'model_set': model_set,})


@login_required
@require_POST
def post(request, id=None):
    if id:
        model = get_object_or_404(Location, pk=id)
        url = reverse('locations.views.post', args=[id])
    else:
        model = None
        url = reverse('locations.views.post')
    form = LocationForm(request.POST)
    if form.is_valid():
        location = form.save(commit=False)
        location.parent = model
        location.save()
        messages.success(request, "A new location has been created.")
        return HttpResponseRedirect(reverse('locations.views.get'))
    else:
        return render(request, 'locations/new.html', {'form': form,
                                                      'model': model,
                                                      'url': url})


@login_required()
def new(request, id=None):
    if id:
        model = get_object_or_404(Location, pk=id)
        url = reverse('locations.views.post', args=[id])
    else:
        model = None
        url = reverse('locations.views.post')
    form = LocationForm()
    return render(request, 'locations/new.html', {'form': form,
                                                  'model': model,
                                                  'url': url,})

@login_required()
@require_POST
def put(request, id):
    model = get_object_or_404(Location, pk=id)
    #auth_or_403(request, 'locations.change_location', model)
    form = LocationForm(request.POST, instance=model)
    if form.is_valid():
        form.save()
        #location = form.save(commit=False)
        #location.parent = model
        #location.save()
        messages.success(request, "The location has been updated.")
        return HttpResponseRedirect(reverse('locations.views.get'))
    else:
        return render(request, 'locations/edit.html', {'form': form,
                                                       'model': model, })


@login_required()
def edit(request, id):
    model = get_object_or_404(Location, pk=id)
    #auth_or_403(request, 'locations.change_location', model)
    form = LocationForm(instance=model)
    return render(request, 'locations/edit.html', {'form': form,
                                                 'model': model})


@login_required()
@require_POST
def delete(request, id):
    model = get_object_or_404(Location, pk=id)
    #auth_or_403(request, 'locations.delete_location', model)
    model.delete()
    messages.success(request, "The location has been deleted.")
    return HttpResponseRedirect(reverse('locations.views.get'))


