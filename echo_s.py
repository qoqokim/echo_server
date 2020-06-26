import socket

HOST = '192.168.0.110'    # "" : 문자열   '': 
PORT = 2000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("binding..")
s.bind((HOST,PORT))
print("success to bind")

s.listen()
print("Listen...")

c, addr = s.accept()
print("Connected by", addr)
   
s_M = b'server accept'   # 서버와 연결됐을때 클라이언트에게 전해줄 메시지
c.sendall(s_M)            # 서버에게 메시지 전달

while True:
	data = c.recv(65536)
	if not data:
		break
	print('Received from',addr, data.decode())
	c.sendall(data)

c.close()
s.close() 
