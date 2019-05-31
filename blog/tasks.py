import time

from celery.utils.log import get_task_logger
from celery import shared_task

logger = get_task_logger(__name__)


@shared_task  # 在django.app中定义的task任务装饰器
def test_add(x, y):
    logger.info('我将睡五秒钟5555555555')
    time.sleep(5)
    logger.info('我睡了五秒钟5555555555')
    print('test_add 执行成功')
    return 'result is: {0} + {1} = {2}'.format(x, y, x + y)
