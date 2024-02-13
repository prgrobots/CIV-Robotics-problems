# test_tip_calculator.py
import unittest
from tip import dollars_to_float, percent_to_float, calculate_tip

class TestTipCalculator(unittest.TestCase):

    def test_dollars_to_float(self):
        input_str = "$50.00"
        expected_output = 50.0
        result = dollars_to_float(input_str)
        self.assertEqual(result, expected_output)

    def test_percent_to_float(self):
        input_str = "15%"
        expected_output = 0.15
        result = percent_to_float(input_str)
        self.assertEqual(result, expected_output)

    def test_calculate_tip(self):
        dollars = 50.0
        percent = 0.15
        expected_output = 7.5
        result = calculate_tip(dollars, percent)
        self.assertEqual(result, expected_output)

    def test_dollars_to_float_negative(self):
        input_str = "$-30.75"
        expected_output = -30.75
        result = dollars_to_float(input_str)
        self.assertEqual(result, expected_output)

    def test_percent_to_float_large(self):
        input_str = "99.99%"
        expected_output = 0.9999
        result = percent_to_float(input_str)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
