from django.core.management.base import BaseCommand

from data.issues import fetch_issues, import_issue


class Command(BaseCommand):
    help = 'Import issues opened by newcomers'

    COLLECTIONS = staticmethod(fetch_issues)
    IMPORT_DATA = staticmethod(import_issue)

    def handle(self, *args, **options):
        # for data in self.COLLECTIONS('github'):
        #    self.IMPORT_DATA('github', data)
        # for data in self.COLLECTIONS('gitlab'):
        #    self.IMPORT_DATA('gitlab', data)
        for data in self.COLLECTIONS('test'):
            self.IMPORT_DATA('test', data)
