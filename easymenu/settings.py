"""
Django settings for easymenu project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition

INSTALLED_APPS = [
    'uzlatekachny.apps.UzlatekachnyConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'easymenu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'easymenu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

SYSTEM_ENV = os.environ.get('SYSTEM_ENV', None)
if SYSTEM_ENV == 'PRODUCTION': # settings for production server
    with open(BASE_DIR / "secret_key.txt") as file:
        SECRET_KEY = file.read().strip()
    with open(BASE_DIR / "secret_github_key.txt") as file:
        SECRET_GITHUB_KEY = file.read().strip()
    ALLOWED_HOSTS = ['.uzlatekachny.com']
    DEBUG = False
    SECURE_HSTS_SECONDS = 1
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_PRELOAD = True
    STATIC_ROOT = "/srv/http/virtual/menu.uzlatekachny.com/static"
    STATICFILES_DIRS = [
        '/srv/http/virtual/menu.uzlatekachny.com/.venv/lib/python3.11/site-packages/django/contrib/admin/static',
    ]
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'OPTIONS': { # type: ignore
                'service': 'easymenu_service',
                'passfile': '.easymenu_pgpass',
            },
        }
    }

elif SYSTEM_ENV == 'GITHUB_WORKFLOW': # settings for github actions
    DEBUG = True
    SECRET_KEY = 'TESTING_KEY' # hardcoded key for testing on github
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'github_actions',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

else: # settings for local development
    with open(BASE_DIR / "secret_key.txt") as file:
        SECRET_KEY = file.read().strip()
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'OPTIONS': { # type: ignore
                'service': 'easymenu_service',
                'passfile': '.easymenu_pgpass',
            },
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'cs'

TIME_ZONE = 'Europe/Prague'

USE_I18N = True

USE_TZ = True

DATE_FORMAT = "j. E, Y"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'