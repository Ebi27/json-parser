import unittest
import sys
from cc_json import json_parser

sys.path.append("/")


class TestJsonParser(unittest.TestCase):
    def test_valid_json(self):
        file_path = 'tests/step1/valid.json'
        exit_code = json_parser.parse_json_file(file_path)  # Use json_parser here
        self.assertEqual(exit_code, 0, f"Expected exit code 0 for valid JSON file: {file_path}")

    def test_invalid_json(self):
        file_path = 'tests/step1/invalid.json'
        exit_code = json_parser.parse_json_file(file_path)  # Use json_parser here
        self.assertEqual(exit_code, 1, f"Expected exit code 1 for invalid JSON file: {file_path}")


if __name__ == '__main__':
    unittest.main()
