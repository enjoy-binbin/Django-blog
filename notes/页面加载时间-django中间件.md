用django中间件，实现一个功能，获取一个页面的加载时间，并显示在页面底部

2019年2月17日 11:46:49

### 编写中间件，在blog目录下新建一个 middleware.py

```python
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

```

### settIngs里设置中间件

```
MIDDLEWARE = [
    ....
    'blog.middleware.LoadTimeMiddleware'  # 页面加载时间
]
```

### 模板文件里调用

```html
<div style="text-align: center">
    本页面加载耗时:<!!LOAD_TIME!!>s
</div>
```

