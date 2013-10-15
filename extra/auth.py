from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group



def create_perms_read(sender, **kwargs):
    """
    This syncdb hooks takes care of adding a view permission too all our
    content types.
    """

    print "auth.create_perms_read"

    # for each of our content types
    for content_type in ContentType.objects.all():
        # build our permission slug
        codename = "read_%s" % content_type.model

        # if it doesn't exist..
        if not Permission.objects.filter(content_type=content_type,
                                         codename=codename):
            # add it
            Permission.objects.create(content_type=content_type,
                                      codename=codename,
                                      name="Can read %s" % content_type.name)
            print "created auth_perm: %s" % codename


def create_perms_own(sender, **kwargs):
    """
    This function adds verb_*_own, permissions for each content type.  For
    create, edit, delete, and read verbs.name.  The default role (assigned to
    every registered user) will be assigned the _own permission for all
    content types and the ModelBackend will be extended such that when
    had_perm() is passed an model instance and the user does not have the
    requested permission, it will check to see if the user has the _own
    version of the permission and that the object was created by that user.
    If that is the case, has_perm will return true.
    """

    print "auth.create_perms_own"

    verbs = ('create', 'change', 'read', 'delete')
    for content_type in ContentType.objects.all():
        for verb in verbs:
            codename = "%s_%s_own" % (verb, content_type.model)
            name = "Can %s own %s" % (verb, content_type.model)
            if not Permission.objects.filter(content_type=content_type,
                                             codename=codename):
                Permission.objects.create(
                    content_type=content_type,
                    codename=codename,
                    name=name
                )
                print "created auth_perm: %s" % codename


def add_perms_default(group):
    """
    Assign verb_*_own permissions for all content types and for all verbs (
    create, edit, view, delete) to the group
    """

    print "add_perms_default"

    for perm in Permission.objects.filter(codename__endswith="own"):

        # group.permissions is a ManyRelatedManager object that is not
        # iterable. It has methods like add() and remove() and such.  It also
        # has a method all() that returns a set of Permission instances that
        # is iterable
        #
        # Remarkably, Python is able to check if perm (a Permission instance) is
        # in the QuerySet (set of Permission instances) returned by the .all()
        # method.  That is freaking amazing

        if not perm in group.permissions.all():
            group.permissions.add(perm)
            print "added auth_perm: %s to auth_group:%s" % \
                  (perm.codename, group.name)
        #else:
        #    print "auth_perm: %s already added to auth_group: %s" % \
        #          (perm.codename, group.name)

def add_perms_locations(group):

    print "add_perms_locations"

    codenames = ['add_location',
                 'change_location',
                 'delete_location',
                 'read_location']

    for codename in codenames:
        try:
            perm = Permission.objects.get(codename=codename)
        except Permission.DoesNotExist:
            continue
        if not perm in group.permissions.all():
            group.permissions.add(perm)
            print "added auth_perm: %s to auth_group: %s" % \
                  (perm.codename, group.name)


def add_perms_ticket_assignment(group):

    print "add_perms_ticket_assignment"

    perms = [
        {
            'codename': 'set_ticket_assignee',
            'name': 'Can set ticket assignee'
        }
    ]

    try:
        content_type = ContentType.objects.get(name="location")
    except ContentType.DoesNotExist:
        print "extra.groups add_perms_ticket_assignment ERROR"
        return

    for perm in perms:
        try:
            permission = Permission.objects.get(codename=perm['codename'])
        except Permission.DoesNotExist:
            permission = Permission.objects.create(
                content_type=content_type,
                codename=perm['codename'],
                name=perm['name']
            )
            print "created auth_perm: %s" % perm['name']

        if not permission in group.permissions.all():
            group.permissions.add(permission)
            print "assigned auth_perm: %s to auth_group: %s" % \
                (permission.codename, group.name)


def get_group_or_create(name):

    try:
        return Group.objects.get(name=name)
    except Group.DoesNotExist:
        return Group.objects.create(name=name)


def create_group_default(sender, **kwargs):
    """
    Create the default group
    """
    print "create_group_default"
    group = get_group_or_create("default")
    add_perms_default(group)


def create_group_pi(sender, **kwargs):
    """
    Create the pi group
    """
    print "create_group_pi"
    group = get_group_or_create("pi")
    add_perms_default(group)
    add_perms_locations(group)
    add_perms_ticket_assignment(group)







