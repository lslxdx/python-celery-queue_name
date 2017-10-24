# coding: utf-8
# celery -A worker worker -Q qq

from common import app

app.start()
