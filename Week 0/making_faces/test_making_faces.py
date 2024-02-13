# test_faces.py
import unittest
from faces import convert

class TestFacesConversion(unittest.TestCase):

    def test_happy_face_conversion(self):
        input_text = "Hello :)"
        expected_output = "Hello 🙂"
        result = convert(input_text)
        self.assertEqual(result, expected_output)

    def test_sad_face_conversion(self):
        input_text = "This is sad :("
        expected_output = "This is sad 🙁"
        result = convert(input_text)
        self.assertEqual(result, expected_output)

    def test_mixed_faces_conversion(self):
        input_text = "Happy :) and sad :("
        expected_output = "Happy 🙂 and sad 🙁"
        result = convert(input_text)
        self.assertEqual(result, expected_output)

    def test_no_conversion_needed(self):
        input_text = "No emoticons here!"
        expected_output = "No emoticons here!"
        result = convert(input_text)
        self.assertEqual(result, expected_output)

    def test_empty_input(self):
        input_text = ""
        expected_output = ""
        result = convert(input_text)
        self.assertEqual(result, expected_output)

    def test_unicode_emoticons(self):
        input_text = "Unicode emoticons 😊 and 😢"
        expected_output = "Unicode emoticons 😊 and 😢"
        result = convert(input_text)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
