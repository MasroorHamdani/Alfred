# Building microservice
from socket import *
from executioner import Executioner
import re
from threading import Thread

URL_ENCODED_DATA_PATTERN = re.compile('(.*data: )(.*)(\r.*)')

def server(address):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	sock.bind(address)
	sock.listen(5)
	while True:
		client, addr = sock.accept()
		print ('Connected')
		Thread(target = handler, args = (client, )).start()


def handler(client):
	while True:
		req = client.recv(10000)
		print ('coming request', req)
		if not req:
			break
		search_params = URL_ENCODED_DATA_PATTERN.search(req)
		if search_params:
			first, text, other = search_params.groups()
			print ('param', text)
		else:
			text = str(req).replace('\n', '')
		if text == 'run':
			exec_obj = Executioner('Running your command', 'test.py')
			exec_obj.speak()
			exec_obj.printText()
			print(exec_obj.run_my_code())


		print ('comes here {0}'.format(text))
		# result = print('call function here')
		resp = text
		client.send('resp'+ b'\n')
	print ('closed')

server(('', 9999))