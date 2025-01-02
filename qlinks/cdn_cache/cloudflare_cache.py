from cloudflare import Cloudflare
from django.conf import settings

from qlinks.cdn_cache import BaseCDNCache


class CloudflareCDNCache(BaseCDNCache):
    cf: Cloudflare
    zone: str

    def __init__(self):
        self.cf = Cloudflare(api_token=getattr(settings, 'QLINKS_CDN_CLOUDFLARE_API_TOKEN', None))
        self.zone = settings.QLINKS_CDN_CLOUDFLARE_ZONE_ID

    def purge(self, url: str) -> None:
        self.cf.cache.purge(zone_id=self.zone, files=[url])
