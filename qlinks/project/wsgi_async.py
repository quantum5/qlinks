import os

import gevent.monkey

gevent.monkey.patch_all()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qlinks.settings.local')

from django.core.wsgi import get_wsgi_application  # noqa

application = get_wsgi_application()
