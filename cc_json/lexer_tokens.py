"""
This module contains the lexing rules for the JSON lexer.

Token_Definitions is a list of tuples where each tuple represents a token definition.
The format of each tuple is: (token_name, regex_pattern)

Here's what each token definition represents:

- 'QUOTED_STRING': Matches a double-quoted string in the JSON input.
- 'NUMBER': Matches a numeric value, which can be an integer, floating-point number, or scientific notation.
- 'OPEN_BRACE': Matches an opening curly brace '{'.
- 'CLOSE_BRACE': Matches a closing curly brace '}'.
- 'OPEN_BRACKET': Matches an opening square bracket '['.
- 'CLOSE_BRACKET': Matches a closing square bracket ']'.
- 'COMMA': Matches a comma ',' used for separating elements in arrays and key-value pairs.
- 'COLON': Matches a colon ':' used to separate keys and values in JSON objects.
- 'NULL': Matches the literal value 'null' in JSON.
- 'TRUE': Matches the literal value 'true' in JSON.
- 'FALSE': Matches the literal value 'false' in JSON.
- 'WHITESPACE': Matches one or more whitespace characters (spaces, tabs, newlines, etc.).
- 'EOF': Represents the end of the input string.

Token definitions are ordered so that longer matching patterns are tried first to avoid conflicts.

"""


Token_Definitions = [
    ('QUOTED_STRING', r'(?![-0-9])".*?(?<!\\)"'),  # To  resolve lexical ambiguity
    ('NUMBER', r'-?(?:0|[1-9]\d*)(?:\.\d+)?(?:e[-+]\d+)?'),
    ('OPEN_BRACE', r'\{'),
    ('CLOSE_BRACE', r'\}'),
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
