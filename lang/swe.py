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
BOOLEAN = {
    True: 'Sant',
    False: 'Falskt',
}
TEST_MAP = {
    'ett plus ett': 2,
    'två minus tre': -1,
    'fem myror är fler än fyra elefanter': BOOLEAN[True],
    'två lasbilar är färre än en bil': BOOLEAN[False],
    'två äpplen delat på två personer': 1,
    'tre päron delat med två personer': 1,
    'en glass delad med fyra personer': 0,
    'ett plus ett är större än tre minus två': BOOLEAN[True],
    'fyra ben gånger två kor': 8,
    'två äpplen plus fyra päron är mer än ett päron': BOOLEAN[True],
    'två kronor gånger ett är mindre än en krona gånger fyra': BOOLEAN[True],
    'två gånger två gånger två': 8,
    'ett gånger två minus två gånger fyra': -6,
}
# ./lang