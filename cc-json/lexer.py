import ply.lex as lex
from lexer_tokens import tokens


class GetToken:
    def __init__(self, token_type, token_value):
        self.type = token_type
        self.value = token_value


class SourceReader:
    def __init__(self, source_code):
        self.source_code = source_code

    def read_source(self):
        #  read the input source code from file
        with open(self.source_code, 'r') as file:
            return file.read()


class Lexer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.current_index = 0

    # Regular expression rules for simple tokens
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACE = r'\['
    t_RBRACE = r'\]'
    t_BLOCKSTART = r'\{'
    t_BLOCKEND = r'\}'
    t_COLON = r':'
    t_DOUBLE_QUOTE = r'"'

    # Regular expression rule for NUMBER and FLOAT
    @staticmethod
    def t_NUMBER(t):
        r'\d+'
        t.value = int(t.value)
        return t

    @staticmethod
    def t_FLOAT(t):
        r'(\d*\.\d+)|(\d+\.\d*)'
        t.value = float(t.value)
        return t

    # Regular expression rule for STRING
    @staticmethod
    def t_STRING(t):
        r'"([^"\\]|\\.)*"'  # Matches double-quoted strings, handling escape sequences
        t.value = t.value[1:-1]  # Remove the double quotes from the value
        return t

    # Regular expression rule for BOOLEAN
    @staticmethod
    def t_BOOLEAN(t):
        r'true|false'
        t.value = (t.value == 'true')  # Convert "true" to True, "false" to False
        return t

    # Error handling rule
    @staticmethod
    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Tokenize the input string
    def get_next_token(self):
        pass


# Build the lexer
def build(self, **kwargs):
    self.lexer = lex.lex(module=self, **kwargs)
