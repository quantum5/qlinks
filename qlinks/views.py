from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from qlinks.models import Link


def short_link(request, slug):
    link = get_object_or_404(Link.objects.values_list('long', flat=True), short=slug)
    return HttpResponseRedirect(link)
