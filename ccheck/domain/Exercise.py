from abc import ABC, abstractmethod
from typing import List

from Token import Token
from ValidationError import ValidationError


class Exercise(ABC):
    @abstractmethod
    def validate(self, tokens: List[Token]) -> List[ValidationError]:
        pass
