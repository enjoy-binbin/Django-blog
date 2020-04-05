"""
Gunicorn配置
http://docs.gunicorn.org/en/stable/configure.html
"""
import multiprocessing
import os

module_name = os.environ.get('MODULE_ID') or 'binblog'
port = os.environ.get('PORT') or '8000'

bind = "0.0.0.0:%s" % port
workers = multiprocessing.cpu_count() * 2 + 1
pidfile = "/var/run/%s.pid" % module_name

# accesslog= "/data/logs/%s/access.log" % module_name
# errorlog = "/data/logs/%s/error.log" % module_name

daemon = True
max_requests = 30000

capture_output = True

threads = 1

raw_env = ['DJANGO_SETTINGS_MODULE=binblog.settings']
