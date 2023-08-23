import subprocess
import sys
import unittest
from cc_json import json_parser

sys.path.append('/json-parser')


class TestJsonParser(unittest.TestCase):
    def test_invalid_json(self):
        file_path = './tests/step1/invalid.json'
        expected_output = "Invalid\n"
        expected_exit_code = 1

        command = ["python", "/cc_json/json_parser_script.py", file_path]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Actual Exit Code:", result.returncode)
        print("Captured Output:", result.stdout)

        self.assertEqual(result.returncode, expected_exit_code)
        self.assertEqual(result.stdout, expected_output)


if __name__ == '__main__':
    unittest.main()
