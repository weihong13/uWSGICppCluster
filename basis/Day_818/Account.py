#-*- encoding:utf-8 -*-

def checkPhoneNum(phoneNum):
    # 1、使用号段列表进行判断
    phoneList = [139,138,137,136,134,135,147,150,151,152,157,158,159,172,178,
                 130,131,132,140,145,146,155,156,166,185,186,175,176,196,
                 133,149,153,177,173,180,181,189,191,193,199,
                 162,165,167,170,171]
    
    # 2、使用正则表达式判断
    if len(phoneNum) == 11 and str(phoneNum).isdigit() and (int(phoneNum[:3]) in phoneList):
        return True
    else:
        return False
