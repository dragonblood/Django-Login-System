import os
import warnings
# from django.utils.translation import ugettext_lazy as _
from os.path import dirname

warnings.simplefilter('error', DeprecationWarning)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE_DIR, 'content')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3%)4ya)u3q4!b6gtu*gh(wxzz@0=vg^k=6b!$3jd5t)c4^*rbg'


DEBUG = True
ALLOWED_HOSTS = ['vipuldjangologin.herokuapp.com', 'login.vipulpetkar.me','login.vipulpetkar.ml', 'login.vipulpetkar.works', '127.0.0.1']

SITE_ID = 1
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Vendor apps
    'bootstrap4', 

    # Application apps
    'main',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(CONTENT_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'main.wsgi.application'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FILE_PATH = os.path.join(CONTENT_DIR, 'tmp/emails')
EMAIL_HOST = 'smtp.gmail.com'
DEFAULT_FROM_EMAIL = 'test@example.com'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd1674t9dctgooi',
        'USER': 'emgjclivpoebpq',
        'PASSWORD': '5ed42e2d9566c53de03badf9a84e9974f40b269b6f383b99c14e4ee01450ac7a',
        'HOST': 'ec2-34-235-108-68.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ENABLE_USER_ACTIVATION = False
DISABLE_USERNAME = False
LOGIN_VIA_EMAIL = True
LOGIN_VIA_EMAIL_OR_USERNAME = True
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'accounts:log_in'
USE_REMEMBER_ME = True

RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = False
ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE = False

SIGN_UP_FIELDS = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
if DISABLE_USERNAME:
    SIGN_UP_FIELDS = ['first_name', 'last_name', 'email', 'password1', 'password2']

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
#LANGUAGES = [
#    ('en', _('English')),
#    ('ru', _('Russian')),
#    ('zh-Hans', _('Simplified Chinese')),
#]

TIME_ZONE = 'UTC'
USE_TZ = True

STATIC_ROOT = os.path.join(CONTENT_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(CONTENT_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(CONTENT_DIR, 'assets'),
    
]

LOCALE_PATHS = [
    os.path.join(CONTENT_DIR, 'locale')
]

