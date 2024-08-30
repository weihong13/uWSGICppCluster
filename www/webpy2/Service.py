#-*- encoding:utf-8 -*-

from socket import *

from proto.massage_pb2 import Message

import struct

# 用于和其他服务器进行通信的模块

# 给其他服务器发送消息
def sendSvrd(host, port, info):
    if not info:
        # 打印日志
        # 到这里info应该是没有问题的，如果出现为空的问题，就需要查看日志，排查问题
        return
    # 建立连接
    ADDR = (host, port)
    tcpCliSocket = socket(AF_INET, SOCK_STREAM)
    tcpCliSocket.connect(ADDR)
    # 
    # struct 是由12字节的头部和protobuf类型info组成的
    # > 转为大端存储  头部 8个c，一个i，12个字节
    # C++结构体由libhv进行解析
    buf = struct.pack(">cccccccci", b'H', b'R', b'P', b'C', chr(1), b'\0', b'\0', b'\0', len(info)) + info
    tcpCliSocket.send(buf)
    tcpCliSocket.close()








    