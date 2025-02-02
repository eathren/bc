from pathlib import Path
import environ
import django_heroku
import dj_database_url

# Initialize environment variables
env = environ.Env(
    DEBUG=(bool, False)
)

# Read .env file
environ.Env.read_env()
print(f"DJANGO_ENV: {env('DJANGO_ENV')}")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='django-insecure-&#xn#*+0!69f5&ma)ac3faey(b64azkx5z=eqbiujr7a*lojl9')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['flashlink.io', 'www.flashlink.io'])

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sites",
    "whitenoise.runserver_nostatic",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # Django apps
    "accounts",
    "core",
    "dashboard",
    
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "bc.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "bc.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if env('DJANGO_ENV') == 'production':
    DATABASES = {
        "default": dj_database_url.config(
            default=env('DATABASE_URL')
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'core/static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = 'accounts.CustomUser'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 1

# CSRF settings
CSRF_TRUSTED_ORIGINS = ['https://flashlink.io', 'https://www.flashlink.io']

# Activate Django-Heroku.
django_heroku.settings(locals())