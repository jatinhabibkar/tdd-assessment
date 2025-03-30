#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.

import logging
import unittest

from src.string_parser import StringCalculator

# Configure logger
# Adding log time to info level
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        logger.info("initialize StringCalculator")
        self.calculator = StringCalculator()

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calculator.add(""), 0, "Expected 0 for an empty string input")

    def test_1_5_comma_separate_string_return_6(self):
        self.assertEqual(self.calculator.add("1,5"), 6, "Expected 6 for an '1,5' string input")


if __name__ == "__main__":
    unittest.main()
