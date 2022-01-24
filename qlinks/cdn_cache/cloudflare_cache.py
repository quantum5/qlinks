from CloudFlare import CloudFlare
from django.conf import settings

from qlinks.cdn_cache import BaseCDNCache


class CloudflareCDNCache(BaseCDNCache):
    cf: CloudFlare
    zone: str

    def __init__(self):
        self.cf = CloudFlare(token=getattr(settings, 'QLINKS_CDN_CLOUDFLARE_API_TOKEN', None))
        self.zone = settings.QLINKS_CDN_CLOUDFLARE_ZONE_ID

    def purge(self, url: str) -> None:
        self.cf.zones.purge_cache.post(self.zone, data={
            'files': [url],
        })
