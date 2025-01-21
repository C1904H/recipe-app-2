import environ

from .base import *

import cloudinary
import cloudinary.uploader
import cloudinary.api

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(str(BASE_DIR / ".env.prod"))

SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG")

#cloudinary credentials
CLOUDINARY_CLOUD_NAME=env.str("CLOUD_NAME")
CLOUDINARY_API_KEY=env.str("API_KEY")
CLOUDINARY_API_SECRET=env.str("API_SECRET")

if not DEBUG:
  DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": CLOUDINARY_CLOUD_NAME,
    "API_KEY": CLOUDINARY_API_KEY,
    "API_SECRET": CLOUDINARY_API_SECRET,
}

ALLOWED_HOSTS = ["recipe-app-2-production.up.railway.app"]
CSRF_TRUSTED_ORIGINS = [
  "https://recipe-app-2-production.up.railway.app"
]


MIDDLEWARE = MIDDLEWARE + ["whitenoise.middleware.WhiteNoiseMiddleware"]

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": env.str("DB_NAME"),
#         "USER": env.str("DB_USER"),
#         "PASSWORD": env.str("DB_PWD"),
#         "HOST": env.str("DB_HOST"),
#         "PORT": env.str("DB_PORT"),
#     }
# }

# If you want to use sqlite3 instead, then uncomment this and comment the above.

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

STATIC_ROOT = str(BASE_DIR / "staticfiles")
STATICFILES_DIRS = (str(BASE_DIR / "static"),)

import dj_database_url

DATABASE_URL = env.str("DATABASE_URL")

DATABASES = {
  "default": dj_database_url.config(default=DATABASE_URL),
}