#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.
import re

from string_calculator.custom_exception import NegativeNumberInputException

DEFAULT_DELIMITERS = [",", "\n"]


def create_regex_pattern(delimiters: [str]) -> str:
    # delimiter1|delimiter2|delimiter3
    return "|".join(map(re.escape, delimiters))


class StringCalculator:
    def add(self, input_string: str) -> int:
        if not input_string:
            return 0

        delimiters: [str] = DEFAULT_DELIMITERS
        input_string_to_process: str = input_string
        # overwrite the input_string_to_process and delimiters if custom delimiter is passed
        if input_string_to_process.startswith("//"):
            match = re.match(r"^//(.+)\n([\s\S]*)$", input_string_to_process)
            if match:
                delimiter_section, input_string_to_process = match.groups()
                custom_delimiters = re.findall(r"\[(.*?)\]", delimiter_section)
                if custom_delimiters:
                    delimiters = custom_delimiters
                else:
                    delimiters = [delimiter_section]
                delimiters.append("\n")

        list_of_numbers_from_input_string_section: [str] = re.split(create_regex_pattern(delimiters),
                                                                    input_string_to_process)
        list_of_numbers: [int] = []
        negative_numbers: [int] = []
        for element in list_of_numbers_from_input_string_section:
            number: int = int(element)
            if number > 1000:
                continue
            if number < 0:
                negative_numbers.append(element)
            list_of_numbers.append(number)

        if negative_numbers:
            raise NegativeNumberInputException(negative_numbers)

        return sum(list_of_numbers)
