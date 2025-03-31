#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.
from src.utility import IStringParserInterface


class StringCalculator:
    """
    A simple string calculator that takes a string of numbers separated by delimiters and returns their sum.
    """

    def __init__(self, parser: IStringParserInterface):
        self.parser = parser

    def add(self, input_string: str) -> int:
        """
        Add method taking string as input and return sum of all number after parsing the string
        """
        list_of_elements = self.parser.parse(input_string)

        sum_of_elements = sum(list_of_elements)
        return sum_of_elements
