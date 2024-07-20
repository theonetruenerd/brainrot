import sys
import importlib
from parser import parser
import logging
import re

# A dictionary to hold variable values
symbol_table = {}

# Function to evaluate expressions
def eval_expression(expr):
    if isinstance(expr, int) or isinstance(expr, str):
        return expr
    elif isinstance(expr, tuple):
        op, *args = expr
        if op == 'assign':
            var, value = args
            if isinstance(value, type(symbol_table[var])):
                symbol_table[var] = eval_expression(value)
                return symbol_table[var]
            else:
                raise Exception('Invalid type')
        elif op == 'identifier':
            return symbol_table.get(args[0], None)
        elif op == 'number':
            return int(args[0])
        elif op == 'string':
            return str(args[0])
        elif op == 'ratios':
            return eval_expression(args[0]) > eval_expression(args[1])
        elif op == 'situationship':
            return {args[0]: args[1]}
        elif op == 'valid':
            if symbol_table[args[0]]:
                return True
            else:
                return False
    return expr

# Function to call functions

def func_call(func_name, func_args):
    func_def = symbol_table[func_name]
    if func_def[0] != 'def':
        raise TypeError(f"{func_name} is not a function")
    _, param_names, body = func_def
    if len(func_args) != len(param_names):
        raise TypeError(f"{func_name} expected {len(param_names)} arguments, recieved {len(func_args)}")
    
    backup_symbol_table = symbol_table.copy()
    for param, arg in zip(param_names, func_args):
        symbol_table[param] = arg

    exec_statement_list(body)   

    symbol_table.clear()
    symbol_table.update(backup_symbol_table)

# Function to execute statements
def exec_statement(statement):
    if not statement:
        return
    stmt_type = statement[0]
    if stmt_type == 'declaration':
        _, var, vartype, value = statement
        try:
            if vartype == 'ghost':
                value = float(value)
            elif vartype == 'lead_on':
                value = str(value)
            elif vartype == 'basic':
                value = int(value)
            elif vartype == 'bet':
                value = bool(value)
        except:
            raise Exception('Type declared and value are not compatible.')
        symbol_table[var] = eval_expression(value)
    elif stmt_type == 'assignment':
        _, var, value = statement
        symbol_table[var] = eval_expression(value)
    elif stmt_type == 'if':
        _, condition, true_block, elif_clauses, else_block = statement
        if eval_expression(condition):
            exec_statement_list(true_block)
        else:
            executed = False
            for elif_clause in elif_clauses:
                _, elif_condition, elif_block = elif_clause
                if eval_expression(elif_condition):
                    exec_statement_list(elif_block)
                    executed = True
                    break
            if not executed and else_block:
                exec_statement_list(else_block)
    elif stmt_type == 'while':
        _, condition, block = statement
        while eval_expression(condition):
            exec_statement_list(block)
    elif stmt_type == 'expression':
        eval_expression(statement[1])
    elif stmt_type == 'return':
        print(f"Return: {eval_expression(statement[1])}")
    elif stmt_type == 'exit':
        print("Exiting...")
        sys.exit()
    elif stmt_type == 'try':
        _, try_block, except_block = statement
        try:
            exec_statement_list(try_block)
        except Exception as e:
            exec_statement_list(except_block)
    elif stmt_type == 'print':
        identifier_or_expression = statement[1]
        if identifier_or_expression == 'identifier_print':
            if statement[2] in symbol_table:
                print(symbol_table[statement[2]])
            else:
                raise Exception('Identifier not found in symbol table.')
        elif identifier_or_expression == 'expression_print':
            print(eval_expression(statement[2]))
        else:
            raise Exception('Invalid print type')
    elif stmt_type == 'raise':
        _, raisetype, exc = statement
        if raisetype == 'cringe':
            raise Exception(eval_expression(exc))
        elif raisetype == 'based':
            raise OSError(eval_expression(exc))
    elif stmt_type == 'len':
        symbol_table[statement[1]] = (len(symbol_table[statement[2]]))
    elif stmt_type == 'del':
        var = statement[1]
        if var in symbol_table:
            del symbol_table[var]
    elif stmt_type == 'pass':
        pass
    elif stmt_type == 'input':
        _, var, prompt = statement
        input_value = input(eval_expression(prompt))
        symbol_table[var] = input_value
    elif stmt_type == 'import':
        _, lib = statement
        lib_name = eval_expression(lib)
        try:
            importlib.import_module(lib_name)
        except ImportError:
            print(f"Error: Could not import module {lib_name}")
    elif stmt_type == 'def':
        _, func_name, params, body = statement
        symbol_table[func_name] = ['def',params, body]
    elif stmt_type == 'init_dict':
        _, var = statement
        symbol_table[var] = {}
    elif stmt_type == 'create_dict':
        _, name, key, value = statement
        symbol_table[name] = {}
        symbol_table[name][eval_expression(key)] = eval_expression(value)
    elif stmt_type == 'add_to_dict':
        _, name, key, value = statement
        symbol_table[name][eval_expression(key)] = eval_expression(value)
    elif stmt_type == 'lookup':
        _, var, dict_name, key = statement
        symbol_table[var] = symbol_table[dict_name][eval_expression(key)]
    elif stmt_type == 'init_logging':
        _, logging_level = statement
        if logging_level == 'yap':
            logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        elif logging_level == 'tea':
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        elif logging_level == 'ick':
            logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
        elif logging_level == 'oof':
            logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
        elif logging_level == 'tweaking':
            logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(levelname)s - %(message)s')
    elif stmt_type == 'log':
        _, logging_level, expression = statement
        if logging_level == 'yap':
            logging.debug(eval_expression(expression))
        elif logging_level == 'tea':
            logging.info(eval_expression(expression))
        elif logging_level == 'ick':
            logging.warning(eval_expression(expression))
        elif logging_level == 'oof':
            logging.error(eval_expression(expression))
        elif logging_level == 'tweaking':
            logging.critical(eval_expression(expression))
    elif stmt_type == 'list':
        _, var, elems = statement
        symbol_table[var] = [eval_expression(elem) for elem in elems]
    elif stmt_type == 'get':
        _, ind, ls, elem = statement
        symbol_table[ind] = symbol_table[ls].index(eval_expression(elem))
    elif stmt_type == 'add_to_list':
        _, ls, item, ind = statement
        symbol_table[ls].insert(eval_expression(ind), eval_expression(item))
    elif stmt_type == 'loop_through_list':
        _, ls, identifier_tag, block = statement
        for item in symbol_table[ls]:
            symbol_table[identifier_tag] = item
            exec_statement_list(block)
        del symbol_table[identifier_tag]
    elif stmt_type == 'call':
        _,func_name, params = statement
        func_call(func_name, params)
    elif stmt_type == 'read':
        _, var, filename = statement
        symbol_table[var] = []
        with open(eval_expression(filename), 'r', encoding='utf-8') as f:
            for line in f:
                symbol_table[var].append(line)
            f.close()
    elif stmt_type == 'find_substring':
        _, var, string, substring = statement
        if var in symbol_table:
            del symbol_table[var]
        if substring in symbol_table:
            substring = symbol_table[substring]
        if string in symbol_table:
            string = symbol_table[string]
        if substring in string:
            symbol_table[var] = True
        else:
            symbol_table[var] = False
    elif stmt_type == 'extract_string':
        _, var, string, substring = statement
        if substring in symbol_table:
            substring = symbol_table[substring]
        if string in symbol_table:
            string = symbol_table[string]
        symbol_table[var] = re.findall(eval_expression(substring), string)
    elif stmt_type == 'is_true':
        _, var, expr = statement
        if eval_expression(expr) == True:
            symbol_table[var] = True
        else:
            symbol_table[var] = False


class BreakLoop(Exception):
    pass

# Function to execute a list of statements
def exec_statement_list(statements):
    for statement in statements:
        stmt_type = statement[0]
        if stmt_type == 'break':
            raise BreakLoop()
        else:
            exec_statement(statement)

# Function to interpret the parsed program
def interpret(program):
    ast = parser.parse(program)
    exec_statement_list(ast)

# Main execution
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python interpreter.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        program = file.read()
    
    interpret(program)
