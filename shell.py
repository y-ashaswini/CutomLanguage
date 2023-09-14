from lexer import Lexer
from parse import Parse
from interpreter import Interpreter

cont = 1
while cont == 1:
    text = input("Enter your text: ")
    lexer = Lexer(text)
    lexer.tokenize()
    tokens = lexer.return_tokens()
    lexer.print_tokens()

    parser = Parse(tokens)
    tree = parser.parse()

    interpret = Interpreter(tree)
    result = interpret.interpret()
    print("computed result: ", result.type, result.value)

print("terminated.")
