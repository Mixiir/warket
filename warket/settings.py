import os
import sys
from pathlib import Path

from decouple import config

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '*']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "warket_viewer",
    "storages",
    "users",
    "crispy_forms",
    "vertical_multi_columns",
    "auctions",
    "cart",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "warket.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "warket_viewer/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "cart.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "warket.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_IP"),
        "PORT": "3306",
        "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"},
    },
    # "default": {
    #     "ENGINE": "django.db.backends.mysql",
    #     "NAME": config("DB_BLANK"),
    #     "USER": config("DB_USER"),
    #     "PASSWORD": config("DB_PASSWORD"),
    #     "HOST": config("DB_IP"),
    #     "PORT": "3306",
    #     "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"},
    # },
    "local_database": {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database',
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django."
                "contrib."
                "auth."
                "password_validation."
                "UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django."
                "contrib."
                "auth."
                "password_validation."
                "MinimumLengthValidator",
    },
    {
        "NAME": "django."
                "contrib."
                "auth."
                "password_validation."
                "CommonPasswordValidator",
    },
    {
        "NAME": "django."
                "contrib."
                "auth."
                "password_validation."
                "NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Etc/GMT-2"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "warket_viewer/static"), ]
MEDIA_ROOT = [os.path.join(BASE_DIR, "media")]
MEDIA_URL = config("IMAGE_SERVER")


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
LOGIN_URL = "login"

# Custom settings

DEFAULT_FILE_STORAGE = "storages.backends.ftp.FTPStorage"
FTP_STORAGE_LOCATION = config("FTP_STORAGE_LOCATION")

CRISPY_TEMPLATE_PACK = "bootstrap4"
CART_SESSION_ID = "cart"
AUTH_USER_MODEL = 'users.MyUser'

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_d109366sd476154'
    }


# Email conf:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.zone.eu'
IMAP_HOST = 'imap.zone.eu'
EMAIL_PORT = 587
EMAIL_HOST_USER = config("EMAIL_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
