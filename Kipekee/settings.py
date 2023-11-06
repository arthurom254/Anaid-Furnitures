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
    'django_daraja',
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

PESAPAL_CONSUMER_SECRET = ''
PESAPAL_CONSUMER_KEY = ''
PESAPAL_TRANSACTION_DEFAULT_REDIRECT_URL = 'clients:pesapal_ipn'

# MPESA_CONFIG = {
#     "CONSUMER_KEY": "", 
#     "CONSUMER_SECRET": "", 
#     "HOST_NAME": "", 
#     "PASS_KEY": "", 
#     "SAFARICOM_API": "https://sandbox.safaricom.co.ke", 
#     "SHORT_CODE": "174379",

# }
###########################################################################
# mpesa

# Possible values: sandbox, production

MPESA_ENVIRONMENT = 'sandbox'

# Credentials for the daraja app

MPESA_CONSUMER_KEY = ''
MPESA_CONSUMER_SECRET = ''

#Shortcode to use for transactions. For sandbox  use the Shortcode 1 provided on test credentials page

MPESA_SHORTCODE = '600111'

# Shortcode to use for Lipa na MPESA Online (MPESA Express) transactions
# This is only used on sandbox, do not set this variable in production
# For sandbox use the Lipa na MPESA Online Shorcode provided on test credentials page

MPESA_EXPRESS_SHORTCODE = '600111'

# Type of shortcode
# Possible values:
# - paybill (For Paybill)
# - till_number (For Buy Goods Till Number)

MPESA_SHORTCODE_TYPE = 'till_number'

# Lipa na MPESA Online passkey
# Sandbox passkey is available on test credentials page
# Production passkey is sent via email once you go live

MPESA_PASSKEY = 'mpesa_passkey'

# Username for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

MPESA_INITIATOR_USERNAME = 'initiator_username'

# Plaintext password for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

MPESA_INITIATOR_SECURITY_CREDENTIAL = ''
