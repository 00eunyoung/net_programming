from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(10)
print('waiting...')
while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        msg=client.recv(1024).decode()
        temp = random.randint(0, 40)
        humid = random.randint(0,100)
        lilum= random.randint(70, 150)

        txt = f"Temp={temp}, Humid={humid}, lilum={lilum}"
        
        if(msg == 'Request'):
            client.send(txt.encode())

        elif (msg == 'quit'):
            s.close()
            break

        else :
            print("Try Again!")