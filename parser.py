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
        if action is 'print_string':
            str = 'print("' + parameter.pop('subject') + '")'
        elif action is 'print_variable':
            str = 'print(' + parameter.pop('variable') + ')'
        else:
            str = "Error: Invalid Operation"
        return str

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
        if action is 'assign_var_to_var':
            str = parameter.pop('source_var') + ' = ' + parameter.pop('target_var')
        elif action is 'assign_val_to_var':
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
            str = 'if ' + cond_list[0] + '<=' + cond_list[len(cond_list)-1] + ':\n'
        elif 'greater than' in condition and 'equal to' in condition:
            str = 'if ' + cond_list[0] + '>=' + cond_list[len(cond_list)-1] + ':\n'
        elif 'less than' in condition:
            str = 'if ' + cond_list[0] + '<' + cond_list[len(cond_list)-1] + ':\n'
        elif 'greater than' in condition:
            str = 'if ' + cond_list[0] + '>' + cond_list[len(cond_list) - 1] + ':\n'
        elif 'not equal to' in condition:
            str = 'if ' + cond_list[0] + '!=' + cond_list[len(cond_list) - 1] + ':\n'
        elif 'equal to' in condition:
            str = 'if ' + cond_list[0] + '==' + cond_list[len(cond_list) - 1] + ':\n'

        else:
            str = "Error: Invalid Operation"

        if 'Error' not in str:
            str += '    ' + action_list[0] + ' = ' + action_list[len(action_list) - 1]
        return str

    def for_loop_statement(self,for_loop_json):
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
        if action is 'loop':
            self.for_loop_content = 'for number in range(1,' + parameter.pop('range') + '):\n'
        if 'print' in action:
            self.for_loop_content += '    ' + self.print_statement(for_loop_json) + '\n'
        if 'assign' in action:
            self.for_loop_content += '    ' + self.assign_statement(for_loop_json) + '\n'
        if action is 'end_loop':
            self.for_loop_content += '\n'
        return self.for_loop_content