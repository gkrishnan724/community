from django.core.management.base import BaseCommand

from data.mrs import fetch_mrs, import_mr


class Command(BaseCommand):
    help = 'Import mrs opened by newcomers'

    COLLECTIONS = staticmethod(fetch_mrs)
    IMPORT_DATA = staticmethod(import_mr)

    def handle(self, *args, **options):
        # for data in self.COLLECTIONS('github'):
        #    self.IMPORT_DATA('github', data)
        # for data in self.COLLECTIONS('gitlab'):
        #    self.IMPORT_DATA('gitlab', data)
        for data in self.COLLECTIONS('test'):
            self.IMPORT_DATA('test', data)
