from dataclasses import dataclass
from typing import List


@dataclass
class ValidationError:
    error_message: str
    invalid_tokens: List[int]
