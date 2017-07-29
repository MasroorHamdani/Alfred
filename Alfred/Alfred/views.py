from django.http.response import HttpResponse
from rest_framework.views import APIView

from manage_keystrokes import add_text
from parser import Parser

class Services(APIView):
	"""

	"""
	def post(self, request):
		print ('check')
		print (request.data)
		PARSER = Parser()
		action = request.data.get('result').get('action')
		if 'print' in action:
			target_code = PARSER.print_statement(request.data)
			add_text(target_code)
		if 'assign' in action:
			target_code = PARSER.assign_statement(request.data)
			add_text(target_code)

		return HttpResponse({True})