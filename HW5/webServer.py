from socket import *
s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    filename=req[0].split()[1].strip('/')
    print(filename)

    if filename=='index.html':
        c.send(b'HTTP/1.1\r\n')
        c.send(b'Content-Type: text/html \r\n')
        c.send(b'\r\n')
        f = open(filename, 'r', encoding='utf-8')
        data = f.read()
        c.send(data.encode('euc-kr'))
    
    elif filename=='iot.png':
        c.send(b'HTTP/1.1\r\n')
        c.send(b'Content-Type: image/png \r\n')
        c.send(b'\r\n')
        f = open(filename, 'rb')
        data = f.read()
        c.send(data)

    elif filename=='favicon.ico':
            c.send(b'HTTP/1.1\r\n')
            c.send(b'Content-Type: image/x-icon \r\n')
            c.send(b'\r\n')
            f = open(filename, 'rb')
            data = f.read()
            c.send(data)

    else :
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')

    c.close()