import socket

HOST = '192.168.0.110'    # "" : 문자열   '': 
PORT = 2000

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

c.connect((HOST,PORT))

data = c.recv(65536)
print(repr(data.decode()))     # Server로부터 온 메시지

while True:

	data = input().encode()
	if data == b'exit':
		c.close()
		break

	c.sendall(data)
	data = c.recv(65536)
	print('Received', repr(data.decode()))   #repr : 숫자를 문자열로 바꾸는것
