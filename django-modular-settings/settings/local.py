from .base import *


# INSTALLED_APPS += [
#     'debug_toolbar',
# ]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# STATIC files
STATICFILES_DIRS = [
    # BASE_DIR / 'static',
    os.path.join(BASE_DIR, 'static') 
    
]  # staticfiles_dirs --> is the list of folders where Django will search for additional static files aside from the static folder of each app installed.(development)
