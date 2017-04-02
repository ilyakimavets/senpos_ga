from .base import *

import dj_database_url


ALLOWED_HOSTS += ['senpos-ga.herokuapp.com']
DEBUG = False

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
