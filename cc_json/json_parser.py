import argparse
import sys
from lexer import Lexer
from parser import Parser

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
        self.parser = Parser()

    def parse_json_file(self, file_path):
        """
        Parses a JSON file using the provided file path.

        Args:
            file_path (str): The path to the JSON file to parse.

        Returns:
            None
        """
        tokens = self.lexer.tokenize(file_path)
        ast = self.parser.parse(tokens)
        print(ast)

        if ast:
            print("Valid")
            sys.exit(0)
        else:
            print("Invalid JSON file")
            sys.exit(1)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='JSON Parser')
    arg_parser.add_argument("file_path", help="Path to the JSON file to parse")
    args = arg_parser.parse_args()

    print("File path:", args.file_path)

    json_parser = JSONParser()
    print("Instantiated JSONParser")
    json_parser.parse_json_file(args.file_path)
