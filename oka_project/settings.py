"""
Django settings for oka_project project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from django.contrib.messages import constants as messages
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY')
YOUR_DOMAIN = config('YOUR_DOMAIN')
STRIPE_PUBLISHABLE_KEY = config('STRIPE_PUBLISHABLE_KEY')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY="django-insecure-o6)v^=#%mw105c45tst@am0ay4hd26iy7zuv@=37nhq@$crhgu"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'categories',
    'Product',
    'carousel',
    'contact',
    'offer',
    'footer',
    'faq',
    'cart',
    'users',
    'social',
    'header_footer',
    'nested_admin',
    'orders',
    'reviews',
        
    
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "oka_project.urls"

CART_SESSION_ID = 'cart'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "cart.context_processor.cart_total_amount",
                'header_footer.context_processors.navbar',
                'social.context_processors.socials',
            ],
        },
    },
]

WSGI_APPLICATION = "oka_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Karachi"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = "/static/"

MEDIA_URL = "/media/"

if DEBUG:

    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

else:

    STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mail.nullxcoder.xyz"
EMAIL_PORT = 465  # or 587 if you switch to TLS
EMAIL_USE_TLS = (
    False  # or True if you switch to port 587  # or False if you switch to port 587
)
EMAIL_USE_SSL = (
    True  # or True if you switch to port 587  # or False if you switch to port 587
)
EMAIL_HOST_USER = "info@nullxcoder.xyz"
EMAIL_HOST_PASSWORD = "Pq-?C@6TH27Z"


JAZZMIN_SETTINGS = {
    "custom_css": "css/custom_admin.css",
    "site_title": "Admin Panel",
    "site_header": "Admin Panel",
    "site_icon": "images/fav.png",
    "site_logo": "images/logo.png",
    "welcome_sign": "Welcome to Admin Dashboard",
    'copyright': 'Baby Planet',
    "icons": {
        'user_avatar': 'avatar',
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "faq.Faq": "fas fa-question",
        "navbar.Navbar" : "fas fa-bars",
        "contact.Contact":"fas fa-id-badge",
        "carousel.Carousel":"fas fa-image",
        "categories.Category":"fas fa-list",
        "offer.Offer":"fas fa-tag",
        "Product.Products":"fas fa-plus", 
        "header_footer.Header":"fas fa-bars", 
        "header_footer.footer":"fas fa-bars", 
        "social.Social":"fas fa-icons", 
        "users.Userdata":"fas fa-database",
        "orders.Orders":"fas fa-cart-shopping",
        "orders.OrderItem":"fas fa-italic",
        "reviews.Reviews":"fas fa-registered",
    }
}