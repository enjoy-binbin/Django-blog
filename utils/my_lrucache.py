import time
from collections import OrderedDict  # 一个有序的Dict
from functools import wraps


class LRUCacheDict(object):
    # py3: from functools import lru_cache
    def __init__(self, max_size=1024, expiration=60):
        self.max_size = max_size  # 最大容量, 1024个key
        self.expiration = expiration  # 单个key有效期60秒
        self._cache = {}  # LRU缓存 (Least Recently Used 近期最少使用)
        self._access_time = OrderedDict()  # 记录访问时间
        self._expire_time = OrderedDict()  # 记过过期时间

    def __setitem__(self, key, value):
        """ 设置缓存, 调用obj[key] = value执行 """
        now = int(time.time())
        self.__delitem__(key)  # 删除当前key

        self._cache[key] = value
        self._access_time[key] = now
        self._expire_time[key] = now + self.expiration
        self.cleanup()

    def __getitem__(self, key):
        """ 获取缓存中key对应的value, 调用obj['key']执行 """
        now = int(time.time())
        del self._access_time[key]

        self._access_time[key] = now
        self.cleanup()

        return self._cache[key]

    def __delitem__(self, key):
        """ 调用 del obj['key']时候执行 """
        if key in self._cache:
            del self._cache[key]
            del self._access_time[key]
            del self._expire_time[key]

    def __contains__(self, key):
        """ 当前缓存中是否有这个key, 当调用key in obj会执行 """
        self.cleanup()
        return key in self._cache

    def cleanup(self):
        """ 清理过期或者超过大小的缓存 """
        if self.expiration is None:
            return None  # 没设置过期时间就不清理

        now = int(time.time())
        pending_del_keys = []  # 存储待删除的key

        # 记录过期缓存key
        for key, value in self._expire_time.items():
            if value < now:
                pending_del_keys.append(key)

        # 删除过期缓存key, 因为不能在上面迭代过程中删除
        for del_key in pending_del_keys:
            self.__delitem__(del_key)

        # 超过容量, 删除最旧的缓存
        while len(self._cache) > self.max_size:
            for key in self._access_time:
                self.__delitem__(key)
                break

    def size(self):
        """ 返回缓存长度 """
        return len(self._cache)

    def clear(self):
        """ 清理所有缓存 """
        self._cache.clear()
        self._access_time.clear()
        self._expire_time.clear()


def cache_it(max_size=1024, expiration=60):
    cache = LRUCacheDict(max_size, expiration)

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            key = repr(*args, **kwargs)
            try:
                result = cache[key]
            except KeyError:
                result = func(*args, **kwargs)
                cache[key] = result
            return result

        return inner

    return wrapper


@cache_it(max_size=2, expiration=2)
def test(num):
    time.sleep(1)  # 睡一秒, 只有第一次没缓存的时候慢
    res = 'this is number %s' % num
    return res


if __name__ == '__main__':
    cache_dict = LRUCacheDict(max_size=3, expiration=1)
    cache_dict['name'] = 'binbin'
    cache_dict['age'] = '22'
    cache_dict['gender'] = 'male'
    cache_dict['other'] = 'null'

    print('name' in cache_dict)  # False, 超过最大容量, 最旧的记录被删除了
    print('other' in cache_dict)  # True
    time.sleep(1.5)
    print('other' in cache_dict)  # Fasle, 过期记录被删除了

    print(test(2))
    print(test(3))
    print(test(2))  # 这里就直接用到了缓存, 没有sleep(1)
