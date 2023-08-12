# parser.py - Parses the tokens generated by the lexer and constructs the JSON data structure


class JSONParser:
    def __init__(self):
        self.tokens = []
        self.curr_token = None
        self.current_index = 0

    def parse(self, tokens):
        self.tokens = tokens
        self.current_index = 0
        self.curr_token = self.tokens[self.current_index]

        return self.parse_json()

    def consume_token(self):
        self.current_index += 1
        if self.current_index < len(self.tokens):
            self.curr_token = self.tokens[self.current_index]
        else:
            self.curr_token = None

    # This method ensures that the current token matches the expected types before proceeding with parsing.
    def expect_token(self, expected_type):
        if self.curr_token and self.curr_token.type == expected_type:
            self.expect_token(self.curr_token)
        else:
            raise ValueError(f"Expected token of type '{expected_type}' but got '{self.curr_token.type}'")

        # This is the entry point for the JSON Parsing.

    def parse_json(self):
        if self.curr_token:
            token_type = self.curr_token.type

            if token_type == "OPEN_BRACE":
                return self.parse_object()
            elif token_type == "OPEN_BRACKET":
                return self.parse_array()
            elif token_type == "QUOTED_STRING":
                return self.parse_string()
            elif token_type == "NUMBER":
                return self.parse_number()
            elif token_type == "TRUE" or token_type == "FALSE":
                return self.parse_boolean()
            elif token_type == "NULL":
                return self.parse_null()
            else:
                raise ValueError(f"Unexpected token type: {token_type}")
        else:
            raise ValueError("No tokens to parse")

    # Implement methods for parsing object, array, string, number, boolean, and null
    def parse_object(self):
        if self.curr_token.type == "OPEN_BRACE":
            self.consume_token()  # Consume the opening brace '{'
            obj = {}
            while self.curr_token and self.curr_token.type != "CLOSE_BRACE":
                key = self.parse_string()  # Parse the key (string)
                self.expect_token("COLON")  # Expect a colon after the key
                value = self.parse_json()  # Parse the value (any JSON type)

                obj[key] = value
                if self.curr_token and self.curr_token.type == "COMMA":
                    self.consume_token()  # Consume the comma between key-value pairs
                elif self.curr_token and self.curr_token.type != "CLOSE_BRACE":
                    raise ValueError("Expected a comma or closing brace after value")

            self.expect_token("CLOSE_BRACE")  # Expect a closing brace '}'
            return obj
        else:
            raise ValueError("Expected an opening brace but got " + self.curr_token.type)

    def parse_string(self):
        if self.curr_token.type == "QUOTED_STRING":
            value = self.curr_token.value[1:-1]  # Remove the surrounding quotes
            # Handle escape sequences within the string
            value = self.handle_escape_sequences(value)
            self.consume_token()  # Consume the string token
            return value
        else:
            raise ValueError("Expected a quoted string but got " + self.curr_token.type)

    def handle_escape_sequences(self, value):
        # Define a dictionary to map escape sequences to their respective characters
        escape_sequences = {
            r'\\"': '"',
            r"\\'": "'",
            r'\\n': '\n',
            r'\\r': '\r',
            r'\\t': '\t',
            r'\\b': '\b',
            r'\\f': '\f',
            r'\\/': '/',
            r'\\u': 'u',
            r'\s+': '+'
        }

        # Replace escape sequences with their corresponding characters
        for escape_seq, char in escape_sequences.items():
            value = value.replace(escape_seq, char)

        return value

    def parse_array(self):
        pass

    def parse_number(self):
        pass

    def parse_boolean(self):
        pass

    def parse_null(self):
        pass
