from typing import List
import re

from ccheck.domain.Rule import Rule
from ccheck.domain.token_type import TokenType

class Config:
    rule_config: List[Rule] = [
        Rule(re.compile(r"^\/\*([^*]|\*(?!\/))*\*\/$"), TokenType.AREA_COMMENT),
        Rule(re.compile(r"^\/\*([^*]|\*(?!\/))*\*?$"), TokenType.AREA_COMMENT_CONTINUE),
        Rule(re.compile(r"^\/\/[^\n]*$"), TokenType.LINE_COMMENT),
        Rule(re.compile(r"^\"([^\"\n]|\\\")*\"?$"), TokenType.QUOTE),
        Rule(re.compile(r"^'(\\?[^'\n]|\\')'?$"), TokenType.CHAR),
        Rule(re.compile(r"^'[^']*$"), TokenType.CHAR_CONTINUE),
        Rule(re.compile(r"^#(\S*)$"), TokenType.DIRECTIVE),
        Rule(re.compile(r"^\($"), TokenType.OPEN_PAREN),
        Rule(re.compile(r"^\)$"), TokenType.CLOSE_PAREN),
        Rule(re.compile(r"^\[$"), TokenType.OPEN_SQUARE),
        Rule(re.compile(r"^\]$"), TokenType.CLOSE_SQUARE),
        Rule(re.compile(r"^{$"), TokenType.OPEN_CURLY),
        Rule(re.compile(r"^}$"), TokenType.CLOSE_CURLY),
        Rule(re.compile(r"^([-<>~!%^&*\/+=?|.,:;]|->|<<|>>|\*\*|\|\||&&|--|\+\+|[-+*|&%\/=]=)$"), TokenType.OPERATOR),
        Rule(re.compile(r"^([_A-Za-z]\w*)$"), TokenType.IDENTIFIER),
        Rule(re.compile(r"^[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$"), TokenType.NUMBER),
        Rule(re.compile(r"^(\s+)$"), TokenType.WHITESPACE),
        Rule(re.compile(r"^\\\n?$"), TokenType.LINE_CONTINUE),
    ]
