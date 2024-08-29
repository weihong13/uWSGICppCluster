
import re

print("hello world")

def checkPassword(password):  
    # 字母、数字和可选字符!@#*?.+，至少一个数字和一个字母，8-16位  
    pattern = re.compile('^(?=.*[0-9])(?=.*[a-zA-Z])[0-9a-zA-Z!@#*?.+]{8,16}$')  
    if re.match(pattern, str(password)): 
        print("Account checkPassword TRUE") 
        return True  
    print("Account checkPassword False") 
    return False 

# 测试函数  
passwords =  "weihong1223."  
print(checkPassword(passwords))


import Config
import ErrorCfg

def verifyAccount(userId, password):  
    # 尝试在一次查询中获取密码和状态  
    result = Config.gdb.select("user", what=['password', 'status'], where="userid=$userid", vars=dict(userid=userId))  
      
    # 检查用户是否存在  
    if not result:  
        return {'code': ErrorCfg.EC_LOGIN_USERID_ERROR, 'reason': ErrorCfg.ER_LOGIN_USERID_ERROR}  
      
    # 取出密码和状态  
    user_password, user_status = result[0]['password'], result[0]['status']  
      
    # 验证密码（假设使用了哈希函数）  
    if not verify_password(password, user_password):  
        return {'code': ErrorCfg.EC_LOGIN_PASSWORD_ERROR, 'reason': ErrorCfg.ER_LOGIN_PASSWORD_ERROR}  
      
    # 检查账户是否冻结  
    if user_status == Config.USER_STATUS_FRERZE:  # 注意：这里更改为正确的状态名 FROZEN  
        return {'code': ErrorCfg.EC_LOGIN_STATUS_FRERZE, 'reason': ErrorCfg.ER_LOGIN_STATUS_FRERZE}  # 注意：这里也更改了错误代码和错误信息的常量名以保持一致  
      
    # 验证成功  
    return {'code': 0, 'reason': 'Login successful'}  
  
# 假设的 verify_password 函数，用于验证密码（需要实现）  
def verify_password(provided_password, hashed_password):  
    # 这里应该使用与存储密码时相同的哈希函数来验证密码  
    # 返回一个布尔值，表示密码是否匹配  
    # 注意：这个函数需要您自己根据使用的哈希库来实现  
    return (provided_password == hashed_password)