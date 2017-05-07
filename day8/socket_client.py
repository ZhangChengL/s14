import socket

client = socket.socket()
client.connect(('localhost',6969))

while True:
    msg = input('>>:').strip()
    if len(msg) == 0 :
        continue
    client.send(msg.encode())
    date = client.recv(1024)
    print('来自服务器:',date.decode())

client.close()