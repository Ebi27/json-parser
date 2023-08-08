# This module contains the lexing rules

Token_Definitions = [
    # Token definition order is done in a way that the bigger entities are matched first.
    # (name, regex)
    ('QUOTED_STRING', r'(?![-0-9])".*?(?<!\\)"'),  # To  resolve lexical ambiguity
    ('NUMBER', r'-?(?:0|[1-9]\d*)(?:\.\d+)?(?:e[-+]\d+)?'),
    ('OPEN_BRACE', r'{'),
    ('CLOSE_BRACE', r'}'),
    ('OPEN_BRACKET', r'\['),
    ('CLOSE_BRACKET', r'\]'),
    ('COMMA', r','),
    ('COLON', r':'),
    ('NULL', r'null'),
    ('TRUE', r'true'),
    ('FALSE', r'false'),
    ('WHITESPACE', r'\s+'),
    ('EOF', r'^$')
]
