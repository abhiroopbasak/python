import socket
import threading
import os

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip = "13.126.199.236"
port = 3000
s.bind( (ip,port) )


def t():
    while True:
        msg=input()
        s.sendto(msg.encode(),("13.126.199.236",3000))
        x=s.recvfrom(1024)
        data=x[0]
        print("linux : "+data.decode())


t1 = threading.Thread(target = t)
t2 = threading.Thread(target = t)
t3 = threading.Thread(target = t)
t1.start()
t2.start()
t3.start()