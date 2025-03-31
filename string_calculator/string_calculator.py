#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.
import re

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
                delimiter+="|\n"

        list_of_number_in_string_format = re.split(delimiter,input_string)
        sum_of_elements = 0
        for element in list_of_number_in_string_format:
            sum_of_elements += int(element)
        return sum_of_elements
