from .base import config

FROM_EMAIL = config("FROM_EMAIL", default="")
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
