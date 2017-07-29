from django.http.response import HttpResponse
from rest_framework.views import APIView
from parser import Parser


class Services(APIView):
    def post(self, request):
        print('check')
        print(request.data)
        PARSER = Parser()
        action = request.data.get('result').get('action')
        if 'print' in action:
            print(PARSER.print_statement(request.data))
        elif 'assign' in action:
            print(PARSER.assign_statement(request.data))
        elif 'conditon_if' in action:
            print(PARSER.if_statement(request.data))
        elif 'loop' in action:
            print(PARSER.for_loop_statement(request.data))
        return HttpResponse({True})
