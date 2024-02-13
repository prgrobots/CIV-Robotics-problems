# test_einstein.py
import unittest
from einstein import calculate_energy_equivalence

class TestEinsteinProgram(unittest.TestCase):

    def test_energy_equivalence(self):
        mass = 1
        expected_energy_equivalence = 9e16  # 1 kg * (3e8 m/s)^2
        result = calculate_energy_equivalence(mass)
        self.assertEqual(result, expected_energy_equivalence)

    def test_zero_mass(self):
        mass = 0
        expected_energy_equivalence = 0
        result = calculate_energy_equivalence(mass)
        self.assertEqual(result, expected_energy_equivalence)

    def test_negative_mass(self):
        mass = -2
        with self.assertRaises(ValueError):
            calculate_energy_equivalence(mass)

    def test_large_mass(self):
        mass = 1e6  # 1 million kilograms
        expected_energy_equivalence = 9e22  # 1e6 kg * (3e8 m/s)^2
        result = calculate_energy_equivalence(mass)
        self.assertEqual(result, expected_energy_equivalence)

if __name__ == '__main__':
    unittest.main()
