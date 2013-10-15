from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import Group


def register(request):
    if request.method == 'POST':

        username = request.POST.get('username', '')
        password = request.POST.get('password1', '')
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()

            # Automatically log the user into the site.  Note: the
            # UserCreationForm model has password1 and password2 as properties,
            # not vanilla 'password'

            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                messages.success(request, "Thanks for registering! You have "
                    " been automatically logged in."
                )

                # Assign the user a group of "default".  All other group
                # assignment should be done by an administrator

                group = Group.objects.get(name="default")
                if group is not None:
                    user.groups.add(group)
                    messages.success(request, "You have been assigned to the"
                        "group %s" % group.name)


            return HttpResponseRedirect(reverse('artists_get'))
    else:
        form = UserCreationForm()
    return render(
        request,
        "registration/register.html",
        {
        'form': form,
        }
    )
