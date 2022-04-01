from dataclasses import dataclass

from TokenType import TokenType


@dataclass
class Rule:
    regex: str
    type: TokenType
