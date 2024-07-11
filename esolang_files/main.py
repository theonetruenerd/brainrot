from lexer import lexer
from parser import parser
from interpreter import Interpreter

def execute_esolang(code):
    lexer.input(code)
    print("Tokens:")
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
    
    ast = parser.parse(code, lexer=lexer)
    print("AST:", ast)
    
    interpreter = Interpreter()
    interpreter.interpret(ast)
    return interpreter.variables

# Example usage
if __name__ == "__main__":
    esolang_code = """
    highkey x = 5;
    highkey y = 10;
    vibe_check (x ratios y) leftpilled
        shoutout("x is greater than y");
    rightmaxxer big_yikes leftpilled
        shoutout("x is not greater than y");
    rightmaxxer
    """
    variables = execute_esolang(esolang_code)
    print("Variables:", variables)
