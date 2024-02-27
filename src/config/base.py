import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = bool(int(os.getenv("DEBUG", 1)))

ALLOWED_HOSTS = [
    "0.0.0.0",
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'rest_framework',
    'drf_spectacular',
    'rest_framework_simplejwt',
    'shared.infra.django.config.DjangoConfig',
]

MIGRATION_MODULES = {
    'app': 'shared.infra.django.migrations',
}

ASGI_APPLICATION = 'main.app'

ROOT_URLCONF = 'routers'

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "shared.infra.django.data.static"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "shared.infra.django.data.media"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
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

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = 'redis://pub_sub:6379/0'

RESULT_BACKEND_URL = 'redis://pub_sub:6379/1'
