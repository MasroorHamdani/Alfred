# Building microservice
from socket import *
from executioner import Executioner
import re

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
		text = str(req).replace('\n', '')
		if text == 'run':
			exec_obj = Executioner('Running your command')
			exec_obj.speak()
			exec_obj.printText()

		print ('comes here {0}'.format(text))
		# result = print('call function here')
		resp = str(text).encode('ascii') + b'\n'
		client.send(resp)
	print ('closed')

server(('', 9999))