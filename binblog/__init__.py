# 使得django在启动的时候会加载celery的app
from binblog.celery import app as celery_app

__all__ = ('celery_app',)
