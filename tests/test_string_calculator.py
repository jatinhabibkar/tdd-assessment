#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.

import unittest

from string_calculator.string_calculator import StringCalculator

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_input_case(self):
        self.assertEqual(self.calculator.add(None), 0, "Expected 0 for an None input")

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calculator.add(""), 0, "Expected 0 for an empty string input")

    def test_one_number_case_return_sum(self):
        self.assertEqual(self.calculator.add("1"), 1, "Expected 1 for an '1' string input")

    def test_two_number_case_return_sum(self):
        self.assertEqual(self.calculator.add("1,2"), 3, "Expected 3 for an '1,2' string input")

if __name__ == '__main__':
    unittest.main()
