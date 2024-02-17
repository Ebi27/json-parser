# parser.py - Parses the tokens generated by the lexer and constructs the JSON data structure

class Parser:
    def __init__(self):
        """
        Initializes the Parser with attributes for managing tokens and parsing process.
        """
        self.tokens = []
        self.stack = []

    def expect_token(self, expected_type):
        if not self.tokens:
            raise ValueError('Expected token of type', expected_type, 'but got end of input')
        token = self.tokens[0]
        if token.type != expected_type:
            raise ValueError('Expected token of type', expected_type, 'but got', token.type)

    def parse(self, tokens):
        """
        Parses a list of tokens to construct the JSON data structure.

        Args:
            tokens (list): A list of tokens generated by the lexer.

        Returns:
            dict or list: The parsed JSON data structure.
        """
        self.tokens = tokens
        self.handle_whitespace()  # Handle leading whitespace tokens

        self.stack.append(('START', None))

        while self.stack:
            action, data = self.stack.pop()
            if action == 'START':
                self.parse_json()

    def parse_json(self):
        """
        Parses the input JSON data structure iteratively based on the current token type.

        Returns:
            dict, list, str, int, float, bool, None: The parsed JSON data structure based on the token type.

        Raises:
            ValueError: If an unexpected token type is encountered or if there are no tokens to parse.
        """
        if self.tokens:
            token = self.tokens.pop(0)

            if token.type == 'OPEN_BRACE':
                return self.parse_object()
            elif token.type == 'OPEN_BRACKET':
                return self.parse_array()
            elif token.type == 'QUOTED_STRING':
                return self.parse_string()
            elif token.type == 'NUMBER':
                return self.parse_number()
            elif token.type == 'TRUE' or token.type == 'FALSE':
                return self.parse_boolean()
            elif token.type == 'NULL':
                return self.parse_null()
            else:
                raise ValueError(f'Unexpected token type: {token.type}')
        else:
            raise ValueError('Invalid: No tokens to parse')

    # Implement methods for parsing object, array, string, number, boolean, and null
    def parse_object(self):
        """
        Parses a JSON object.

        Returns:
            dict: The parsed JSON object.

        An object is an unordered set of name/value pairs.
        In JSON, an object takes this form;
         An object begins with {left brace and ends with }right brace.
        Each name is followed by :colon and the name/value pairs are separated by ,comma.
        """
        obj = {}

        while self.tokens:
            token = self.tokens.pop(0)  # Consume token from beginning
            if token.type == 'CLOSE_BRACE':
                return obj
            elif token.type == 'QUOTED_STRING':
                key = self.parse_string()
                self.expect_token('COLON')
                # it'll throw an error if there is no colon as each name has to be followed by a colon
                value = self.parse_json()
                obj[key] = value
                if token.type[0] == 'COMMA':
                    self.tokens.pop(0)
                elif token.type[0] == 'CLOSE_BRACKET':
                    self.tokens.pop(0)
            else:
                raise ValueError('Expected an opening brace or closing brace but got ' + self.tokens[0].type)

    def parse_array(self):
        """
        Parses a JSON array.

        Returns:
            list: The parsed JSON array.


        NOTE: An array is an ordered collection of values. An array begins with [left bracket and ends with ]right bracket.
        Values are separated by ,comma.

        A value can be a string in double quotes, or a number, or true or false or null, or an object or an array.
        These structures can be nested.
        """
        arr = []
        while self.tokens:
            token = self.tokens.pop(0)

            if token.type == 'CLOSE_BRACKET':
                return arr
            elif token.type in [''
                                'QUOTED_STRING',
                                'NUMBER',
                                'TRUE',
                                'FALSE',
                                'NULL',
                                'OPEN_BRACE',
                                'OPEN_BRACKET'
                                ]:
                value = self.parse_json()
                arr.append(value)
                if token.type[0] == 'COMMA':
                    self.tokens.pop(0)
                elif token.type[0] == 'CLOSE_BRACKET':
                    self.tokens.pop(0)
            else:
                raise ValueError('Expected an opening bracket but got ' + self.tokens[0].type)

    def parse_string(self):
        """
        Parses a JSON string.

        Returns:
            str: The parsed JSON string.

        A string is a sequence of zero or more Unicode characters, wrapped in double quotes, using backslash escapes.
         A character is represented as a single character string.
        """
        # To ensure there are tokens to parse
        if self.tokens:
            token = self.tokens.pop(0)

            if token.type == 'QUOTED_STRING':
                value = token.value[1:-1]  # Remove the surrounding quotes
                # Handle escape sequences within the string
                value = self.handle_escape_sequences(value)
                return value  # Return the parsed string value
            # If no tokens or token is not of the expected type, raise an error
            else:
                raise ValueError('Expected a quoted string but got ' + str(token.type))

    @staticmethod
    def handle_escape_sequences(value):
        """
        Handles escape sequences within a JSON string.

        Args:
            value (str): The string containing escape sequences.

        Returns:
            str: The string with escape sequences replaced by corresponding characters.
        """
        # Define a dictionary to map escape sequences to their respective characters
        escape_sequences = {
            r'\\"': '"',  # double quotation mark U+0022
            r"\\'": "'",  # single quotation mark
            r'\\n': '\n',  # line feed             U+000A
            r'\\r': '\r',  # carriage return       U+000D
            r'\\t': '\t',  # tab                   U+0009
            r'\\b': '\b',  # backspace             U+0008
            r'\\f': '\f',  # form feed             U+000C
            r'\\/': '/',  # solidus               U+002F
            r"\\\\": '\\',  # reverse solidus       U+005C
            r'\\u': 'u',
            r'\s+': '+'
        }

        # Replace escape sequences with their corresponding characters
        for escape_seq, char in escape_sequences.items():
            value = value.replace(escape_seq, char)

        return value

    def parse_number(self):
        """
        Parses a JSON number.

        Returns:
            str: The parsed JSON number.
        """
        if self.tokens:
            token = self.tokens.pop(0)

            if token.type == 'NUMBER':
                return token

    def parse_boolean(self):
        """
        Parses a JSON boolean value.
        """
        if self.tokens:
            token = self.tokens.pop(0)
            if token.type == 'TRUE':
                return token
            elif token.type == 'FALSE':
                return token

    def handle_whitespace(self):
        """
        Handles whitespace tokens in the token list.
        """
        while self.tokens:
            token = self.tokens[0]
            if token.type == 'WHITESPACE':
                self.tokens.pop(0)  # Consume the whitespace token
            else:
                break

    def parse_null(self):
        """
        Parses a JSON null value.
        """
        if self.tokens:
            token = self.tokens.pop(0)
            if token.type == 'NULL':
                return token
