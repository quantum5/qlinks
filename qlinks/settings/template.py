# This is the settings template. Copy this as local.py
from .base import *  # noqa

SECRET_KEY = 'THIS IS INSECURE PLEASE CHANGE ME'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_ROOT = '/srv/example'
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# qlinks configuration
QLINKS_ADMIN_HOST = r'admin'

# Set to link prefix for short links, e.g. 'https://short.example.com/'
QLINKS_CANONICAL = None

# If you are using a CDN, you can optionally configure it to cache all the
# redirects, and then use a CDN cache backend to purge the cache.
# QLINKS_CDN_CACHE = 'qlinks.cdn_cache.cloudflare_cache.CloudflareCDNCache'
# QLINKS_CDN_CLOUDFLARE_API_TOKEN = ...
# QLINKS_CDN_CLOUDFLARE_API_ZONE_ID = ...

# Automatic link checking settings.
# Minimum and maximum time before next check.
# A time is randomly chosen to spread out the load.
# QLINKS_CHECK_MIN = timedelta(days=6)
# QLINKS_CHECK_MAX = timedelta(days=8)

# Minimum time in seconds between two consecutive checks.
# QLINKS_CHECK_THROTTLE = 1
