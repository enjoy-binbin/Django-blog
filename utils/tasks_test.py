from .tasks import hello

# delay异步放入中间人那里, 然后celery再去调用
hello.delay()
