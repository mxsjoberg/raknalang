#!/usr/bin/python

# FILLERS = {
#     'är': None,
#     'än': None,
# }

OPERATORS = {
    'plus': '+',
    'minus': '-',
    'fler': '>',
    'mer': '>',
    'färre': '<',
    'mindre': '<',
    'delat': '/'
}

NUMBERS = {
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
    # additionals
    'en': 1,
}

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

def parser(tokens):
    ast = {
        'node': None,
        'children': [],
    }
    for token in tokens:
        if str(token).isnumeric():
            ast['children'].append(int(token))
        else:
            ast['node'] = token
    return ast

def interpret(file):
    for line in file.readlines():
        if line.startswith('--') or line.isspace():
            pass
        else:
            print(line.strip())
            tokens = lexer(line)
            ast = parser(tokens)
            # plus
            if ast['node'] == '+':
                print(ast['children'][0] + ast['children'][1])
            # minus
            if ast['node'] == '-':
                print(ast['children'][0] - ast['children'][1])
            # greater
            if ast['node'] == '>':
                if (ast['children'][0] > ast['children'][1]):
                    print('Sant')
                else:
                    print('Falskt')
            # less
            if ast['node'] == '<':
                if (ast['children'][0] < ast['children'][1]):
                    print('Sant')
                else:
                    print('Falskt')
            # divide
            if ast['node'] == '/':
                print('%d (kvar: %d)' % (int(ast['children'][0] / ast['children'][1]), int(ast['children'][0] % ast['children'][1])))
            print('')
    return

if (__name__ == "__main__"):
    file = open('test.rakna', 'r')
    interpret(file)
