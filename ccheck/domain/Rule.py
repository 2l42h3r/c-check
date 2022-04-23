from dataclasses import dataclass

from ccheck.domain.token_type import TokenType


@dataclass
class Rule:
    regex: str
    type: TokenType
