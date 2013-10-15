from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied


def auth_or_403(request, perm, obj):
    """
    The name "auth" refers to authorization, not authentication

    Check if the session user has a an object-level permission.  This function
    utilizes the extended ModelBackend called ModelBackendPlus located in
    backends.py

    ModelBackendPlus checks for the perm and if that fails, it checks for the
    perm appended with _own.  If the user has the *_own perm and obj.user ==
    request.user, it returns true.  If the perm check returns false, issue a
    403 response. The perm argument follows the standard format:
    <package>.<codename>
    """

    #print "auth_or_403"
    #print "auth_or_403" + request.user.username

    if not request.user.has_perm(perm, obj):
        # msg = 'You are not authorized to perform this action'
        # print msg
        raise PermissionDenied
    else:
        return True

