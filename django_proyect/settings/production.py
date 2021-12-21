from .base import *
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_root')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_URL = 'proyectoinf-grupo14.herokuapp.com/static/'
MEDIA_URL = 'proyectoinf-grupo14.herokuapp.com/media/'
