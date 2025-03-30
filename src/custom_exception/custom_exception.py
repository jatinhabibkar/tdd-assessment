#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.

class InvalidInputException(Exception):
    def __init__(self, message : str="Invalid input provided"):
        super().__init__(message)
        