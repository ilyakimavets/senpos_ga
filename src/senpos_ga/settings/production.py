from .base import *

import dj_database_url


ALLOWED_HOSTS += [
    'senpos-ga.herokuapp.com'
]

# static files handle
MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DEBUG = False

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
