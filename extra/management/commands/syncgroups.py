from extra import auth
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def handle(self, *args, **options):

        auth.create_perms_read(self)
        auth.create_perms_own(self)
        auth.create_group_default(self)
        auth.create_group_pi(self)