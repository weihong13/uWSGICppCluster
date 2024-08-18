#-*- encoding:utf-8 -*-

import logging
import logging.config

# 配置文件方式

logging.config.fileConfig('logging.conf')

rootLogger = logging.getLogger()

rootLogger.debug("这是 root Logger 的 debug 日志")

logger = logging.getLogger('applog')
logger.warning("这是 applog Logger 的 warning 日志")
