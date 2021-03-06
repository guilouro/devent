"""
Django settings for devent project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from unipath import Path
from dj_database_url import parse, config as djconfig
import os
import sys

BASE_DIR = Path(__file__).parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7)7xkv(dxuucmdd942nazo7m1%d&wae@d1rka!bm4hew3h%tj7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)

sys.path.append("%s/scrapy_devent" % BASE_DIR.parent)
os.environ['SCRAPY_SETTINGS_MODULE'] = 'scrapy_devent.settings'

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps #
    'kombu.transport.django',
    'djcelery',
    'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'devent.urls'

WSGI_APPLICATION = 'devent.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': djconfig()
}


BROKER_URL = 'django://'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'


from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'update_events': {
        'task': 'core.tasks.crawl',
        'schedule': timedelta(hours=1)
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Template path
TEMPLATE_DIRS = (
    BASE_DIR.parent.child('templates'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATICFILES_DIRS = (
    BASE_DIR.parent.child('assets'),
)

STATIC_ROOT = BASE_DIR.parent.child('static')
STATIC_URL = '/static/'


####################################
# load settings_local.py if exists
####################################
try:
    execfile(BASE_DIR.child('settings_local.py'), globals(), locals())
except IOError:
    pass
