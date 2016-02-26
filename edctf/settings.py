"""
Django settings for edctf project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# import local secrets
try:
  import edctf_secret
except ImportError as err:
  err.message += ".  edctf_secret.py needs to be generated!"
  raise

# import ctf database information
try:
  from edctf_databases import databases as CTF_DATABASES
except ImportError as err:
  with open(os.path.join(BASE_DIR, 'edctf/edctf_databases.py'), 'wb') as f:
    f.write('databases = {}\n')
  from edctf_databases import databases as CTF_DATABASES


SECRET_KEY = edctf_secret.SECRET_KEY.decode('base64')
DEBUG = True

if DEBUG:
  ALLOWED_HOSTS = []
else:
  ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = (
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'edctf.api',
  'rest_framework',
)

MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'edctf.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'edctf/static/ember/')],
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

WSGI_APPLICATION = 'edctf.wsgi.application'

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': edctf_secret.DB_NAME,
    'USER': edctf_secret.DB_USER,
    'PASSWORD': edctf_secret.DB_PASSWORD,
    'HOST': edctf_secret.DB_HOST,
    'PORT': edctf_secret.DB_PORT,
  },
}
DATABASES.update(CTF_DATABASES)


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = ('/opt/edctf/edctf/static/',)

if DEBUG:
  REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
      'edctf.api.permissions.EdctfPermission',
    ),
    'DEFAULT_PARSER_CLASSES': (
      'rest_framework.parsers.JSONParser',
    ),
  }
else:
  REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
      'edctf.api.permissions.EdctfPermission',
    ),
    'DEFAULT_RENDERER_CLASSES': (
      'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
      'rest_framework.parsers.JSONParser',
    ),
  }
