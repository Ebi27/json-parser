# This module contains the lexing rules

tokens = [
    # BRACKETS #
    'LPAREN',  # (
    'RPAREN',  # )
    'LBRACE',  # [
    'RBRACE',  # ]
    'BLOCKSTART',  # {
    'BLOCKEND',  # }

    # DATA TYPES #
    'INTEGER',  # int
    'FLOAT',  # dbl
    'STRING',
    'ARRAY',
    'BOOLEAN',
    'NULL',
    'OBJECT',

    # SYMBOLS #
    'COLON',  # :
    'DOUBLE_QUOTE',  # "

    'COMMENT',  # --
]
