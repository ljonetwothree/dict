import getpass #隐藏加密
import hashlib #转换加密
pwd=getpass.getpass("PW:")
print(pwd)

# hass=hashlib.md5() #生成对象

hash=hashlib.md5("*#06".encode())
hash.update(pwd.encode())   #算法加密
pwd=hash.hexdigest()  #提取加密后的密码
print(pwd)
