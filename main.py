#!/usr/bin/python
import sys

COLORS = {
    'header': '\033[95m',
    'blue': '\033[94m',
    'cyan': '\033[96m',
    'green': '\033[92m',
    'warning': '\033[93m',
    'fail': '\033[91m',
    'end': '\033[0m',
    'bold': '\033[1m',
    'underline': '\033[4m',
}

PRECEDENCE = { '/': 2, '*': 2, '+': 1, '-': 1, '>': 0, '<': 0 }

# lexer
def lexer(line):
    lexemes = line.split(' ')
    tokens = []
    for lexeme in lexemes:
        lexeme = str(lexeme).strip().lower()
        # operators
        if lexeme in OPERATORS: 
            tokens.append(OPERATORS[lexeme])
        # numbers
        if lexeme in NUMBERS:
            tokens.append(NUMBERS[lexeme])
        # all other
        if lexeme not in NUMBERS and lexeme not in OPERATORS:
            pass

    return tokens

# parser : recursive-descent
def parser(ast, tokens):
    operator = []
    ast = ast.copy()
    while len(tokens) > 0:
        token = tokens[0]
        # number
        if str(token).isnumeric():
            tokens.remove(token)
            ast['children'].append(int(token))
        # operator
        elif token in PRECEDENCE:
            tokens.remove(token)
            # precedence
            while len(operator) > 0:
                op = operator.pop()
                if op in PRECEDENCE and PRECEDENCE[op] >= PRECEDENCE[token]:
                    ast['node'] = op
                    ast = { 'node': token, 'children': [ast, parser({ 'node': None, 'children': [] }, tokens)] }
                else:
                    operator.append(op)
                    break
            
            operator.append(token)
            # tokens.remove(token)
            # ast = { 'node': token, 'children': [ast, parser({ 'node': None, 'children': [] }, tokens)] }
        else:
            tokens.remove(token)
            ast['node'] = token

    while len(operator) > 0:
        op = operator.pop()
        ast['node'] = op
        # ast = { 'node': op, 'children': [ast, parser({ 'node': op, 'children': [] }, tokens)] }

    return ast

# evaluate
def evaluate(ast):
    # number
    if str(type(ast)) != "<class 'dict'>":
        return int(ast)
    if not ast['node']:
        return ast['children'][0]
    # plus
    if ast['node'] == '+':
        return evaluate(ast['children'][0]) + evaluate(ast['children'][1])
    # minus
    if ast['node'] == '-':
        return evaluate(ast['children'][0]) - evaluate(ast['children'][1])
    # divide
    if ast['node'] == '/':
        return evaluate(ast['children'][0]) / evaluate(ast['children'][1])
    # multiply
    if ast['node'] == '*':
        return evaluate(ast['children'][0]) * evaluate(ast['children'][1])

# interpret
def interpret(text, debug = False):
    if text.startswith('--') or text.isspace():
        return
    else:
        tokens = lexer(text)
        if debug:
            # print('lexer: ', tokens)
            print("  {}lexer (tokens): {}{}".format(COLORS['cyan'], tokens, COLORS['end']))
        ast = parser({ 'node': None, 'children': [] }, tokens)
        if debug:
            # print('parser: ', ast)
            print("  {}parser (AST): {}{}".format(COLORS['cyan'], ast, COLORS['end']))
        # plus
        if ast['node'] == '+':
            return evaluate(ast['children'][0]) + evaluate(ast['children'][1])
        # minus
        if ast['node'] == '-':
            return evaluate(ast['children'][0]) - evaluate(ast['children'][1])
        # greater than
        if ast['node'] == '>':
            if (evaluate(ast['children'][0]) > evaluate(ast['children'][1])):
                return BOOLEAN[True]
            else:
                return BOOLEAN[False]
        # less than
        if ast['node'] == '<':
            if (evaluate(ast['children'][0]) < evaluate(ast['children'][1])):
                return BOOLEAN[True]
            else:
                return BOOLEAN[False]
        # divide
        if ast['node'] == '/':
            return int(evaluate(ast['children'][0]) / evaluate(ast['children'][1]))
        # multiply
        if ast['node'] == '*':
            return evaluate(ast['children'][0]) * evaluate(ast['children'][1])
    return

if (__name__ == "__main__"):
    DEBUG = False
    # running
    print("{}Running {}raknalang{}{} interpreter...{}".format(COLORS['header'], COLORS['bold'], COLORS['end'], COLORS['header'], COLORS['end']))
    # tests
    if len(sys.argv) > 2 and sys.argv[2] == "--test":
        from lang.swe import *
        print(" {}Language: {}, running tests...{}".format(COLORS['header'], sys.argv[1][2:].capitalize(), COLORS['end']))
        for test in TEST_MAP:
            try:
                assert(interpret(test) == TEST_MAP[test])
                print("  {}{} => {}{}  {}OK{}".format(COLORS['cyan'], test, TEST_MAP[test], COLORS['end'], COLORS['green'], COLORS['end']))
            except:
                print("  {}{} => {}{}  {}FAILED{}".format(COLORS['cyan'], test, TEST_MAP[test], COLORS['end'], COLORS['fail'], COLORS['end']))
        print(" {}Tests done.{}".format(COLORS['header'], COLORS['end']))
        print("{}Exiting...{}".format(COLORS['header'], COLORS['end']))
    elif len(sys.argv) > 1:
        print(" {}Language: {}, type 'q' + ENTER to exit.{}".format(COLORS['header'], sys.argv[1][2:].capitalize(), COLORS['end']))
        # load lang
        if sys.argv[1] == '--swedish':
            from lang.swe import *
        # debug
        if len(sys.argv) > 2 and sys.argv[2] == "--debug":
            DEBUG = True
            print("  {}DEBUG MODE{}".format(COLORS['warning'], COLORS['end']))
        # interpret
        while True:
            line = input("  > ")
            # exit
            if line == "q":
                print("{}Exiting...{}".format(COLORS['header'], COLORS['end']))
                break
            # print
            print("  {}{}{}".format(COLORS['header'], interpret(line, DEBUG), COLORS['end']))
    else:
        print(" {}Usage: --lang --option{} (options: test, debug)".format(COLORS['warning'], COLORS['end']))

