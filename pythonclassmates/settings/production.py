from .base import *
import django_heroku

# Activate Django-Heroku.
django_heroku.settings(locals())

DEBUG = False
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME'),
#     }
# }

#         "USER": os.getenv('DB_USER'),
#         "PASSWORD": os.getenv('PASSWORD'),
#         "HOST": os.getenv('DB_HOST'),
#         "PORT": 5433,

try:
    from .local import *
except ImportError:
    pass
