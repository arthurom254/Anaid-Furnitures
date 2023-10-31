import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure--lvh&253$96s5to$x))5$^v9md2u+dwp@9ojhh0=_#&7xc1v!x'

DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID=1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'administrator',
    'social_django',
    'clients',
    'paypal.standard.ipn',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    # 'mpesa',
    # 'django_pesapal',
    # 'pesapal',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'Kipekee.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'clients.basic_info.information',
            ],
        },
    },
]

WSGI_APPLICATION = 'Kipekee.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
# 	'ENGINE':'django.db.backends.postgresql',
# 	'NAME':'postgres',
# 	'USER':'postgres',
# 	'PASSWORD':'P_',
# 	'HOST':'localhost',
# 	'PORT':'5432',
#     }
# }


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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_ROOT=os.path.join(BASE_DIR, 'shopstatic')
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), ) 
MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PAYPAL_RECEIVER_EMAIL = 'sb-xpdk4727496802@business.example.com'
PAYPAL_TEST=True


AUTHENTICATION_BACKENDS = [
'social_core.backends.facebook.FacebookOAuth2',
'django.contrib.auth.backends.ModelBackend',
]
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout'
LOGOUT_REDIRECT_URL = '/'
SOCIAL_AUTH_FACEBOOK_KEY = "2629405060551028"
SOCIAL_AUTH_FACEBOOK_SECRET = "ac80fd2a9ac12bf0f6909700279f0487"
SOCIAL_AUTH_FACEBOOK_SCOPE = [
'email',
]

EMAIL_BACKEND='django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH=BASE_DIR / 'sent_emails'


# EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS=True
# EMAIL_HOST='smtp.gmail.com'
# EMAIL_HOST_USER='kengenstudents@gmail.com'
# EMAIL_HOST_PASSWORD='11111111111'
# EMAIL_PORT=587

PESAPAL_CONSUMER_SECRET = 'osGQ364R49cXKeOYSpaOnT++rHs='
PESAPAL_CONSUMER_KEY = 'qkio1BGGYAXTu2JOfm7XSXNruoZsrqEW'
PESAPAL_TRANSACTION_DEFAULT_REDIRECT_URL = 'clients:pesapal_ipn'

# MPESA_CONFIG = {
#     "CONSUMER_KEY": "", 
#     "CONSUMER_SECRET": "", 
#     "HOST_NAME": "", 
#     "PASS_KEY": "", 
#     "SAFARICOM_API": "https://sandbox.safaricom.co.ke", 
#     "SHORT_CODE": "174379",

# }