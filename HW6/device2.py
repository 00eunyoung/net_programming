from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 4444))
s.listen(10)
print('waiting...')
while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        msg=client.recv(1024).decode()
        heartbeat = random.randint(40, 140)
        step = random.randint(2000,6000)
        cal= random.randint(1000, 4000)

        txt = f"Heartbeat={heartbeat}, Steps={step}, Cal={cal}"
        
        if(msg == 'Request'):
            client.send(txt.encode())

        elif (msg == 'quit'):
            s.close()
            break
        else :
            print("Try Again!")