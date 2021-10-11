import os
import json
import sys
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured
from kaffeefinder.apps.core.versioning import get_git_changeset_timestamp

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# EXTERNAL_BASE = os.path.join(BASE_DIR "externals")
EXTERNAL_APPS_PATH = BASE_DIR / "apps"
kaffeefinder_MAIN_PATH = BASE_DIR / "kaffeefinder"

# EXTERNAL_LIBS_PATH = os.path.join(EXTERNAL_BASE, "libs")
# EXTERNAL_APPS_PATH = os.path.join(EXTERNAL_BASE, "apps")

#
# with open(os.path.join(os.path.dirname(__file__), 'secrets.json'), 'r') as f:
#     secrets = json.loads(f.read())
#
#
# def get_secret(setting):
#     """Get the secret variable or return explicit exception."""
#     try:
#         return secrets[setting]
#     except KeyError:
#         error_msg = f'Set the {setting} secret variable'
#         raise ImproperlyConfigured(error_msg)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "irmfaosd9uiv[qe4irt'pokdf0qierqerg[oqjefglbkjadf"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
    "87.107.68.50",
]


# Application definition

INSTALLED_APPS = [
    # contributed
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third-party
    'crispy_forms',
    # local
    # ...
    "kaffeefinder.apps.cafes.apps.CafesConfig",
    "kaffeefinder.apps.comments.apps.CommentsConfig",
    "kaffeefinder.apps.accounts.apps.AccountsConfig",
    "kaffeefinder.apps.pages.apps.PagesConfig",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'kaffeefinder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'kaffeefinder', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kaffeefinder.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR / 'locale'
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# auth
LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/cafes/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'kaffeefinder', 'site_static'),
    BASE_DIR / 'kaffeefinder' / 'site_static'
]

timestamp = get_git_changeset_timestamp(BASE_DIR)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
