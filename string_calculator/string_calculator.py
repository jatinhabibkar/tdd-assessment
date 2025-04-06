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

        delimiter = [",", "\n"]

        if input_string.startswith("//"):
            match = re.match(r"^//(.+)\n([\s\S]*)$", input_string)
            if match:
                delimiter_section, input_string = match.groups()
                custom_delimiters = re.findall(r"\[(.*?)\]", delimiter_section)
                if custom_delimiters:
                    delimiter = custom_delimiters
                else:
                    delimiter = [delimiter_section]
                delimiter.append("\n")

        delimiter_pattern = "|".join(map(re.escape, delimiter))

        list_of_number_in_string_format = re.split(delimiter_pattern, input_string)
        list_of_number = []
        negatives = []
        for element in list_of_number_in_string_format:
            element_integer_format: int = int(element)
            if element_integer_format > 1000:
                continue
            if element_integer_format < 0:
                negatives.append(element)
            list_of_number.append(int(element_integer_format))

        if negatives:
            raise NegativeNumberInputException(negatives)

        return sum(list_of_number)
