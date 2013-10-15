from django.contrib.auth.backends import ModelBackend


class ModelBackendPlus(ModelBackend):

    def has_perm(self, user_obj, perm, obj=None):
        """
        It is assumed that perm will be one of the Django default perm codes
        like 'delete_comment' or 'change_comment'.  The default users, however,
        will not have the default privileges for the delete and change verbs.
        Instead, they will have '_own' versions of the verbs:
        'change_comment_own', 'delete_comment_own'

        The first step is to call has_perm w/o the object to use standard
        permission checking (do this on purpose).  If the user has the
        permission, return True.
        """
        # print "ModelBackendPlus.has_perm()"

        allowed = ModelBackend.has_perm(self, user_obj, perm)
        if allowed:
            return True

        # The majority of users will fail this check because only non-default
        # auth_groups will have any of the default permissions for the create
        # and delete verbs
        #
        # If an obj is not None, however, we have the chance to check the
        # business rule for the "_own" extension of the perm verb, namely, that
        # the object was created by the user.
        #
        # The idea is that in a conventional RBAC scheme, we would always have
        # a task, i.e., "read" as the lowest child and it would have a parent
        # "read_own" that would need a business rule of "the session user
        # created this model"
        #
        # All of the "_own" permissions verbs would be put into the default
        # auth_group

        if obj is not None:

            # print "ModelBackendPlus.has_perm() obj is not None"

            # Make sure obj has a user property.  If it does not, return
            # False.  Again, we will call ModelBackend.has_perm without the
            # object parameter so that we bypass the built-in object workflow,
            # which is incomplete

            if hasattr(obj, "user"):

                #print "ModelBackendPlus.has_perm() obj has user property"

                # DEBUG
                #a = ModelBackend.has_perm(self, user_obj, perm + '_own')
                #b = obj.user == user_obj
                #
                #print "ModelBackendPlus.has_perm() _own:" + \
                #      "true" if a else "false"
                #print "ModelBackendPlus.has_perm() obj.user = user: " + \
                #      "true" if b else "false"

                return (ModelBackend.has_perm(self, user_obj, perm + '_own') and
                        obj.user == user_obj)
            else:
                return False
        else:
            return False