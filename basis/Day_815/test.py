#-*- encoding:utf-8 -*-



# print("Hello World")


# # 推导式

# list1 = [1,5,8,7]

# # 将list1中的每个元素 乘以2 放入 list2
# list2 = [item*2 for item in list1]
# print(list2)

# # 过滤 只添加奇数，并×2
# list2 = [item*2 for item in list1 if item % 2!=0]
# print(list2)
# # 偶数留着，奇数×2
# list2 = [item*2 if item % 2!=0 else item for item in list1 ]
# print(list2)


# def add(a,b):
#     if not isinstance(a,int) or not isinstance(b,int):
#         print("参数类型错误")
#         return
#     print(a+b);

# #add(1,"asd")

# # 默认值
# # 0 系统发送
# # 1 玩家发送
# def sendMail(a,b,type=None):
#    if type:
#         if type == 0:
#             print("系统发送")
#             print(a+b)
#         elif type ==1:
#             print("玩家发送")
#             print(a-b)
#         pass

   
# sendMail(20,10,0)

# # 闭包
# def add(a,b):
#     print(a+b)

# def sub(a,b):
#     print(a-b)

# def log(fuc):
#     def printf(a,b):
#         print("函数开始运行")
#         return fuc(a,b)
#     return printf

# dasda = log(add)
# dasda(2,3)


# # 闭包--支持任意参数
# def add(a,b):
#     print(a+b)

# def sub(a,b):
#     print(a-b)

# def log(fuc):
#     def printf(*args,**kwargs):
#         print("函数开始运行")
#         return fuc(*args,**kwargs)
#     return printf

# dasda = log(add)
# dasda(2,3)


# 装饰器

def log(fuc):
    def printf(*args,**kwargs):
        print("函数开始运行")
        return fuc(*args,**kwargs)
    return printf

@log
def add(a,b):
    print(a+b)
@log
def sub(a,b):
    print(a-b)

add(1,3)

# 装饰器实现类型检测

def typeDetection(func):
    def wrapper(*args,**kwargs):
        rules = func.__annotations__
        for k,v in kwargs.items():
            if k in rules and not isinstance(v,rules[k]):
                print(f'参数 {v} 类型错误，传入类型为: {type(v)}，应传入的类型为: {rules[k]}')
        res = func(*args,**kwargs)
        if 'return' in rules and not isinstance(res,rules['return']):
            print(f"返回值 {res} 类型错误，传出类型为: {type(res)}，应传出的类型为: {rules['return']}")
        return res
    return wrapper


@typeDetection
def Info(name: str, age: int) -> str:
    print(name,age)
    return name

Info(23,23)