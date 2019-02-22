import time


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
        response.content = response.content.replace(b'<!!LOAD_TIME!!>', str.encode(str(load_time)[:5]))
        return response
