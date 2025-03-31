#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.

import unittest

from src.string_parser import StringCalculator
from src.utility import IStringParserInterface


class CustomParser(IStringParserInterface):

    def parse(self, string: str) -> list[int]:
        return [int(number) for number in string.split("|")]


class TestCaseForCustomParser(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator(CustomParser())

    def test_custom_string_parser(self):
        self.assertEqual(self.calculator.add("1|2|3|6"), 12, "Expected 12 for an '1|2|3|6' string input")


if __name__ == '__main__':
    unittest.main()
