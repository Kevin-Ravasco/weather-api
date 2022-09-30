from .base import *  # NOQA

# use development settings with debug = True
if DEBUG:
    from .development import * # NOQA
else:
    from .production import * # NOQA


# For using production settings with debug = True
# if DEBUG:
#     from .production import *
# else:
#     from .development import *
