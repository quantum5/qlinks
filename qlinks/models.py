import random
from datetime import timedelta
from functools import cached_property

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from qlinks.cdn_cache import cdn_cache
from qlinks.fields import ShortURLField
from qlinks.health import check_url


def compute_next_check():
    min_check = settings.QLINKS_CHECK_MIN.total_seconds()
    max_check = settings.QLINKS_CHECK_MAX.total_seconds()
    return timezone.now() + timedelta(seconds=random.randint(min_check, max_check))


class Link(models.Model):
    short = ShortURLField(max_length=64, verbose_name=_('short link slug'), unique=True, blank=True,
                          help_text=_('the part of URL after / that will redirect to the long URL, '
                                      'e.g. https://my.short.link/[slug]'))
    long = models.URLField(max_length=512, verbose_name=_('long URL'))
    created_on = models.DateTimeField(verbose_name=_('creation time'), auto_now_add=True)
    updated_on = models.DateTimeField(verbose_name=_('last update'), default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                   verbose_name=_('created by'))
    is_working = models.BooleanField(verbose_name=_('URL is working'))
    last_check = models.DateTimeField(verbose_name=_('last time URL was checked'))
    next_check = models.DateTimeField(verbose_name=_('the next time the URL will be checked'),
                                      default=compute_next_check, db_index=True)

    def __str__(self):
        return self.short or '/'

    @cached_property
    def short_url(self):
        return settings.QLINKS_CANONICAL + self.short

    def check_url(self, save=True):
        self.is_working = check_url(self.long)
        self.last_check = timezone.now()
        self.next_check = compute_next_check()

        if save:
            self.save()
    check_url.alters_data = True

    def purge_cdn(self):
        if cdn_cache:
            cdn_cache.purge(self.short_url)
    purge_cdn.alters_data = True
