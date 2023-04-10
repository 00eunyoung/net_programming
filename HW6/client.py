from socket import *
import time

device1 = socket(AF_INET, SOCK_STREAM)
device2 = socket(AF_INET, SOCK_STREAM)

device1.connect(('localhost', 3333))
device2.connect(('localhost', 4444))

while True:
    msg = input('Number to send (1 or 2):')
    f = open('data.txt', 'a')
    
    if(msg == '1'):
        device1.send(b"Request")
        result= device1.recv(1024).decode()
        f.write(f'{time.ctime(time.time())}: Device1: {result}\n')
        print(result)

    elif(msg == '2'):
        device2.send(b"Request")
        result= device2.recv(1024).decode()
        f.write(f'{time.ctime(time.time())}: Device2: {result}\n')
        print(result)

    elif(msg == 'quit'):
        device1.send(msg.encode())
        device2.send(msg.encode())
        break
        
    else :
        print('Try Again!')

device1.close()
device2.close()
f.close()