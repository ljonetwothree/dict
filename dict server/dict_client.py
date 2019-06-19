"""

dict 客户端

"""
from socket import *
from multiprocessing import Process
import sys,signal
from getpass import getpass

ADDR=('127.0.0.1',8000)

#搭建客户端网络
s = socket()
s.connect(ADDR)
#注册函数
def do_register():
    while True:
        name=input("User:")
        passwd=getpass()
        passwd_=getpass('Again:')

        if (' ' in name) or (' ' in passwd):
            print("用户名或密码不能有空格")
            continue
        if passwd !=passwd_:
            print("两次密码不一样")
            continue
        msg="R %s %s"%(name,passwd)
        s.send(msg.encode())
        data=s.recv(128).decode()
        if data=='OK':
            print("注册成功")
        else:
            print("注册失败")
            return

def do_login(c,data):
    name=input("USER:")
    passwd=getpass()
    msg="L %s %s"%(name,passwd)
    s.send(msg.encode())
    data=s.recv(128).decode()
    if data=="OK":
        print("登录成功")
    else:
        print("登录失败")




def main():

    while True:
        print("""
        ================welcome================
            1.注册      2.登录       3.退出
        ================welcome================      
        """)
        cmd=input("请输入选项：")
        if cmd=='1':
            do_register()
        elif cmd=='2':
            do_login(c,cmd)
        elif cmd=='3':
            s.send(cmd.encode())
        else :
            print("请输入正确选项")

if __name__=="__main__":
    main()

