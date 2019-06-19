"""

TCP套接字
"""
from socket import *
from multiprocessing import Process
import signal,sys
from operation import *

db=Database()

# 全局变量
HOST='0.0.0.0'
PORT=8000
ADDR=(HOST,PORT)

def do_register(c,data):
    tem=data.split(' ')
    name=tem[1]
    passwd=tem=tem[2]
    if db.register(name,passwd):
        c.send(b'OK')
    else:
        c.send(b'Fail')



def request(c):
    db.create_cursor() #生成游标
    while True:
        data=c.recv(1024).decode()
        print(c.getpeername(),":",data)
        if data[0]=='R':
            do_register(c,data)


# 搭建网络
def main():
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(3)

    #处理僵尸进程

    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    #循环等待客户端链接

    print("Listen the port 8000")
    while True:
        try:
            c,addr=s.accept()
            print("connect from",addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务端退出")
        except Exception as e:
            print(e)
            continue

        #为客户端创建子进程
        p=Process(target=request,args=(c,))
        p.daemon=True
        p.start()

if __name__=="__main__":
    main()
