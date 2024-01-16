# import socket
# # 创建socket对象
# socket_server = socket.socket()
# # 绑定IP和端口
# socket_server.bind(("localhost", 1888))
# # 监听端口
# socket_server.listen(5)
# # 接收客户端链接，获得链接对象
# conn, address = socket_server.accept()
#
# print(f'接收到了客户端的链接，客户端的信息是{address}')
# while True:
# 	data = conn.recv(1024).decode("UTF-8")
# 	if data == "break":
# 		print("退出链接")
# 		break
# 	print(f"客户端发来的消息为{data}")
# 	msg = input("请输入你要返回给客户端的消息")
# 	conn.send(f"这是返回给客户端的消息{msg}".encode("UTF-8"))
# conn.close()
# socket_server.close()

import socket

socket_server = socket.socket()

socket_server.bind(("localhost", 8888))

socket_server.listen(5)
# 接收客户端链接额
conn, address = socket_server.accept()
print(f"客户端IP{address[0]},端口号为{address[1]}")
while True:
	data = conn.recv(1024).decode("UTF-8")
	print(f"客户端发来的消息:{data}")
	
	msg = input("请输入你要发送给客户端的内容:")
	if msg == 'break':
		print("服务端退出连接")
		break
	conn.send(msg.encode("UTF-8"))
conn.close()
socket_server.close()
