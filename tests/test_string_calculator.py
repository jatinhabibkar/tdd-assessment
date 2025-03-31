#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.

import unittest

from string_calculator.string_calculator import StringCalculator

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_input_case(self):
        self.assertEqual(0,self.calculator.add(None), "Expected 0 for an None input")

    def test_empty_string_returns_zero(self):
        self.assertEqual(0,self.calculator.add(""), "Expected 0 for an empty string input")

    def test_one_number_case_return_sum(self):
        self.assertEqual(1,self.calculator.add("1"), "Expected 1 for an '1' string input")

    def test_two_number_case_return_sum(self):
        self.assertEqual(3,self.calculator.add("1,2"), "Expected 3 for an '1,2' string input")

    def test_n_number_case_return_sum(self):
        self.assertEqual(40,self.calculator.add("8,7,10,13,1,1"), "Expected 40 for an '8,7,10,13,1,1' string input")

    def test_to_handle_new_line_instead_of_comma(self):
        self.assertEqual(6,self.calculator.add("1\n2,3"),"Expected 6 for an '1\n2,3' string input")

    def test_support_for_custom_delimiter(self):
        self.assertEqual(3,self.calculator.add("//;\n1;2"),"Expected 3 for an '//;\n1;2' string input")

    def test_support_for_custom_delimiter_with_new_line_as_delimiter(self):
        self.assertEqual( 7,self.calculator.add("//;\n1;2\n4"), "Expected 7 for an '//;\n1;2\n4' string input")

if __name__ == '__main__':
    unittest.main()
