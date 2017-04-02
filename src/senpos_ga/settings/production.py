from .base import *

import dj_database_url


# ALLOWED_HOSTS += [
#     'senpos-ga.herokuapp.com'
# ]

ALLOWED_HOSTS += ['*']

DEBUG = False

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
