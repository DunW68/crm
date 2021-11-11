"""
Django settings for crmest project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&5ltw9+1)39b3bp&j+hzt%264lo3xm#tpij^rlwojja&rn$&#)'
# amoCRM
SECRET_KEY_FOR_CRM = "przhSb5XoGkQovOSzAhulfME5lPyOCbFjxOUuQTVk3UN84PdWkpqmg2TVpLVq1Dy"
INTEGRATION_ID = "2b05c046-7be1-4711-9f6a-6acce6adfd57"
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjU1YmIzOTRhYjkzYjQzOTllNTYxYjIyOGNkNzE0ZGY3ODQ2YzJiNTkyMTUxYjNiNzE3NzBiYzdhMzVjNjU4ZDcxNmQ0MzBiMzlmMmQ2MGU4In0.eyJhdWQiOiIyYjA1YzA0Ni03YmUxLTQ3MTEtOWY2YS02YWNjZTZhZGZkNTciLCJqdGkiOiI1NWJiMzk0YWI5M2I0Mzk5ZTU2MWIyMjhjZDcxNGRmNzg0NmMyYjU5MjE1MWIzYjcxNzcwYmM3YTM1YzY1OGQ3MTZkNDMwYjM5ZjJkNjBlOCIsImlhdCI6MTYzNjU2MzAyNiwibmJmIjoxNjM2NTYzMDI2LCJleHAiOjE2MzY2NDk0MjYsInN1YiI6Ijc2MjI1NTciLCJhY2NvdW50X2lkIjoyOTgxMjc3MSwic2NvcGVzIjpbInB1c2hfbm90aWZpY2F0aW9ucyIsImNybSIsIm5vdGlmaWNhdGlvbnMiXX0.E1SK--TV-7lOIYqr2IBxs-_2nKE4f0bs1J_cd523I9vqn0MPx8nXN9sn9QN2lOYL40b6sIpGAtM_lBEDCZK1MLqmmz3Oy3BGGDT0FwD1zfWR0_lxOkvzrFV-21vmDkedlqy7KsrIISPICtkXVcZEwTskwilCNen-AbMhLFjhkW97r_ZDobzzdkJJgtIOLPFf8FW9SUN-8lM9D679t5vR5yNasHi6WgUwIUaiZkPczd4v8zJ42p2BDbXHkaMQoyjGs7uODLaeIKq-QFb7pDvPw8ZT6lMzypAhX8yONBzWYqE4b_r7AIfI3ddMqwDwEWkoqucWcJAq15yfOPi4ceDixQ'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'amoCRM',
    'rest_framework',
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

ROOT_URLCONF = 'crmest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'crmest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
