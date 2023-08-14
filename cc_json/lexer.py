from lexer_tokens import Token_Definitions
import re


class GetToken:
    def __init__(self, token_type, token_value, curr_position):
        self.type = token_type
        self.position = curr_position
        self.value = token_value


class Lexer:
    def __init__(self, input_text):
        self.text = input_text
        self.position = 0
        self.tokens = []

    # Tokenize the input string
    def tokenize(self, input_text):
        while self.position < len(self.text):
            self.get_next_token()

    def get_next_token(self):
        for token_type, rgx in Token_Definitions:
            pattern = re.compile(rgx)
            match = pattern.match(self.text, pos=self.position)
            if match:
                value = match.group()
                self.position += len(value)
                token = GetToken(token_type, value, self.position)
                self.tokens.append(token)
                return
        raise ValueError("Unrecognized token")

