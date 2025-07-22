import traceback

from django.conf import settings
from django.core.cache import cache
from django.utils.log import AdminEmailHandler

THROTTLE_VARIABLE = 'qlinks_error_email_throttle'
throttle_limit, throttle_duration = getattr(settings, 'QLINKS_EMAIL_THROTTLE', (2, 60))


class ThrottledEmailHandler(AdminEmailHandler):
    def emit(self, record):
        try:
            cache.add(THROTTLE_VARIABLE, 0, throttle_duration)
            count = cache.incr(THROTTLE_VARIABLE)
        except Exception:
            traceback.print_exc()
        else:
            if count > throttle_limit:
                return
        super().emit(record)
