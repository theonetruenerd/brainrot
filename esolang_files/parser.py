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
                 | break_statement
                 | create_dict_statement
                 | add_to_dict_statement
                 | init_logging_statement
                 | logging_statement
                 | lookup_dict_statement
                 | list_assignment_statement
                 | list_access_statement
                 | list_creation_statement
                 | empty'''
    p[0] = p[1]

def p_declaration_statement(p):
    'declaration_statement : HIGHKEY IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = ('declaration', p[2], p[4])

def p_assignment_statement(p):
    'assignment_statement : LOWKEY IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = ('assignment', p[2], p[4])

def p_if_statement(p):
    'if_statement : VIBECHECK LPAREN expression RPAREN LEFTPILLED statement_list RIGHTMAXXER elif_clauses else_clause'
    p[0] = ('if', p[3], p[6], p[8], p[9])

def p_elif_clauses(p):
    '''elif_clauses : elif_clauses MID LPAREN expression RPAREN LEFTPILLED statement_list RIGHTMAXXER 
                    | empty'''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = p[1] + [('elif', p[4], p[7])]

def p_else_clause(p):
    '''else_clause : BIGYIKES LEFTPILLED statement_list RIGHTMAXXER
                   | empty'''
    if len(p) == 2:
        p[0] = None
    else:
        p[0] = p[3]

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
                  | expression RATIOS expression
                  '''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == 'ratios':
        p[0] = ('ratios', p[1], p[3])

def p_return_statement(p):
    '''return_statement : ITSGIVING expression SEMICOLON
                        | ITSGIVING IDENTIFIER SEMICOLON'''
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
    '''print_statement : SHOUTOUT LPAREN expression RPAREN SEMICOLON
                       | SHOUTOUT LPAREN IDENTIFIER RPAREN SEMICOLON'''
    p[0] = ('print', p[3])

def p_raise_statement(p):
    '''raise_statement : BRUH CRINGE LEFTPILLED expression RIGHTMAXXER
                       | BRUH BASED LEFTPILLED expression RIGHTMAXXER'''
    p[0] = ('raise', p[2], p[4])

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
    'input_statement : IDENTIFIER BFFR LEFTPILLED expression RIGHTMAXXER'
    p[0] = ('input', p[1], p[4])

def p_import_statement(p):
    'import_statement : STAN expression SEMICOLON'
    p[0] = ('import', p[2])

def p_add_to_dict_statement(p):
    '''add_to_dict_statement : SITUATIONSHIP IDENTIFIER LEFTPILLED expression HOOKUP expression RIGHTMAXXER
                             | SITUATIONSHIP IDENTIFIER LEFTPILLED IDENTIFIER HOOKUP expression RIGHTMAXXER
                             | SITUATIONSHIP IDENTIFIER LEFTPILLED expression HOOKUP IDENTIFIER RIGHTMAXXER
                             | SITUATIONSHIP IDENTIFIER LEFTPILLED IDENTIFIER HOOKUP IDENTIFIER RIGHTMAXXER'''
    p[0] = ('add_to_dict', p[2], p[4], p[6])

def p_def_statement(p):
    'def_statement : NPC IDENTIFIER LPAREN RPAREN LEFTPILLED statement_list RIGHTMAXXER' 
    p[0] = ('def', p[2], p[6])

def p_break_statement(p):  # Doesnt seem to work
    'break_statement : GG SEMICOLON'
    p[0] = ('break')

def p_create_dict_statement(p):
    '''create_dict_statement : IYKYK IDENTIFIER LEFTPILLED expression SITUATIONSHIP expression RIGHTMAXXER
                             | IYKYK IDENTIFIER SEMICOLON'''
    if len(p) == 4:
        p[0] = ('init_dict', p[2])
    else:
        p[0] = ('create_dict', p[2], p[4], p[6])

def p_init_logging_statement(p):
    '''init_logging_statement : POURTEA TEA SEMICOLON
                              | POURTEA YAP SEMICOLON
                              | POURTEA OOF SEMICOLON
                              | POURTEA TWEAKING SEMICOLON
                              | POURTEA ICK SEMICOLON'''
    p[0] = ('init_logging', p[2])

def p_logging_statement(p):
    '''logging_statement : SPILLTEA TEA LEFTPILLED expression RIGHTMAXXER
                         | SPILLTEA YAP LEFTPILLED expression RIGHTMAXXER
                         | SPILLTEA OOF LEFTPILLED expression RIGHTMAXXER
                         | SPILLTEA TWEAKING LEFTPILLED expression RIGHTMAXXER
                         | SPILLTEA ICK LEFTPILLED expression RIGHTMAXXER'''
    p[0] = ('log',p[2],p[4])

def p_lookup_dict_statement(p):
    'lookup_dict_statement : IDENTIFIER SNEAKYLINK IDENTIFIER LEFTPILLED expression RIGHTMAXXER'
    p[0] = ('lookup',p[1],p[3],p[5])

def p_list_assignment_statement(p):
    'list_assignment_statement : MANDEM IDENTIFIER LEFTPILLED expression RIGHTMAXXER expression SEMICOLON'
    p[0] = ('add_to_list',p[2],p[4],p[6])

def p_list_access_statement(p):
    'list_access_statement : IDENTIFIER GETYOURBOY IDENTIFIER expression SEMICOLON'
    p[0] = ('get',p[1],p[3],p[4])

def p_list_creation_statement(p):
    'list_creation_statement : IDENTIFIER HOMIES elements NOHOMO'
    p[0] = ('list',p[1],p[3])

def p_elements(p):
    '''elements : elements COMMA expression
                | expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at {p.value!r}, line {p.lineno}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
