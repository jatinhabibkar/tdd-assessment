#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.
import re

from string_calculator.custom_exception import NegativeNumberInputException


class StringCalculator:
    def add(self, input_string: str):
        if not input_string:
            return 0

        length_of_input = len(input_string)

        if length_of_input == 0:
            return 0
        if length_of_input == 1:
            return int(input_string)

        delimiter = ",|\n"

        if input_string.startswith("//"):
            match = re.match(r"^//(.+)\n([\s\S]*)$", input_string)
            if match:
                delimiter, input_string = match.groups()
                delimiter += "|\n"

        list_of_number_in_string_format = re.split(delimiter, input_string)
        list_of_number = []
        negatives = []
        for element in list_of_number_in_string_format:
            element_integer_format: int = int(element)
            if element_integer_format < 0:
                negatives.append(element)
            list_of_number.append(int(element_integer_format))

        if negatives:
            raise NegativeNumberInputException(negatives)

        return sum(list_of_number)
