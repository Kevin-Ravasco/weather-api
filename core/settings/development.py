from .base import *  # NOQA

ALLOWED_HOSTS = ['*']

# INSTALLED_APPS += [
#     'debug_toolbar',
# ]

# add debug toolbar middleware as high as possible
# MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
