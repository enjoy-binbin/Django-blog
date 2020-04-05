import logging
import time

from django.http import HttpResponse

logger = logging.getLogger('django.request')


class LoadTimeMiddleware(object):
    """ 在页面底部显示当前页面的加载时间 """

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        # 会在调用view和之后的中间件之前调用
        start_time = time.time()
        response = self.get_response(request)
        load_time = time.time() - start_time
        # 要使用bytes, 将 <!!LOAD_TIME!!> 替换为加载时间
        try:
            response.content = response.content.replace(b'<!!LOAD_TIME!!>', str.encode(str(load_time)[:5]))
        except:
            # 显示图片等媒体文件时跳过
            pass
        response.load_time = f"{int(load_time * 1000)}ms"
        return response


class HealthCheckMiddleware:
    """ 健康检查, 自动响应health_check开头, 中间件需要加到最顶部 """

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/health_check'):
            return HttpResponse()

        response = self.get_response(request)
        return response


class LoggerMiddleware:
    """ 接口请求日志记录 """

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        self.request = request
        self.__init_ip__()
        self.__init_ua__()

        response = self.get_response(request)
        logger.info(
            f"{request.user} {request.client_ip} {request.method} {request.path} "
            f"{response.status_code} {response.reason_phrase} {response.load_time}"
        )
        return response

    def __init_ip__(self):
        request = self.request
        request.client_ip = \
            request.META.get('HTTP_ALI_CDN_REAL_IP') or \
            request.META.get('HTTP_CDN_SRC_IP') or \
            request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0] or \
            request.META.get('HTTP_X_REAL_IP') or \
            request.META['REMOTE_ADDR']

    def __init_ua__(self):
        request = self.request
        request.ua = request.META.get('HTTP_USER_AGENT', '')
