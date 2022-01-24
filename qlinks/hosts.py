from django.conf import settings
from django_hosts import host, patterns

from qlinks.urls import admin, short

host_patterns = patterns(
    '',
    host(settings.QLINKS_ADMIN_HOST, admin, name='admin'),
    host('', short, name='shortener'),
)
