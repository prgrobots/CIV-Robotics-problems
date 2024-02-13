# test_indoor.py
import unittest
from indoor import process_input

class TestIndoorProgram(unittest.TestCase):

    def test_lowercase_conversion(self):
        input_str = "Hello World!"
        expected_output = "hello world!"
        result = process_input(input_str)
        self.assertEqual(result, expected_output)

    def test_empty_input(self):
        input_str = " "
        expected_output = " "
        result = process_input(input_str)
        self.assertEqual(result, expected_output)

    def test_whitespace_input(self):
        input_str = "   Python   "
        expected_output = "   python   "
        result = process_input(input_str)
        self.assertEqual(result, expected_output)

    def test_punctuation_input(self):
        input_str = "Testing, one, two, three!"
        expected_output = "testing, one, two, three!"
        result = process_input(input_str)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
