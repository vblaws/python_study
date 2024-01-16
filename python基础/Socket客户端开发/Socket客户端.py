import socket

socket_client = socket.socket()

socket_client.connect(("localhost", 8888))

while True:
	msg = input("请输入你要发送给服务端的内容:")
	if msg == "break":
		print("客户端退出")
		break
	socket_client.send(msg.encode("UTF-8"))
	# 服务端返回的消息
	recv_data = socket_client.recv(1024)
	print(f"服务端返回的消息为:{recv_data.decode("UTF-8")}")
socket_client.close()
