import random
from typing import List

from ccheck.domain.validation_error import ValidationError
from ccheck.domain.token import Token
from ccheck.domain.exercise.exercise import Exercise


class VariableDeclarationExercise(Exercise):
    __variable_types: List[str] = [
        "char",
        "unsigned char",
        "short",
        "unsigned short",
        "int",
        "unsigned int",
        "long",
        "unsigned long",
        "float",
        "double",
        "long double",
    ]
    __variable_name = "var"

    __picked_variable_type: str

    def __init__(self) -> None:
        self.__generate()

    def __generate(self) -> None:
        self.__picked_variable_type = random.choice(self.__variable_types)

    def get_description(self) -> str:
        return (
            'Zdefiniuj zmienną o nazwie "'
            + self.__variable_name
            + '" typu '
            + self.__picked_variable_type
            + ". Nie inicjalizuj zmiennej."
        )

    def validate(self, tokens: List[Token]) -> List[ValidationError]:
        return []
