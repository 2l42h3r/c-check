"""Functions aiding validations"""

from typing import List

from ccheck.domain.token import Token
from ccheck.domain.token_type import TokenType


def remove_additional_whitespace(array: List[Token]) -> List[Token]:
    """Return array of tokens with every sequential whitespace concatinated into one"""
    new_array: List[Token] = []
    for token in array:
        if token.type != TokenType.WHITESPACE or new_array[-1] != TokenType.WHITESPACE:
            new_array.append(token)
    return new_array


def trim_whitespace(array: List[Token]) -> List[Token]:
    """(IMPURE) Remove starting and ending whitespace tokens if they exist"""
    if array[0] is not None and array[0].type == TokenType.WHITESPACE:
        del array[0]
    if array[-1] is not None and array[-1].type == TokenType.WHITESPACE:
        del array[-1]
    return array


def remove_whitespace_tokens(array: List[Token]) -> List[Token]:
    """Remove all whitespace tokens (for checks where whitespaces do not matter)"""
    return list(filter(lambda t: t.type != TokenType.WHITESPACE, array.copy()))


def prepare_token_list(array: List[Token]) -> List[Token]:
    """Return fully cleaned and prepared token list"""
    return trim_whitespace(remove_additional_whitespace(array))
