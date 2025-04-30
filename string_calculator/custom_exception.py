#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.

class NegativeNumberInputException(Exception):
    def __init__(self, list_of_negative_number):
        super().__init__(f"Negative numbers not allowed {','.join(list_of_negative_number)}")
