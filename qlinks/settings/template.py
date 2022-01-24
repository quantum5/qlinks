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

# qlinks configuration
QLINKS_ADMIN_HOST = r'admin'

# Set to link prefix for short links, e.g. 'https://short.example.com/'
QLINKS_CANONICAL = None
