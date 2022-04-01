from dataclasses import dataclass

from TokenType import TokenType


@dataclass
class Token:
    type: TokenType
    content: str
