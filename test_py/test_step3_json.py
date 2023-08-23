import unittest
import sys
from cc_json import json_parser
sys.path.append('/json-parser')


class TestJsonParser(unittest.TestCase):
    def test_valid_json(self):
        file_path = './tests/step3/valid.json'
        json_parser_instance = json_parser.JSONParser()  # Create an instance
        exit_code = json_parser_instance.parse_json_file(file_path)
        self.assertEqual(exit_code, 0, f"Expected exit code 0 for valid JSON file: {file_path}")

    def test_invalid_json(self):
        file_path = './tests/step3/invalid.json'
        json_parser_instance = json_parser.JSONParser()  # Create an instance
        exit_code = json_parser_instance.parse_json_file(file_path)
        self.assertEqual(exit_code, 1, f"Expected exit code 1 for invalid JSON file: {file_path}")


if __name__ == '__main__':
    unittest.main()
