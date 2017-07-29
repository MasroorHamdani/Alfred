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
            target_code = PARSER.print_statement(request.data)
            add_text(target_code)
        elif 'assign' in action:
            target_code = PARSER.assign_statement(request.data)
            add_text(target_code)
        elif 'conditon_if' in action:
            target_code = PARSER.if_statement(request.data)
            add_text(target_code)
        elif 'infinte_loop' in action:
            target_code = PARSER.infinite_loop(action)
            add_text(target_code)
        elif 'loop' in action:
            target_code = PARSER.for_loop_statement(request.data)
            add_text(target_code)
        elif 'cursor' in action:
            PARSER.cursor_action(action)
        elif 'import' in action:
            target_code = PARSER.import_library(request.data)
            add_text(target_code)
        elif 'import_from' in action:
            target_code = PARSER.from_import_library(request.data)
            add_text(target_code)
        elif 'copy' in action:
            PARSER.copy_line(request.data)
        elif 'set_canvas' in action:
            target_code = PARSER.setup_canvas()
        elif 'draw_circle' in action:
            target_code = PARSER.draw_circle(request.data)
        elif 'draw_line' in action:
            target_code = PARSER.draw_line(request.data)
        else:
            Executioner('Error: Invalid Operation').speak()
        return HttpResponse({True})