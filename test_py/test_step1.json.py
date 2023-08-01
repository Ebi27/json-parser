import unittest
import sys

from cc_json import json_parser
# Add the 'json-parser' directory to the sys.path
sys.path.append("C:/tmp/json-parser")


class TestJsonParser(unittest.TestCase):
    def test_valid_json(self):
        file_path = 'tests/step1/valid.json'
        exit_code = json_parser.parse_json_file(file_path)
        self.assertEqual(exit_code, 0, f"Expected exit code 0 for valid JSON file: {file_path}")


if __name__ == '__main__':
    unittest.main()
