# test_playback.py
import unittest
from playback import process_input

class TestPlaybackProgram(unittest.TestCase):

    def test_space_replacement(self):
        input_str = "Hello World!"
        expected_output = "Hello...World!"
        result = process_input(input_str)
        self.assertEqual(result, expected_output)

    def test_empty_input(self):
        input_str = ""
        expected_output = ""
        result = process_input(input_str)
        self.assertEqual(result, expected_output)

    def test_multiple_spaces(self):
        input_str = "   Python   is   fun   "
        expected_output = "...Python...is...fun..."
        result = process_input(input_str)
        self.assertEqual(result, expected_output)

    def test_no_space_input(self):
        input_str = "NoSpacesHere"
        expected_output = "NoSpacesHere"
        result = process_input(input_str)
        self.assertEqual(result, expected_output)

    def test_unicode_input(self):
        input_str = "Café au lait"
        expected_output = "Café...au...lait"
        result = process_input(input_str)
        self.assertEqual(result, expected_output)

    def test_special_characters_input(self):
        input_str = "!@#$%^&*()"
        expected_output = "!@#$%^&*()"
        result = process_input(input_str)
        self.assertEqual(result, expected_output)

    def test_numeric_input(self):
        input_str = "123 456"
        expected_output = "123...456"
        result = process_input(input_str)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
