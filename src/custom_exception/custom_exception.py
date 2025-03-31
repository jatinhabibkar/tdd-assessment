#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.

class InvalidUserInputException(Exception):
    """
    If the user provide invalid string as per the given constrains throw InvalidUserInputException
    """
    def __init__(self, message: str = "Invalid input provided"):
        """
        InvalidUserInputException takes message as input parameter to specify why the input is invalid
        :param message: default message set to "Invalid input provided"
        """
        super().__init__(message)

class NegativeNumberInputException(Exception):
    """
    If the user provides valid string with negative numbers in the string throw NegativeNumberInputException
    """
    def __init__(self, numbers_list):
        """
        NegativeNumberInputException takes list of number as input parameter
        :param numbers_list: list of numbers
        """
        super().__init__(f"Negative numbers not allowed {numbers_list}")
