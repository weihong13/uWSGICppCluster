#-*- encoding:utf-8 -*-

from wsgiref.simple_server import make_server
import time
# 修改解释器的编码格式
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# 记录请求耗时的中间件
class ResponseTimingMiddleware(object):
    """记录请求耗时"""
    def __init__(self,app):
        self.app = app

    def __call__(self, environ, start_response):
        # 记录开始时间
        start_time = time.time()
        # 调用请求处理函数，得到返回值
        response = self.app(environ, start_response)
        # 记录请求耗时
        response_time = (time.time() - start_time)*1000
        # 设置日志
        timing_text = "\n\n\n记录请求耗时中间件输出\n\n本次请求耗时：{:.10f}ms \n\n\n".format(response_time)
        # 添加到返回值
        response.append(timing_text.encode('utf-8'))
        # 返回请求处理结果
        return response

# 使用url 调用函数
def login(req):
    print(req)
    return 'login'
def home(req):
    print(req)
    return 'home'
def index(req):
    print(req)
    return 'index'
def regist(req):
    print(req)
    return 'regist'

all_url = {
    '/':home,
    '/login':login,
    '/regist':regist,
    '/index':index,
}

# 基本的WSGI协议的实现
# 函数
def simple_app(environ, start_response):
    # 打印请求中的参数，得到请求的url，这样就可以根据信息返回内容； 
    print(environ.get('PATH_INFO')) 

    url = environ.get('PATH_INFO')   # 附加的路径信息，由浏览器发出
    params = environ.get('QUERY_STRING') # 请求URL的 “?” 后面的部分
    if url is None or url not in all_url.keys():
        start_response('404 not found',[('Content-type','text/plain;charset=utf-8')])
        return [b'404 Not Found']
    res = all_url.get(url)
    if res is None:
        start_response('404 not found',[('Content-type','text/plain;charset=utf-8')])
        return [b'404 Not Found']
    
    return_body = []
    return_body.append(res(params))
    # 将环境变量也返回
    for k,v in environ.items():
        return_body.append("{} : {}".format(k,v))

    start_response('200 OK',[('Content-type','text/plain;charset=utf-8')])
    return ["\n".join(return_body).encode('utf-8')]

application = ResponseTimingMiddleware(simple_app)
server = make_server('192.168.0.186',8080,app=application)

#启动服务器  
server.serve_forever();



