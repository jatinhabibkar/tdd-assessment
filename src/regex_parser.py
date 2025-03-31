#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.
from src.custom_exception.custom_exception import InvalidUserInputException
#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.
from src.utility.string_parser_interface import IStringParserInterface

COMMA_DELIMITER = ","


class RegexParser(IStringParserInterface):
    """
    RegexParser class use regex to parse string input
    """

    def parse(self, input_string: str) -> list[int]:
        """
        Parses input string using regex and returns a list of integers.

        :param input_string: Input string containing numbers separated by delimiters.
        :return: A list of integers parsed from the input string.
        :raises InvalidUserInputException: If the input string contains invalid characters (e.g., letters or symbols other than delimiters).

        Example:
            >>> parser = RegexParser()
            >>> parser.parse("1,2,3")
            [1, 2, 3]
            >>> parser.parse("1,2,3a,4")
            InvalidUserInputException: Invalid input: 3a is not a number
        """
        if input_string == "":
            return [0]

        numbers_list_string_elements = input_string.split(COMMA_DELIMITER)
        numbers_list = []
        for number in numbers_list_string_elements:
            if number.isdigit():
                numbers_list.append(int(number))
            else:
                raise InvalidUserInputException()
        return numbers_list
