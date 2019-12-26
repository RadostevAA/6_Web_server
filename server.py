import socket
import os

sock = socket.socket()

try:
    sock.bind(('', 80))
    print("Using port 80")
except OSError:
    sock.bind(('', 8080))
    print("Using port 8080")
while True:
    sock.listen(5)

    conn, addr = sock.accept()
    print("Connected", addr)
    
    data = conn.recv(8192)
    msg = data.decode()
    
    
    msg1 = msg.split(' ')[1]
    print(msg1[1:])
    print(os.path.abspath('index.html'))
    
    if msg1 == '/':
        file = open('index.html', 'r')
        content = file.read()
        conn.send(content.encode())
        file.close()
    elif os.path.exists(os.path.abspath(str(msg1[1:]))) == True:
        file = open(str(msg1[1:]), 'r')
        content = file.read()
        conn.send(content.encode())
        file.close()
    else:
        resp1 = """HTTP/1.1 404 NOT FOUND
        Server: SelfMadeServer v0.0.1
        Content-type: text/html
        Connection: close
        """
        conn.send(resp1.encode())

conn.close()