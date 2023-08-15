import argparse
import sys
from lexer import Lexer
from parser import Parser


class JSONParser:
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()

        arg_parser = argparse.ArgumentParser(description='JSON Parser')
        arg_parser.add_argument("file_path", help="Path to the JSON file to parse")
        args = arg_parser.parse_args()
        self.run_parser(args.file_path)

    def parse_json_file(self, file_path):
        tokens = self.lexer.tokenize(file_path)
        ast = self.parser.parse(tokens)
        if ast:
            return sys.exit(0)
        else:
            return sys.exit(1)

    def run_parser(self, file_path):
        self.parse_json_file(file_path)


if __name__ == '__main__':
    parser = JSONParser()
