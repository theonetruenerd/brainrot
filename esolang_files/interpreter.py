import sys
from parser import parser

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
        _, condition, true_block, else_block = statement
        if eval_expression(condition):
            exec_statement_list(true_block)
        elif else_block:
            exec_statement(else_block)
    elif stmt_type == 'else':
        _, block = statement
        exec_statement_list(block)
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
            exec_statement(except_block)
    elif stmt_type == 'print':
        print(eval_expression(statement[1]))
    elif stmt_type == 'raise':
        _, exc = statement
        raise Exception(eval_expression(exc))
    elif stmt_type == 'len':
        print(len(eval_expression(statement[1])))
    elif stmt_type == 'del':
        var = statement[1]
        if var in symbol_table:
            del symbol_table[var]
    elif stmt_type == 'pass':
        pass
    elif stmt_type == 'input':
        var = statement[1]
        symbol_table[var] = input()
    elif stmt_type == 'import':
        var = statement[1]
        exec(open(var).read())
    elif stmt_type == 'def':
        pass  # Function definitions can be handled here

# Function to execute a list of statements
def exec_statement_list(statements):
    for statement in statements:
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
