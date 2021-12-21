from .base import *
DEBUG = False


ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_URL = 'https://proyectoinf-grupo14.herokuapp.com/static/'
MEDIA_URL = 'https://proyectoinf-grupo14.herokuapp.com/media/'
