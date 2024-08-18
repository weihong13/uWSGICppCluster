#-*- encoding:utf-8 -*-

import logging
# 高级用法

# 1.记录器
logger = logging.getLogger('dp.zz.applog')
logger.setLevel(logging.INFO)

# 2.处理器
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.WARNING)

# 没有给 fileHandler设置级别，使用logger的级别
fileHandler = logging.FileHandler(filename='appdemo.log')

# formtter格式
formatter = logging.Formatter("%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s")

# 给处理器设置格式，可以给不同的处理器设置不同的格式
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# 给记录器设置处理器
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

# 定义一个过滤器
flt = logging.Filter("dp.zz")

# 关联过滤器
logger.addFilter(flt)

# 打印日志
logger.debug("这是 debug 日志")
logger.info("这是 info 日志")
logger.warning("这是 warning 日志")
logger.error("这是 error 日志")