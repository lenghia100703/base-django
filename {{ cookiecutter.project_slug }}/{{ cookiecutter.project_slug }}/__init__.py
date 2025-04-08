from __future__ import absolute_import, unicode_literals

{% if cookiecutter.use_celery == "y" %}
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery_tasks import celery_app

__all__ = ["celery_app"]
{% endif %}