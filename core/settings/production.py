import os
from .base import *  # NOQA

USING_IP = True

ALLOWED_HOSTS = ['*']


# Github workflow environment for CI/CD
if os.getenv('GITHUB_WORKFLOW'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

ADMINS = [('Kevin O', 'okevin182@gmail.com')]

# More production configuration goes here...