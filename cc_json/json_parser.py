import argparse
import os
from lexer import Lexer
from parser import Parser


class JSONParser:
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()

    def parse_json_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                input_text = file.read()
                tokens = self.lexer.tokenize(input_text)
                ast = self.parser.parse(tokens)
                return ast
        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")
            return None


if __name__ == '__main__':
    import sys
    parser = JSONParser()

    # Creating argument parser
    arg_parser = argparse.ArgumentParser(description = 'JSON Parser')
    arg_parser.add_argument("file_path, help = 'Path to the Json file to parse'")

    # Parse command line argument
    args = arg_parser.parse_args()

    # Make an attempt to parse the specified Json file
    ast = parser.parse_json_file(args.file_path)

    # check if parsing succeeded and exit with appropriate code as specified in challenge
    if ast:
        sys.exit(0)  # exit with code 0 for success
    else:
        sys.exit(1)  # exit with code 1 for failure


