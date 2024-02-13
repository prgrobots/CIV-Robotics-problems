# test_bank.py
import unittest
from bank import determine_greeting_cost

class TestBankProgram(unittest.TestCase):

    def test_hello_starts_with_hello(self):
        result = determine_greeting_cost("hello, world!")
        self.assertEqual(result, 0)

    def test_hello_starts_with_hello_case_insensitive(self):
        result = determine_greeting_cost("HeLLo, World!")
        self.assertEqual(result, 0)

    def test_h_starts_with_h(self):
        result = determine_greeting_cost("hi there")
        self.assertEqual(result, 20)

    def test_h_starts_with_h_case_insensitive(self):
        result = determine_greeting_cost("Hi tHeRe")
        self.assertEqual(result, 20)

    def test_other_starts_with_other(self):
        result = determine_greeting_cost("Goodbye!")
        self.assertEqual(result, 100)

    def test_leading_whitespace(self):
        result = determine_greeting_cost("     hello")
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
