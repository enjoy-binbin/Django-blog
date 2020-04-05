#!/bin/sh
gunicorn -c gunicorn.conf.py binblog.wsgi
