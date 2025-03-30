#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.
from src.custom_exception.custom_exception import InvalidInputException
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
        parse method takes input as string and return list of number

        :exception if the user provide invalid string it will throw exception
        for eg: 1,2,3a,4 -> 3a is not integer
        """
        if input_string == "":
            return [0]

        numbers_list_string_elements = input_string.split(COMMA_DELIMITER)
        numbers_list = []
        for number in numbers_list_string_elements:
            if number.isnumeric():
                numbers_list.append(int(number))
            else:
                raise InvalidInputException()
        return numbers_list
