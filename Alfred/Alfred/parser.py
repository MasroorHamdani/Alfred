from manage_keystrokes import manage_keystrokes, copy, add_text

class Parser:
    """
    Parser class will be responsible to
    convert text into python commands
    Operation being handeled are as below:
    Print
    Assignment
    Conditions
    Loop
    Run
    """
    def __init__(self):
        """
        Constructor will initiate the loop conent variable
        which will be used in multiple loop statements
        """
        self.for_loop_content = ''

    def print_statement(self, print_json):
        """
        Formats supported:
        print string <string content>
        print variable <variable>
        :param text:
        :return:
        """
        action = print_json.get('result').get('action')
        parameter = print_json.get('result').get('parameters')
        if action in 'print_string':
            strp = 'print("' + parameter.pop('subject') + '")'
        elif action in 'print_variable':
            strp = 'print(' + parameter.pop('variable') + ')'
        else:
            strp = "Error: Invalid Operation"
        return strp

    def assign_statement(self, assignment_json):
        """
        Formats supported:
        assign <number> to <variable>
        assign <variable> to <variable>
        :param text:
        :return:
        """
        action = assignment_json.get('result').get('action')
        parameter = assignment_json.get('result').get('parameters')
        if action in 'assign_var_to_var':
            strp = parameter.pop('source_var') + ' = ' + parameter.pop('target_var')
        elif action in 'assign_val_to_var':
            strp = parameter.pop('variable') + ' = ' + parameter.pop('value')
        else:
            strp = "Error: Invalid Operation"
        return strp

    def if_statement(self, if_json):
        """
        Format supported:
        If condition </<=/>/>=/==/!= then assign value to variable passed.
        :param if_json:
        :return:
        """
        parameter = if_json.get('result').get('parameters')
        action = parameter.pop('action')
        action_list = action.split(' ')
        condition = parameter.pop('condition')
        cond_list = condition.split(' ')
        if 'less than' in condition and 'equal to' in condition:
            str = 'if ' + cond_list[0] + '<=' + cond_list[len(cond_list)-1] + ':' + 'nl'
            manage_keystrokes('enter')
        elif 'greater than' in condition and 'equal to' in condition:
            str = 'if ' + cond_list[0] + '>=' + cond_list[len(cond_list)-1] + ':' + 'nl'
        elif 'less than' in condition:
            str = 'if ' + cond_list[0] + '<' + cond_list[len(cond_list)-1] + ':' + 'nl'
            manage_keystrokes('enter')
        elif 'greater than' in condition:
            str = 'if ' + cond_list[0] + '>' + cond_list[len(cond_list) - 1] + ':' + 'nl'
            manage_keystrokes('enter')
        elif 'not equal to' in condition:
            str = 'if ' + cond_list[0] + '!=' + cond_list[len(cond_list) - 1] + ':' + 'nl'
            manage_keystrokes('enter')
        elif 'equal to' in condition:
            str = 'if ' + cond_list[0] + '==' + cond_list[len(cond_list) - 1] + ':' + 'nl'
            manage_keystrokes('enter')
        else:
            str = "Error: Invalid Operation"

        if 'Error' not in str:
            str += 'tab' + action_list[0] + ' = ' + action_list[len(action_list) - 1]
        return str

    def for_loop_statement(self, for_loop_json):
        """
        Format Supported:
        For loops start condition
        Intermediate steps inside loop
        For end condition
        :param for_loop_json:
        :return:
        """
        action = for_loop_json.get('result').get('action')
        parameter = for_loop_json.get('result').get('parameters')
        if action in 'loop':
            self.for_loop_content = 'for number in range(1,' + parameter.pop('range') + '):' + 'nl' + 'tab'
        if 'print' in action:
            manage_keystrokes('tab')
            self.for_loop_content += self.print_statement(for_loop_json)
            manage_keystrokes('enter')
        if 'assign' in action:
            manage_keystrokes('tab')
            self.for_loop_content += self.assign_statement(for_loop_json)
            manage_keystrokes('enter')
        if action in 'end_loop':
            manage_keystrokes('enter')
            manage_keystrokes('backspace')
            self.for_loop_content += '\n'
        return self.for_loop_content

    def cursor_action(self, action):
        """
        Format supported:
        Back space from keyboard
        Up Arrow key from Keyboard
        Down Arrow key from Keyboard
        Right Arrow key from Keyboard
        Left Arrow key from Keyboard
        Enter key from Keyboard
        Space key from Keyboard
        Tab key from Keyboard
        :param action:
        :return:
        """
        if 'cursor_backspace' in action:
            manage_keystrokes('backspace')
        if 'cursor_up' in action:
            manage_keystrokes('up')
        if 'cursor_down' in action:
            manage_keystrokes('down')
        if 'cursor_left' in action:
            manage_keystrokes('left')
        if 'cursor_right' in action:
            manage_keystrokes('right')
        if 'cursor_enter' in action:
            manage_keystrokes('enter')
        if 'cursor_space' in action:
            manage_keystrokes('space')
        if 'cursor_tab' in action:
            manage_keystrokes('tab')
        return

    def infinite_loop(self, action):
        """
        Runs an infinite loop
        :param action:
        :return:
        """
        strp = "while(True):"
        return strp

    def import_library(self, import_json):
        """
        Accept file name and return import statement for that file
        in format
        import filename
        """
        parameter = import_json.get('result').get('parameters')
        strp = "import" + parameter.pop('library')
        return strp

    def from_import_library(self, import_json):
        """
        Accept file name and return import statement for that file
        in format
        from file import module
        """
        parameter = import_json.get('result').get('parameters')
        strp = "from " + parameter.pop('library') + "import *"
        return strp

    def copy_line(self, copy_line_json):
        """
        Params passed will be line number
        which will be passed to manage_leystroke and that will
        create a copy of that line and paste it.
        :param copy_line_json:
        :return:
        """
        parameter = copy_line_json.get('result').get('parameters')
        line_number = parameter.pop('number')
        return copy(line_number)

    def setup_canvas(self):
        add_text("import pygame")
        add_text("screen = pygame.display.set_mode((640, 480))")
        add_text("screen.fill((0, 0, 0))")

    def draw_circle(self, circle_json):
        parameter = circle_json.get('result').get('parameters')
        radius = parameter.pop('radius')
        add_text("pygame.draw.circle(screen, (255, 255, 255), (320, 240), {0}, 2)".format(radius))
        add_text("nl tab pygame.display.flip()")

    def draw_line(self, line_json):
        parameter = line_json.get('result').get('parameters')
        length = parameter.pop('length')
        add_text("nl tab pygame.draw.line(screen, (0, 0, 255), (100, 0), (100, {0}))".format(length))
        add_text("nl tab pygame.display.flip()")