import math
import sympy
import random
import socket

host='127.0.0.1'
port=7080


s=socket.socket()
s.connect((host,port))

proot=int((s.recv(1024)).decode())
q=int((s.recv(1024)).decode())
print("q recieved is ",q)
print("primitive root recieved is ",proot)
xc=sympy.randprime(int(q/2),q)
print("xc = ",xc)
yc=(proot**xc)%q
print("yc = ",yc)
ys=int((s.recv(1024)).decode())
print("ys recieved is ",ys)
s.send(str(yc).encode())
kc=(ys**xc)%q
print("My key is ",kc)
s.close()
