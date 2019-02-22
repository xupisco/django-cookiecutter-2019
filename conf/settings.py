# coding: utf-8
import os
import pytz
import dj_database_url

from decouple import config
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_NAME = config("SITE_NAME", default='Django')
ADMIN_TITLE = config("ADMIN_TITLE", default='Django ADM')
SITE_URL = config("SITE_URL", default='http://localhost:8000')
OG_DESCRIPTION = config("OG_DESCRIPTION", default='')

GTM_ID = config("GTM_ID", default='')
TW_CONSUMER_KEY = config("TW_CONSUMER_KEY", default='')
TW_CONSUMER_SECRET = config("TW_CONSUMER_SECRET", default='')
TW_TOKEN = config("TW_TOKEN", default='')
TW_TOKEN_SECRET = config("TW_TOKEN_SECRET", default='')
FACEBOOK_APP_ID = config("FACEBOOK_APP_ID", default='')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)
THUMBNAIL_DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = ['*', ]

ADMINS = (
    ('@labCorp', 'dev@labcorp.com.br'),
    ('Leandro Voltolino', 'xupisco@gmail.com'),
)

# Application definition
DJANGO_APPS = (
    # 'grappelli',  # Thirdparty APP, but must be called before contrib.admin
    # 'filebrowser',  # Thirdparty APP, but must be called before contrib.admin
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

EXTERNAL_APPS = (
    # Third-party apps goes here
)

PROJECT_APPS = (
    # Your apps
    'apps.core',
)

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + PROJECT_APPS

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'conf.context_processors.settings_context'
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = [os.path.join(BASE_DIR, '_emails')]

WSGI_APPLICATION = 'conf.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(
        url=config(
            'DATABASE_URL', default=os.environ.get('DATABASE_URL'))
    )
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 6, }
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'pt-br'

SHORT_DATE_FORMAT = 'd/m/Y'
SHORT_DATETIME_FORMAT = 'd/m/Y H:i'
DATE_FORMAT = 'd/m/Y'
DATETIME_FORMAT = 'd/m/Y H:i'

DATE_INPUT_FORMATS = (
    '%d/%m/%Y', '%d/%m/%y',  # '25/10/2006', '25/10/06'
    # '%d de %b de %Y', '%d de %b, %Y',   # '25 de Out de 2006', '25 Out, 2006'
    # '%d de %B de %Y', '%d de %B, %Y',   # '25 de Outubro de 2006', '25 de Outubro, 2006'
)

TIME_ZONE = 'America/Sao_Paulo'

TZ_SP = pytz.timezone(TIME_ZONE)
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('pt-br', _('Portuguese (Brazil)')),
    ('en-us', _('English')),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale")
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '_static_collected')
STATIC_ROOT_DEV = os.path.join(BASE_DIR, '_static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '_media')

UPLOAD_DIRECTORY = os.path.join(MEDIA_ROOT, 'uploads')
CHUNKS_DIRECTORY = os.path.join(MEDIA_ROOT, 'chunks')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "_static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

IMAGE_CROPPING_THUMB_SIZE = (500, 500)
FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
FILEBROWSER_DIRECTORY = 'uploaded/'
FILEBROWSER_VERSIONS_BASEDIR = '_versions/'

FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {
    'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Pequeno', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medio', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Grande', 'width': 460, 'height': '', 'opts': ''},
    'card': {'verbose_name': 'Card', 'width': 364, 'height': 205, 'opts': 'crop'},
    'product': {'verbose_name': 'Product', 'width': 560, 'height': 476, 'opts': 'crop'},
    'card_product': {'verbose_name': 'Card Product', 'width': 364, 'height': 310, 'opts': 'crop'},
    'store': {'verbose_name': 'Store', 'width': 364, 'height': 195, 'opts': 'crop'},
    'highlight': {'verbose_name': 'Destaque', 'width': 1920, 'height': 535, 'opts': 'crop'},
    'large': {'verbose_name': 'Gigante', 'width': 680, 'height': '', 'opts': ''},
}
