import logging
import time

from django.conf import settings
from django.core.management import BaseCommand
from django.db.models import Min
from django.utils import timezone

from qlinks.models import Link

logger = logging.getLogger('qlinks.checker')


class Command(BaseCommand):
    verbosity = 0
    help = 'Check QLinks for broken redirect destinations.'

    def add_arguments(self, parser):
        parser.add_argument('-d', '--daemon', action='store_true',
                            help='run as a daemon, constantly checking links')

    def handle(self, *args, **options):
        self.verbosity = int(options['verbosity'])

        try:
            if options['daemon']:
                self.daemon()
            else:
                self.check_links()
        except KeyboardInterrupt:
            self.stdout.write('Interrupted.')

    def daemon(self):
        while True:
            self.check_links()

            next_check = Link.objects.aggregate(min=Min('next_check'))['min']
            wait = (next_check - timezone.now()).total_seconds()
            if wait > 0:
                if self.verbosity > 2:
                    self.stdout.write(f'Sleeping for: {wait:.0f} seconds')
                time.sleep(wait)

    def check_links(self):
        for link in Link.objects.filter(next_check__lte=timezone.now()).order_by('next_check'):
            if self.verbosity > 0:
                self.stdout.write(f'Checking URL for {link.short}: {link.long}')

            was_working = link.is_working
            link.check_url()
            if was_working and not link.is_working:
                self.stdout.write(f'URL for {link.short} just broke: {link.long}')

            time.sleep(settings.QLINKS_CHECK_THROTTLE)
