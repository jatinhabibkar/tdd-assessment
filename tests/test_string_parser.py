#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.

import unittest

from src.custom_exception.custom_exception import InvalidUserInputException, NegativeNumberInputException
from src.regex_parser import RegexParser
from src.string_parser import StringCalculator


# Configure logger
# Adding log time to info level

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator(RegexParser())

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calculator.add(""), 0, "Expected 0 for an empty string input")

    def test_1_5_comma_separate_string_return_6(self):
        self.assertEqual(self.calculator.add("1,5"), 6, "Expected 6 for an '1,5' string input")

    def test_invalid_string_throw_exception(self):
        with self.assertRaises(InvalidUserInputException,
                               msg="adding character with integer raise InvalidUserInputException"):
            self.calculator.add("1,2,3,78,67,10z")

    def test_invalid_string_with_trailing_comma_throw_exception(self):
        with self.assertRaises(InvalidUserInputException, msg="Trailing comma raise InvalidUserInputException"):
            self.calculator.add("1,2,3,78,67,10,")

    def test_new_line_instead_of_comma(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6, "Expected 6 for an '1,5' string input")

    def test_valid_custom_delimiter(self):
        self.assertEqual(self.calculator.add("//a\n1a2a3a4a78"), 88, "Expected 88 for input '//a\n1a2a3a4a78'")

    def test_negative_numbers(self):
        with self.assertRaises(NegativeNumberInputException, msg="Input should not contain negative numbers"):
            self.calculator.add("1,2,3,4,-19,10000")

    def test_negative_numbers_with_custom_delimiter(self):
        with self.assertRaises(NegativeNumberInputException,
                               msg="Input should not contain negative numbers with custom delimiter"):
            self.calculator.add("//;\n1;2;3;4;-19")

    def test_invalid_negative_numbers_with_custom_delimiter(self):
        with self.assertRaises(InvalidUserInputException, msg="Trailing semi colon raise InvalidUserInputException"):
            self.calculator.add("//;\n1;2;3;4;-19;")


if __name__ == "__main__":
    unittest.main()
