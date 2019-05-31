from celery import Celery

app = Celery('hello', broker='redis://localhost:6379/0')


@app.task
def hello():
    return 'hello celery'

# 这里测试的时候版本需要低一些 celery==3.1.24 和 redis==2.10.6
# 1) 进入当前目录, 命令行运行: celery -A tasks worker --loglevel=info
# 2) 运行tasks_test.py后查看控制台输出: succeeded in 0.01599999999962165s: hello celery
# 新版celery V4看 binblog/celery.py和 binblog/__init_.py
