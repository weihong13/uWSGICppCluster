
import re
def CheckPassword(password):  
    # 字母、数字和可选字符!@#*?.+，至少一个数字和一个字母，8-16位  
    pattern = re.compile('^(?=.*[0-9])(?=.*[a-zA-Z])[0-9a-zA-Z!@#*?.+]{8,16}$')  
    if re.match(pattern, password):  
        print("CheckPassword return True")  
        return True  
    print("CheckPassword return False")  
    return False 

# 测试函数  
passwords = ["Password123", "123!@#*", "abc+?*.", "Password12345678901234567", "Pass@word123", "A1b!C#2d?.+e*F3"]  
for pwd in passwords:  
    ret = CheckPassword(pwd)
    print(ret)