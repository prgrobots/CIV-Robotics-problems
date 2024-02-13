# test_deep.py
import unittest
from deep import answer_to_life_universe_everything

class TestDeepProgram(unittest.TestCase):

    def test_answer_42(self):
        result = answer_to_life_universe_everything("42")
        self.assertEqual(result, "Yes")

    def test_answer_forty_two(self):
        result = answer_to_life_universe_everything("forty-two")
        self.assertEqual(result, "Yes")

    def test_answer_forty_two_space(self):
        result = answer_to_life_universe_everything("forty two")
        self.assertEqual(result, "Yes")

    def test_case_insensitivity(self):
        result_upper = answer_to_life_universe_everything("FORTY-TWO")
        result_mixed = answer_to_life_universe_everything("FoRtY tWo")
        self.assertEqual(result_upper, "Yes")
        self.assertEqual(result_mixed, "Yes")

    def test_answer_no(self):
        result = answer_to_life_universe_everything("not the answer")
        self.assertEqual(result, "No")

    def test_wrap_onto_multiple_lines(self):
        user_input = "The answer is\nforty-two!"
        result = answer_to_life_universe_everything(user_input)
        self.assertEqual(result, "Yes")

if __name__ == '__main__':
    unittest.main()
