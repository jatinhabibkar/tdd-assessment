#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.

class StringCalculator:
    def add(self, input_string):
        if not input_string:
            return 0

        length_of_input = len(input_string)

        if length_of_input == 0:
            return 0
        if length_of_input == 1:
            return int(input_string)

        list_of_number_in_string_format = input_string.split(",")
        return int(list_of_number_in_string_format[0]) + int(list_of_number_in_string_format[1])
