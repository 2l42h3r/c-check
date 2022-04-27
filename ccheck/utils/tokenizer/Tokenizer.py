from typing import List, Optional
import re
from functools import reduce

from ccheck.domain.Rule import Rule
from ccheck.domain.Token import Token
from ccheck.config import Config

class Tokenizer:
    __rules: List[Rule] = []

    def __init__(self, rules: Optional[List[Rule]]=None) -> None:
        if rules is None:
            self.__rules = Config.rule_config
            return
        self.__rules = rules

    @staticmethod
    def __rule_matches_text_predicate_factory(text: str, rule: Rule) -> bool:
        return re.search(rule.regex, text) is not None

    def __get_matching_rule(self, text: str) -> Optional[Rule]:
        return next(
            (
                rule
                for rule in self.__rules
                if self.__rule_matches_text_predicate_factory(text, rule)
            ),
            None,
        )

    def __get_max_text_index(self, text: str) -> int:
        indexes = range(len(text))

        return next(
            (
                index
                for index in indexes
                if self.__get_matching_rule(text[0 : (index + 1)]) is None
            ),
            0,
        )

    def __partial_tokenize(self, text: str) -> List[Token]:
        length = len(text)
        if length == 0:
            return []

        max_index = self.__get_max_text_index(text)

        if max_index == 0 or max_index == length:
            return []

        match = text[0:max_index]
        rule = self.__get_matching_rule(match)

        if rule is None:
            return []

        tokens = [Token(rule.type, match)]

        tokens.extend(self.__partial_tokenize(text[max_index:length]))

        return tokens

    def tokenize(self, text: str) -> List[Token]:
        tokens = text.split()
        return reduce(lambda a,b:a+b, list(map(self.__partial_tokenize, tokens)))

    def add_rule(self, rule: Rule) -> None:
        self.__rules.append(rule)
