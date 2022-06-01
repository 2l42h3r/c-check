from ccheck.domain.token import Token
from typing import List, TypeVar, Optional, Union

from ccheck.domain.token_type import TokenType

T = TypeVar("T")


def intersperse(array: List[T], item: T) -> List[T]:
    result = [item] * (len(array) * 2 - 1)
    result[0::2] = array
    return result


def check_for_ordered_subarray(array: List[T], subarray: List[T]) -> bool:
    match = False

    try:
        for masterIndex, masterElement in enumerate(array):
            if masterElement == subarray[0]:
                match = True
                for subIndex, subElement in enumerate(subarray):
                    if array[masterIndex + subIndex] != subElement:
                        match = False
    except IndexError:
        return False
    return match


def filter_out_none(array: List[Optional[T]]) -> List[T]:
    return list(filter(lambda i: i is not None, array))


class ValidationUtilsService:
    def __remove_additional_whitespace(self, array: List[Token]) -> List[Token]:
        new_array: List[Token] = []
        for el in array:
            if el.type != TokenType.WHITESPACE or new_array[-1] != TokenType.WHITESPACE:
                new_array.append(el)
        return new_array

    def __trim_whitespace(self, array: List[Token]) -> List[Token]:
        if array[0] is not None and array[0].type == TokenType.WHITESPACE:
            del array[0]
        if array[-1] is not None and array[-1].type == TokenType.WHITESPACE:
            del array[-1]
        return array

    def prepare_token_list(self, array: List[Token]) -> List[Token]:
        return self.__trim_whitespace(self.__remove_additional_whitespace(array))
