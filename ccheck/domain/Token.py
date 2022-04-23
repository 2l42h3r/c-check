from dataclasses import dataclass

from ccheck.domain.token_type import TokenType


@dataclass
class Token:
    type: TokenType
    content: str
