from abc import ABC, abstractmethod
from typing import List

from ccheck.domain.token import Token
from ccheck.domain.validation_error import ValidationError


class Exercise(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def validate(self, tokens: List[Token]) -> List[ValidationError]:
        pass
