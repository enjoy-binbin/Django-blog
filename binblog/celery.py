import os

from celery import Celery

# 把默认的django settings模块配置给celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'binblog.settings')
# redis_url = 'redis://127.0.0.1:6379/0'  # 这里不用localhost, 因为有时候celery会连不上redis
# app = Celery('binblog', broker=redis_url, backend=redis_url)  # 配置信息写入settings里

app = Celery('binblog')

# 这里使用字符串以使celery的worker不用为子进程序列化配置对象。
# 命名空间 namespace='CELERY' 规定在settings里关于celery的配置信息都以 'CELERY_' 为前缀
app.config_from_object('django.conf:settings', namespace='CELERY')

# 可以自动发现和注册各个app下的tasks.py里的任务
# win下需要安装eventlet, 不然注册不到tasks. pip install eventlet
app.autodiscover_tasks()

# 启动方式: 进入项目根目录 参数-f xxx.log可以指定celery输出日志到文件
# celery -A binblog worker -l info -P eventlet
# python manage.py runserver
# 访问视图(视图里异步调用tasks.py里的任务 xx.delay()), 之后观察控制台输出
# 任务会放到消息中间人那里, celery启动后会去broker里执行任务
