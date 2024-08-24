#-*- encoding:utf-8 -*-

from web.session import Store
import json

class RedisStore(Store):
    def __init__(self, grds, timeout):
        self.redis = grds
        self.timeout = timeout
    
    def encode(self, dession_dict):
        return json.dumps(dession_dict)
    
    def decode(self, dession_data):
        return json.loads(dession_data)
    # 判断session是否存在
    def __contains__(self, key):
        return self.redis.exists(key)

    # 获取session
    def __getitem__(self, key):
        value = self.redis.get(key)
        if value:
            self.redis.expire(key, self.timeout)
            return self.decode(value)
        else:
            raise KeyError(key)
    # 设置session
    def __setitem__(self, key, value):
        self.redis.setex(key, self.timeout, self.encode(value))
    # 删除session
    def __delitem__(self, key):
        self.redis.delete(key)
    # 清理
    def cleanup(self, timeout):
        # Redis自身支持过期时间，这里无需实现
        pass