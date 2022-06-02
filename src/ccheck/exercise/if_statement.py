import secrets
import string
from typing import List, Literal, Optional
from ccheck.domain.token_type import TokenType

from ccheck.domain.validation_error import ValidationError
from ccheck.domain.token import Token
from ccheck.domain.exercise.exercise import Exercise
from ccheck.utils.arrays import check_for_ordered_subarray, filter_out_none, flatten
from ccheck.utils.validation import remove_whitespace_tokens


class IfStatementExercise(Exercise):
    def __init__(self) -> None:
        self.__generate()

    __variable_one: str
    __variable_two: str
    __condition: Literal["gt", "lt"]
    __validated: List[Token] = []

    def __generate(self) -> None:
        self.__variable_one = secrets.choice(string.ascii_lowercase)
        self.__variable_two = secrets.choice(string.ascii_lowercase)
        self.__condition = secrets.choice(["gt", "lt"])

    def get_description(self) -> str:
        return (
            "Zapisz jednolinijkową instrukcję warunkową if, w której sprawdzisz, czy zmienna '"
            + self.__variable_one
            + "' jest "
            + ("większa" if self.__condition == "gt" else "mniejsza")
            + " od zmiennej '"
            + self.__variable_two
            + "'."
        )

    def __validate_if_statement_begin(
        self, tokens: List[Token]
    ) -> Optional[ValidationError]:
        new_tokens = [
            Token(TokenType.IDENTIFIER, "if"),
            Token(TokenType.OPEN_PAREN, "("),
        ]
        if check_for_ordered_subarray(
            remove_whitespace_tokens(tokens), flatten([self.__validated, new_tokens])
        ):
            self.__validated = self.__validated + new_tokens
            return None
        return ValidationError("Błędnie zapisana konstrukcja if!")

    def __get_valid_comparison_operator_token(self) -> Token:
        return Token(TokenType.OPERATOR, (">" if self.__condition == "gt" else "<"))

    def __get_valid_reverse_comparison_operator_token(self) -> Token:
        return Token(TokenType.OPERATOR, ("<" if self.__condition == "gt" else ">"))

    def __validate_condition(self, tokens: List[Token]) -> Optional[ValidationError]:
        variable_one_token = Token(TokenType.IDENTIFIER, self.__variable_one)
        variable_two_token = Token(TokenType.IDENTIFIER, self.__variable_two)
        new_tokens = [
            variable_one_token,
            self.__get_valid_comparison_operator_token(),
            variable_two_token,
        ]
        new_tokens_reverse = [
            variable_two_token,
            self.__get_valid_reverse_comparison_operator_token(),
            variable_one_token,
        ]
        is_ordered = check_for_ordered_subarray(
            remove_whitespace_tokens(tokens), flatten([self.__validated, new_tokens])
        )
        if is_ordered or check_for_ordered_subarray(
            remove_whitespace_tokens(tokens),
            flatten([self.__validated, new_tokens_reverse]),
        ):
            self.__validated = self.__validated + (
                new_tokens if is_ordered else new_tokens_reverse
            )
            return None
        return ValidationError("Błędnie zapisany warunek!")

    def __validate_if_statement_end(
        self, tokens: List[Token]
    ) -> Optional[ValidationError]:
        new_tokens = [Token(TokenType.CLOSE_PAREN, ")")]
        if check_for_ordered_subarray(
            remove_whitespace_tokens(tokens), flatten([self.__validated, new_tokens])
        ):
            self.__validated = self.__validated + new_tokens
            return None
        return ValidationError(
            "Błędnie zapisana konstrukcja if! (brak zamknięcia nawiasu)"
        )

    def validate(self, tokens: List[Token]) -> List[ValidationError]:
        return filter_out_none(
            [
                self.__validate_if_statement_begin(tokens),
                self.__validate_condition(tokens),
                self.__validate_if_statement_end(tokens),
            ]
        )
