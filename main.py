#!/usr/bin/python

# lang : swedish
OPERATORS = {
    'plus': '+',
    'lägg till': '+',
    'minus': '-',
    'dra av': '-',
    'fler': '>',
    'mer': '>',
    'större': '>',
    'färre': '<',
    'mindre': '<',
    'delat': '/',
    'delad': '/',
    'gånger': '*',
}

NUMBERS = {
    'noll': 0,
    'ett': 1,
    'två': 2,
    'tre': 3,
    'fyra': 4,
    'fem': 5,
    'sex': 6,
    'sju': 7,
    'åtta': 8,
    'nio': 9,
    'tio': 10,
    'elva': 11,
    'tolv': 12,
    'tretton': 13,
    'fjorton': 14,
    'femton': 15,
    'sexton': 16,
    'sjutton': 17,
    'arton': 18,
    'nitton': 19,
    'tjugo': 20,
    # variations
    'en': 1
}

LANG = {
    True: 'Sant',
    False: 'Falskt',
}
# ./lang

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
    ast = ast.copy()
    while len(tokens) > 0:
        token = tokens[0]
        # number
        if str(token).isnumeric():
            tokens.remove(token)
            ast['children'].append(int(token))
        # otherwise
        elif ast['node'] and token in ['>', '<', '/', '*']:
            tokens.remove(token)
            ast = { 'node': token, 'children': [ast, parser({ 'node': None, 'children': [] }, tokens)] }
        else:
            tokens.remove(token)
            ast['node'] = token
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
        # print(text.strip())
        tokens = lexer(text)
        if debug: print('lexer: ', tokens)
        ast = parser({ 'node': None, 'children': [] }, tokens)
        if debug: print('parser: ', ast)
        # plus
        if ast['node'] == '+':
            return evaluate(ast['children'][0]) + evaluate(ast['children'][1])
        # minus
        if ast['node'] == '-':
            return evaluate(ast['children'][0]) - evaluate(ast['children'][1])
        # greater than
        if ast['node'] == '>':
            if (evaluate(ast['children'][0]) > evaluate(ast['children'][1])):
                return LANG[True]
            else:
                return LANG[False]
        # less than
        if ast['node'] == '<':
            if (evaluate(ast['children'][0]) < evaluate(ast['children'][1])):
                return LANG[True]
            else:
                return LANG[False]
        # divide
        if ast['node'] == '/':
            return int(evaluate(ast['children'][0]) / evaluate(ast['children'][1]))
        # multiply
        if ast['node'] == '*':
            return evaluate(ast['children'][0]) * evaluate(ast['children'][1])
    return

if (__name__ == "__main__"):
    assert(interpret('ett plus ett') == 2)
    assert(interpret('två minus tre') == -1)
    assert(interpret('fem myror är fler än fyra elefanter') == LANG[True])
    assert(interpret('två lasbilar är färre än en bil') == LANG[False])
    assert(interpret('två äpplen delat på två personer') == 1)
    assert(interpret('tre päron delat med två personer') == 1)
    assert(interpret('en glass delad med fyra personer') == 0)
    assert(interpret('ett plus ett är större än tre minus två') == LANG[True])
    assert(interpret('fyra ben gånger två kor') == 8)
    assert(interpret('två äpplen plus fyra päron är mer än ett päron') == LANG[True])
    assert(interpret('två kronor gånger ett är mindre än en krona gånger fyra') == LANG[True])
    assert(interpret('två gånger två gånger två') == 8)
    # file
    file = open('test.rakna', 'r')
    for line in file.readlines():
        result = interpret(line, False)
        if result:
            print(line, result, '\n')
