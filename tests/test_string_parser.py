#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.

import unittest

from src.custom_exception.custom_exception import InvalidInputException
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

    def test_invalid_string_1a23_throw_exception(self):
        with self.assertRaises(InvalidInputException):
            self.calculator.add("1a,2,3")


if __name__ == "__main__":
    unittest.main()
