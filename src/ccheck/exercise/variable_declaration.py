import itertools
import secrets
from typing import List, Optional
from ccheck.domain.token_type import TokenType

from ccheck.domain.validation_error import ValidationError
from ccheck.domain.token import Token
from ccheck.domain.exercise.exercise import Exercise
from ccheck.utils.validation_utils_service import (
    check_for_ordered_subarray,
    filter_out_none,
    intersperse,
)


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
        self.__picked_variable_type = secrets.choice(self.__variable_types)

    def get_description(self) -> str:
        return (
            'Zdefiniuj zmienną o nazwie "'
            + self.__variable_name
            + '" typu '
            + self.__picked_variable_type
            + ". Nie inicjalizuj zmiennej."
        )

    def __create_tokens_from_variable_type(self) -> List[Token]:
        return intersperse(
            list(
                map(
                    lambda word: Token(TokenType.IDENTIFIER, word),
                    self.__picked_variable_type.split(),
                )
            ),
            Token(TokenType.WHITESPACE, " "),
        )

    def __validate_variable_type(
        self, tokens: List[Token]
    ) -> Optional[ValidationError]:
        if check_for_ordered_subarray(
            tokens, self.__create_tokens_from_variable_type()
        ):
            return None
        return ValidationError("Źle określony typ zmiennej!")

    def __validate_variable_name(
        self, tokens: List[Token]
    ) -> Optional[ValidationError]:
        if check_for_ordered_subarray(
            tokens,
            list(
                itertools.chain.from_iterable(
                    [
                        self.__create_tokens_from_variable_type(),
                        [
                            Token(TokenType.WHITESPACE, " "),
                            Token(TokenType.IDENTIFIER, self.__variable_name),
                        ],
                    ]
                )
            ),
        ):
            return None
        return ValidationError("Błędna nazwa zmiennej!")

    def __validate_semicolon(self, tokens: List[Token]) -> Optional[ValidationError]:
        if check_for_ordered_subarray(
            tokens,
            list(
                itertools.chain.from_iterable(
                    [
                        self.__create_tokens_from_variable_type(),
                        [
                            Token(TokenType.WHITESPACE, " "),
                            Token(TokenType.IDENTIFIER, self.__variable_name),
                            Token(TokenType.OPERATOR, ";"),
                        ],
                    ]
                )
            ),
        ):
            return None
        return ValidationError("Brak średnika na końcu linii.")

    def validate(self, tokens: List[Token]) -> List[ValidationError]:
        return filter_out_none(
            [
                self.__validate_variable_type(tokens),
                self.__validate_variable_name(tokens),
                self.__validate_semicolon(tokens),
            ]
        )
