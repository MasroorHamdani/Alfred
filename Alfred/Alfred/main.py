from parser import Parser
from test_data import get_print_string_data, get_print_variable_data,\
    assign_var_to_var, assign_val_to_var, if_cond_data, loop_condition_data,\
    loop_execute_data, loop_end_data, import_json

if __name__ == '__main__':
    """
    Entry point for script
    """
    PARSER = Parser()
    print(PARSER.print_statement(get_print_string_data()))
    print(PARSER.print_statement(get_print_variable_data()))
    print(PARSER.assign_statement(assign_var_to_var()))
    print(PARSER.assign_statement(assign_val_to_var()))
    print(PARSER.if_statement(if_cond_data()))
    print(PARSER.for_loop_statement(loop_condition_data()))
    print(PARSER.for_loop_statement(loop_execute_data()))
    print(PARSER.for_loop_statement(get_print_string_data()))
    print(PARSER.for_loop_statement(assign_var_to_var()))
    print(PARSER.for_loop_statement(assign_val_to_var()))
    print(PARSER.for_loop_statement(loop_end_data()))
    print(PARSER.import_library(import_json()))

