from .base_settings import *

DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default = os.getenv('DATABASE_URL'))
    }

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
