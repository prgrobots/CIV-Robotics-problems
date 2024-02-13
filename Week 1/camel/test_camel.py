# test_camel.py
import unittest
from camel import camel_to_snake

class TestCamelToSnakeConversion(unittest.TestCase):

    def test_simple_conversion(self):
        camel_case = "simpleVariableName"
        expected_snake_case = "simple_variable_name"
        result = camel_to_snake(camel_case)
        self.assertEqual(result, expected_snake_case)

    def test_multiple_words_conversion(self):
        camel_case = "someVariableNameHere"
        expected_snake_case = "some_variable_name_here"
        result = camel_to_snake(camel_case)
        self.assertEqual(result, expected_snake_case)

    def test_already_snake_case(self):
        camel_case = "snake_case_name"
        expected_snake_case = "snake_case_name"
        result = camel_to_snake(camel_case)
        self.assertEqual(result, expected_snake_case)

    def test_single_letter_words_conversion(self):
        camel_case = "aVariableB"
        expected_snake_case = "a_variable_b"
        result = camel_to_snake(camel_case)
        self.assertEqual(result, expected_snake_case)

if __name__ == '__main__':
    unittest.main()
