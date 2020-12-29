
# settings를 common과 dev(개발용), prod(베포용) 으로 나눠서 진행

import os
from os.path import abspath, dirname

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# settings라는 폴더를 만들어줬으므로 dirname 추가
BASE_DIR = dirname(dirname(dirname(abspath(__file__))))



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qr%a%n8s(-r!p)7o@*di*ix=*0b94eczf#dy#hlm672!hj6t3i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

ADMINS = [
    ('Changwan woo', 'woohobi@gmail.com'),
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Third party
    'bootstrap4',
    'debug_toolbar',
    'django_pydenticon',
    #local
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # django debug toolbar 미들웨어 추가
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'askcompany.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'askcompany', 'templates'),
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

WSGI_APPLICATION = 'askcompany.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_USER_MODEL='accounts.User'
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR, 'askcompany', 'static'),
]
STATIC_ROOT=os.path.join(BASE_DIR, 'static')
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')


# 장고 debug toolbar는 나의 local ip가 들어있어야만 작동
INTERNAL_IPS = [
    '127.0.0.1',
]

#email with sendgrid
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True

WELCOME_EMAIL_SENDER = 'woohobi@gmail.com'