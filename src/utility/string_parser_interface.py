#  Copyright (c) 2025. Jatin Habibkar
#  This code is licensed under the MIT License.
from abc import abstractmethod, ABC


class IStringParserInterface(ABC):
    @abstractmethod
    def parse(self, string: str) -> list[int]:
        pass
