import os
import django_heroku
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Use environment variables for sensitive data
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default')  # Default for development
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['aeiformanage.herokuapp.com', 'localhost', '127.0.0.1']

# Configure the database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Specify PostgreSQL as the database engine
        'NAME': os.getenv('DB_NAME', 'your_local_db_name'),  # Default local database name
        'USER': os.getenv('DB_USER', 'your_local_db_user'),  # Default local database user
        'PASSWORD': os.getenv('DB_PASSWORD', 'your_local_db_password'),  # Default local database password
        'HOST': os.getenv('DB_HOST', 'localhost'),  # Default host for local database
        'PORT': os.getenv('DB_PORT', '5432'),  # Default PostgreSQL port
    }
}

# If DATABASE_URL is set (Heroku), overwrite the local database settings
if os.getenv('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.config(
        default=os.getenv('DATABASE_URL'),  # Use DATABASE_URL from Heroku environment variables
        conn_max_age=600,
        ssl_require=True
    )

# Static file settings for Heroku
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'tasks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For serving static files in production
]

ROOT_URLCONF = 'task_manager.urls'

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

WSGI_APPLICATION = 'task_manager.wsgi.application'

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# Activate Django-Heroku
django_heroku.settings(locals())
