from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from qlinks.models import Link


def short_link(request, path):
    link = get_object_or_404(Link.objects.values_list('long', flat=True), short=path)
    return HttpResponseRedirect(link, headers={
        'X-Powered-By': settings.QLINKS_POWERED_BY
    })
