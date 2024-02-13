# test_nutrition.py
import unittest
from nutrition import get_fruit_calories

class TestNutrition(unittest.TestCase):

    def test_valid_fruit(self):
        result = get_fruit_calories("apple")
        self.assertEqual(result, -1)  # TO DO: Update the expected result

    def test_invalid_fruit(self):
        result = get_fruit_calories("watermelon")
        self.assertEqual(result, -1)  # TO DO: Update the expected result

    def test_case_insensitivity(self):
        result = get_fruit_calories("Orange")
        self.assertEqual(result, -1)  # TO DO: Update the expected result

    def test_unknown_input(self):
        result = get_fruit_calories("123")
        self.assertEqual(result, -1)  # TO DO: Update the expected result

    def test_empty_input(self):
        result = get_fruit_calories("")
        self.assertEqual(result, -1)  # TO DO: Update the expected result
    
    def test_multiple_words_input(self):
        result = get_fruit_calories("kiwi fruit")
        self.assertEqual(result, -1)  # TO DO: Update the expected result

if __name__ == '__main__':
    unittest.main()
