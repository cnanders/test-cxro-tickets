from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group


def add_read_permissions(sender, **kwargs):
    """
    This syncdb hooks takes care of adding a view permission too all our
    content types.
    """
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
            print "created auth_permission: %s" % codename


def add_own_permissions(sender, **kwargs):
    """
    This syncdb hook adds verb_*_own, permissions for each content type.  For
    create, edit, delete, and view verbs.name.  The default role (assigned to
    every registered user) will be assigned the _own permission for all
    content types and the ModelBackend will be extended such that when
    had_perm() is passed an model instance and the user does not have the
    requested permission, it will check to see if the user has the _own
    version of the permission and that the object was created by that user.
    If that is the case, has_perm will return true.
    """

    # CHANGE VERB TO 'CHANGE' NOT EDIT.  ALSO NEED TO DO BELOW

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
                print "created auth_permission: %s" % codename


def create_default_group(sender, **kwargs):
    """
    Create the default group and assign verb_*_own permissions for all
    content types and for all verbs (create, edit, view, delete)
    """
    group = Group.objects.get(name="default")
    if not group:
        group = Group.objects.create(name="default")
        print "created auth_group: name=default"

    # Loop through all verb_content-type_own perms and make sure the group has
    # each one of them

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
            print "adding auth_perm: %s to auth_group:default" % perm.codename













