#-*- encoding:utf-8 -*-

import logging

# # 修改日志的输出级别为DEBUG，注意要在日志输出前进行设置
# logging.basicConfig(level=logging.DEBUG)

# # 设置日志输出到文件中
# # logging.basicConfig(filename=='demo.log')

# # 设置写入格式 w：每次清空重新写入；a：追加写入
# logging.basicConfig(filemode='w') # 每次清空
# logging.basicConfig(filemode='a') # 追加写入

# # 设置输出格式、添加一些公共信息
logging.basicConfig(
    #          时间         日志等级      文件名       行号       日志信息
    format='%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S', # 规定时间格式
    level=logging.DEBUG          # 设置输出等级
)

# 这样就会输出所有级别的日志
logging.debug("这是 debug 日志")
logging.info("这是 info 日志")
logging.warning("这是 warning 日志")
logging.error("这是 error 日志")
# logging.critical("这是 critical 日志")


# 向日志输出变量
# name = '张三'
# age = 18

# logging.basicConfig(level=logging.DEBUG)
# logging.debug("姓名：%s，年龄：%d", name, age)

# # 以 % 为运算符输出格式化字符串
# logging.debug("姓名：%s，年龄：%d"%( name, age))

# # 以format函数格式化字符串
# logging.debug("姓名：{}，年龄：{}".format(name, age))

# # python3 支持 f-string 格式化字符串
# logging.debug(f"姓名：{name}，年龄：{age}")





