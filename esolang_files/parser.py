import ply.yacc as yacc
from lexer import tokens

precedence = (
    ('left', 'ASSIGN'),
)

def p_program(p):
    'program : statement_list'
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_statement(p):
    '''statement : declaration_statement
                 | assignment_statement
                 | if_statement
                 | while_statement
                 | expression_statement
                 | return_statement
                 | exit_statement
                 | try_statement
                 | print_statement
                 | raise_statement
                 | len_statement
                 | del_statement
                 | pass_statement
                 | input_statement
                 | import_statement
                 | def_statement
                 | empty'''
    p[0] = p[1]

def p_declaration_statement(p):
    '''declaration_statement : HIGHKEY IDENTIFIER ASSIGN expression SEMICOLON'''
    p[0] = ('declaration', p[2], p[4])

def p_assignment_statement(p):
    'assignment_statement : LOWKEY IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = ('assignment', p[2], p[4])

def p_if_statement(p):
    'if_statement : VIBECHECK LPAREN expression RPAREN LEFTPILLED statement_list RIGHTMAXXER else_clause'
    p[0] = ('if', p[3], p[6], p[8])

def p_else_clause(p):
    '''else_clause : BIGYIKES LEFTPILLED statement_list RIGHTMAXXER
                   | empty'''
    if len(p) == 2:
        p[0] = None
    else:
        p[0] = ('else', p[3])

def p_while_statement(p):
    'while_statement : GRIND LPAREN expression RPAREN LEFTPILLED statement_list RIGHTMAXXER'
    p[0] = ('while', p[3], p[6])

def p_expression_statement(p):
    'expression_statement : expression SEMICOLON'
    p[0] = ('expression', p[1])

def p_expression(p):
    '''expression : CAP
                  | NOCAP
                  | GG
                  | NUMBER
                  | STRING
                  | IDENTIFIER
                  | expression RATIOS expression'''
    p[0] = p[1]

def p_return_statement(p):
    'return_statement : ITSGIVING expression SEMICOLON'
    p[0] = ('return', p[2])

def p_exit_statement(p):
    'exit_statement : PERIODT SEMICOLON'
    p[0] = ('exit',)

def p_try_statement(p):
    'try_statement : FUCKAROUND LEFTPILLED statement_list RIGHTMAXXER except_clause'
    p[0] = ('try', p[3], p[5])

def p_except_clause(p):
    '''except_clause : FINDOUT LEFTPILLED statement_list RIGHTMAXXER
                     | empty'''
    if len(p) == 2:
        p[0] = None
    else:
        p[0] = ('except', p[3])

def p_print_statement(p):
    'print_statement : SHOUTOUT LPAREN expression RPAREN SEMICOLON'
    p[0] = ('print', p[3])

def p_raise_statement(p):
    'raise_statement : SPILLTEA exception_clause SEMICOLON'
    p[0] = ('raise', p[2])

def p_exception_clause(p):
    '''exception_clause : TEA
                        | CRINGE
                        | BRUH
                        | REDFLAG'''
    p[0] = p[1]

def p_len_statement(p):
    'len_statement : BODYCOUNT LPAREN expression RPAREN SEMICOLON'
    p[0] = ('len', p[3])

def p_del_statement(p):
    'del_statement : YEET IDENTIFIER SEMICOLON'
    p[0] = ('del', p[2])

def p_pass_statement(p):
    'pass_statement : SLEPTON SEMICOLON'
    p[0] = ('pass',)

def p_input_statement(p):
    'input_statement : YAP LPAREN expression RPAREN SEMICOLON'
    p[0] = ('input', p[3])

def p_import_statement(p):
    'import_statement : STAN expression SEMICOLON'
    p[0] = ('import', p[2])

#def p_add_to_dict_statement(p):
#    'add_to_dict_statement : SITUATIONSHIP IDENTIFIER LPAREN expression COMMA expression RPAREN SEMICOLON'
#    p[0] = ('add_to_dict', p[2], p[4], p[6])

def p_def_statement(p):
    'def_statement : NPC IDENTIFIER LPAREN RPAREN LEFTPILLED statement_list RIGHTMAXXER' 
    p[0] = ('def', p[2], p[6])

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at {p.value!r}, line {p.lineno}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
