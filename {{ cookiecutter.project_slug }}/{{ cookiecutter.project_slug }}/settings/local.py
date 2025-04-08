"""
    This configuration file overrides some necessary configs
    to easily develop the app.
"""

from .base import *  # noqa
from .base import INSTALLED_APPS, MIDDLEWARE

ALLOWED_HOSTS = ["*"]

{%- if cookiecutter.use_debug_toolbar == "y" %}
# Ref: https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
INSTALLED_APPS += [
    "debug_toolbar",
]
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
{%- endif %}

INTERNAL_IPS = ["127.0.0.1"]

{% if cookiecutter.use_celery == "y" %}CELERY_TASK_ALWAYS_EAGER = True{%- endif %}
