import math
import sympy
import random
import socket

host='127.0.0.1'
port=7080

q=sympy.randprime(100,300)

alpha=[]                    #list to contain primitive roots
n={i for i in range(1,q)}   #set to contain 1 to q-1 numbers
tset=set()
i=1
for i in range(1,q):
    tset.clear()
    for j in range(1,q):
        tset.add((i**j)%q)  #Testing set

    if(len(n-tset)==0):     #If both sets are equal
        alpha.append(i)

proot=random.choice(alpha)  #selecting one random primitive root from list
print("q is ",q)
print("primitive root is ",proot)
s=socket.socket()
s.bind((host,port))
s.listen(1)
c,addr=s.accept()


c.send(str(proot).encode())
c.send(str(q).encode())

xs=sympy.randprime(int(q/2),q)
print("xs = ",xs)
ys=(proot**xs)%q
print("ys = ",ys)
c.send(str(ys).encode())
yc=int((c.recv(1024)).decode())
print("yc recieved is ",yc)
ks=(yc**xs)%q
print("My key is ",ks)
c.close()
