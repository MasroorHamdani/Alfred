from manage_keystrokes import manage_keystrokes


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
            str = parameter.pop('source_var') + ' = ' + parameter.pop('target_var')
        elif action in 'assign_val_to_var':
            str = parameter.pop('variable') + ' = ' + parameter.pop('value')
        else:
            str = "Error: Invalid Operation"
        return str

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
