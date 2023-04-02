from socket import *

table = {'+','-','*','/'}

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        data = data.decode()
        for i in range(0, len(data)):
            if data[i] in table:
                op = data[i]

        if 'q' in data:
            break
        
        num1, num2 = data.split(op) 
        num1 = num1.strip()
        num2 = num2.strip()
        
        if op == '+':
            result = int(num1)+int(num2)
        elif op == '-':
            result = int(num1)-int(num2)
        elif op == '*':
            result = int(num1)*int(num2)
        elif op == '/':
            result = round((float(num1)/float(num2)),1)
        client.send(str(result).encode())
    client.close()
    