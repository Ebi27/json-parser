import argparse
import sys
from cc_json.lexer import Lexer
from cc_json import parser

sys.path.append('/json-parser')


class JSONParser:
    """
    A simple JSON parser class that uses a lexer and parser to validate JSON files.
    """

    def __init__(self):
        """
        Initializes the JSONParser with a lexer and parser.
        """
        self.lexer = Lexer()
        self.parser = parser.Parser()

    def parse_json_file(self, file_path):
        """
        Parses a JSON file using the provided file path.

        Args:
            file_path (str): The path to the JSON file to parse.

        Returns:
            None
        """
        tokens = self.lexer.tokenize(file_path)

        if tokens is None:
            print("Invalid")
            print("Setting exit code to 1")
            sys.exit(1)

        if not tokens:
            print("Invalid")
            sys.exit(1)

        ast = self.parser.parse(tokens)
        if ast:
            print("Valid")
            sys.exit(0)
        else:
            print("Invalid")
            sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='JSON Parser')
    parser.add_argument("file_path", help="Path to the JSON file to parse")
    args = parser.parse_args()

    json_parser = JSONParser()
    json_parser.parse_json_file(args.file_path)
