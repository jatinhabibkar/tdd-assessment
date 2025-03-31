#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.
from abc import abstractmethod, ABC


class IStringParserInterface(ABC):
    """
    you can implement underling method to create your own parser
    """
    @abstractmethod
    def parse(self, string: str) -> list[int]:
        """
        parse method helps compute user input and returns list of integers
        :param string: user input
        :return: list of integer after processing
        """
        pass
