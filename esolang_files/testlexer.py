# test_lexer.py

from lexer import lexer

data = """
highkey x = 5;
highkey y = 10;
vibe_check (x ratios y) leftpilled
    shoutout ("x is greater than y");
rightmaxxer big_yikes leftpilled
    shoutout ("x is not greater than y");
rightmaxxer
"""

lexer.input(data)

for tok in lexer:
    print(tok)

