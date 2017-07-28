# Building microservice
from socket import *

def server(address):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	sock.bind(address)
	sock.listen(5)
	while True:
		client, addr = sock.accept()
		print ('Connected')
		handler(client)

def handler(client):
	while True:
		req = client.recv(100)
		if not req:
			break
		n = int(req)
		print ('comes here')
		# result = print('call function here')
		resp = str(n).encode('ascii') + b'\n'
		client.send(resp)
	print ('closed')

server(('', 9999))