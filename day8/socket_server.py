import socket
server = socket.socket()
server.bind(('localhost',6969)) #绑定要监听的端口
server.listen()  #监听端口
while True:
    print("等待客户端的连接...")
    conn,addr = server.accept() #等电话打进来
    print("新连接:",addr )
    #conn就是客户端连过来而在服务器端为其生成的一个连接实例
    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端已断开连接....")
            break
        print('recv',data.decode())
        conn.send('发送成功！'.encode())
#conn.send(data.upper())

server.close()

