# STATIC files
STATICFILES_DIRS = [
    # BASE_DIR / 'static',
    os.path.join(BASE_DIR, 'static')
]
STATIC_URL = 'static/'
# =======================================================================================================================

# MEDIA files 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# =======================================================================================================================

# AUTH
## change your default User Model via this code :
AUTH_USER_MODEL = 'app_name.model_name'

# =======================================================================================================================

## where user goes after he/she Logs In to your website :
LOGIN_REDIRECT_URL = '/accounts/profile/'
# =======================================================================================================================

## when you use login_required() decorator on a  view, an Unauthenticated user will go to LOGIN page . set your login page url :
LOGIN_URL = '/login/'
# =======================================================================================================================

## redirect user after a user Loges Out :
LOGOUT_REDIRECT_URL = '/home/'
# =======================================================================================================================

## Enabling password validation
# * UserAttributeSimilarityValidator : which checks the similarity between the password and a set of attributes of the user.
# * MinimumLengthValidator   : which checks whether the password meets a minimum length. This validator is configured with a custom option,
#   -it now requires the minimum length to be nine characters, instead of the default eight.
# * CommonPasswordValidator  : which checks whether the password occurs in a list of common passwords.
#   -By default, it compares to an included list of 20,000 common passwords.
# * NumericPasswordValidator : which checks whether the password isn’t entirely numeric.

AUTH_PASSWORD_VALIDATORS =
[
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

