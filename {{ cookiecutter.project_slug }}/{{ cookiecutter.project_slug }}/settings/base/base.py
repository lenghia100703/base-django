"""
Django settings for {{ cookiecutter.project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os

from decouple import config


ENVIRONMENT = os.environ.get("ENVIRONMENT", "local")

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
)

# common settings
DEBUG = config("DEBUG", default=False, cast=bool)
SECRET_KEY = config("SECRET_KEY")
LOG_LEVEL = config("LOG_LEVEL", default="ERROR")
WSGI_APPLICATION = "wsgi.application"
ROOT_URLCONF = "urls"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

BACKEND_URL = config("BACKEND_URL", default="")
APP_URLS = config("APP_URLS", default=[], cast=list)
