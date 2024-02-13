# test_twttr.py
import unittest
from twttr import remove_vowels

class TestTwttrProgram(unittest.TestCase):

    def test_remove_vowels(self):
        input_str = "Hello World!"
        expected_output = "Hll Wrld!"
        result = remove_vowels(input_str)
        self.assertEqual(result, expected_output)

    def test_empty_input(self):
        input_str = ""
        expected_output = ""
        result = remove_vowels(input_str)
        self.assertEqual(result, expected_output)

    def test_only_vowels_input(self):
        input_str = "AEIOUaeiou"
        expected_output = ""
        result = remove_vowels(input_str)
        self.assertEqual(result, expected_output)

    def test_no_vowels_input(self):
        input_str = "Pythn"
        expected_output = "Pythn"
        result = remove_vowels(input_str)
        self.assertEqual(result, expected_output)

    def test_mixed_case_input(self):
        input_str = "ThIs Is A TeSt"
        expected_output = "Ths s  Tst"
        result = remove_vowels(input_str)
        self.assertEqual(result, expected_output)

    def test_special_characters_input(self):
        input_str = "!@#$%^&*()"
        expected_output = "!@#$%^&*()"
        result = remove_vowels(input_str)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
