"""Celery init."""

from __future__ import absolute_import, unicode_literals
import os

from celery import Celery


# set the default Django settings module for the 'celery' program.


print('Celery.py file is running')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatire.settings')
print('os:', os.environ['DJANGO_SETTINGS_MODULE'])

app = Celery('chatire')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()