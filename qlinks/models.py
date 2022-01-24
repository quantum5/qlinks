from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Link(models.Model):
    short = models.SlugField(max_length=64, verbose_name=_('short link slug'), unique=True, blank=True,
                             help_text=_('the part of URL after / that will redirect to the long URL, '
                                         'e.g. https://my.short.link/[slug]'))
    long = models.URLField(max_length=512, verbose_name=_('long URL'))
    created_on = models.DateTimeField(verbose_name=_('creation time'), auto_now_add=True)
    updated_on = models.DateTimeField(verbose_name=_('last update'), default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                   verbose_name=_('created by'))
    is_working = models.BooleanField(verbose_name=_('URL is working'))
    last_check = models.DateTimeField(verbose_name=_('last time URL was checked'))

    def __str__(self):
        return self.short or '/'
