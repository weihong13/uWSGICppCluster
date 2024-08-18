#-*- encoding:utf-8 -*-

import logging


logger = logging.getLogger("applog")

# 记录器默认等级为 0
# 因此要 设置等级
print(logger.level)

# 将 默认的 处理器等级 归零
logging.basicConfig()
# 设置记录器的等级
logger.setLevel(logging.DEBUG)
# 设置日志
logger.debug("这是 loger 的 debug 日志")


# StreamHandler
sh = logging.StreamHandler(stream=None)

# FileHandler
fh = logging.FileHandler(filename='filename',mode='w',encoding='utf-8',delay=False)


# setFormtter() 给处理器设置格式
sh = logging.StreamHandler()

# formatter格式
formatter = logging.Formatter("%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s")

sh.setFormatter(formatter)

sh.setLevel(logging.DEBUG)

logger = logging.getLogger('dq.zz.applog')
sh = logging.StreamHandler()
# 定义一个过滤器
flt = logging.Filter('dq.zz')
# 关联过滤器到记录器上
logger.addFilter(flt)
# 关联过滤器到处理器上
sh.addFilter(flt)




