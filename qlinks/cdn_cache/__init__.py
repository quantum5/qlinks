from typing import Optional

from django.conf import settings
from django.utils.module_loading import import_string

from qlinks.cdn_cache.base import BaseCDNCache

cdn_cache: Optional[BaseCDNCache]
if settings.QLINKS_CDN_CACHE:
    cdn_cache = import_string(settings.QLINKS_CDN_CACHE)()
else:
    cdn_cache = None
