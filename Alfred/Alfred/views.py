from django.http.response import HttpResponse
from rest_framework.views import APIView

from executioner import Executioner
from manage_keystrokes import add_text
from parser import Parser

class Services(APIView):
    """

    """
    def post(self, request):
        """

        :param request:
        :return:
        """
        PARSER = Parser()
        action = request.data.get('result').get('action')
        if action == 'run':
            e = Executioner(file_name="target.py")
            print(e.run_my_code())
        target_code = ""
        if 'input.unknown' in action:
            Executioner('Please repeat your command').speak()
        if 'print' in action:
            target_code  = PARSER.print_statement(request.data)
        elif 'assign' in action:
            target_code = PARSER.assign_statement(request.data)
        elif 'conditon_if' in action:
            target_code = PARSER.if_statement(request.data)
        elif 'loop' in action:
            target_code = PARSER.for_loop_statement(request.data)
        elif 'cursor' in action:
            print(PARSER.cursor_action(action))
        else:
            Executioner('Error: Invalid Operation').speak()
        print(target_code)
        add_text(target_code)
        return HttpResponse({True})