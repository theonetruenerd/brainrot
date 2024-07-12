import sys
import importlib
from parser import parser
import logging

# A dictionary to hold variable values
symbol_table = {}

# Function to evaluate expressions
def eval_expression(expr):
    if isinstance(expr, int) or isinstance(expr, str):
        return expr
    elif isinstance(expr, tuple):
        op, arg1, arg2 = expr
        if op == 'assign':
            symbol_table[arg1] = eval_expression(arg2)
            return symbol_table[arg1]
        elif op == 'identifier':
            return symbol_table.get(arg1, None)
        elif op == 'number':
            return int(arg1)
        elif op == 'string':
            return str(arg1)
        elif op == 'ratios':
            return eval_expression(arg1) > eval_expression(arg2)
        elif op == 'situationship':
            return {arg1:arg2}
    return expr

# Function to execute statements
def exec_statement(statement):
    if not statement:
        return
    stmt_type = statement[0]
    if stmt_type == 'declaration':
        _, var, value = statement
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
        while eval_expression(condition):  # This doesn't seem to recheck condition for loops so just continues
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
            exec_statement(except_block)
    elif stmt_type == 'print':
        identifier_or_expression = statement[1]
        if identifier_or_expression in symbol_table:
            print(symbol_table[identifier_or_expression])
        else:
            print(eval_expression(statement[1]))
    elif stmt_type == 'raise':
        _, raisetype, exc = statement
        if raisetype == 'cringe':
            raise Exception(eval_expression(exc))
        elif raisetype == 'based':
            raise OSError(eval_expression(exc))
    elif stmt_type == 'len':
        print(len(eval_expression(statement[1])))
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
            lib_name = importlib.import_module(lib_name)
        except ImportError:
            print(f"Error: Could not import module {lib_name}")
    elif stmt_type == 'def':
        pass  # Function definitions can be handled here
    elif stmt_type == 'init_dict':
        _, var = statement
        symbol_table[var] = {}
    elif stmt_type == 'create_dict':
        _, name, key, value = statement
        if key in symbol_table:
            key = symbol_table[key]
        if value in symbol_table:
            value = symbol_table[value]
        symbol_table[name] = {}
        symbol_table[name][eval_expression(key)] = eval_expression(value)
    elif stmt_type == 'add_to_dict':
        _, name, key, value = statement
        if key in symbol_table:
            key = symbol_table[key]
        if value in symbol_table:
            value = symbol_table[value]
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
        var_list = []
        for elem in elems:
            var_list.append(eval_expression(elem))
        symbol_table[var] = var_list
    elif stmt_type == 'get':
        _, ind, ls, elem = statement
        if ls in symbol_table:  # Add in error catch
            symbol_table[ind] = symbol_table[ls].index(elem)
    elif stmt_type == 'add_to_list':
        _, ls, item, ind = statement
        if ls in symbol_table:  # Add in error catch
            symbol_table[ls] = symbol_table[ls].insert(item,ind)
# Function to execute a list of statements
def exec_statement_list(statements):
    for statement in statements:  
        stmt_type = statement[0]
        if stmt_type == 'break':
            break
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
