from .base import *

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'my_portfolio',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306'
    }
}