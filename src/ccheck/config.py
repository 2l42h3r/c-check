from typing import List, TypedDict
import re

from ccheck.domain.rule import Rule
from ccheck.domain.token_type import TokenType
from ccheck.domain.exercise_type import ExerciseType


class Config:
    class ExerciseDict(TypedDict):
        exercise: ExerciseType
        name: str

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
        Rule(
            re.compile(
                r"^([-<>~!%^&*\/+=?|.,:;]|->|<<|>>|\*\*|\|\||&&|--|\+\+|[-+*|&%\/=]=)$"
            ),
            TokenType.OPERATOR,
        ),
        Rule(re.compile(r"^([_A-Za-z]\w*)$"), TokenType.IDENTIFIER),
        Rule(re.compile(r"^[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$"), TokenType.NUMBER),
        Rule(re.compile(r"^(\s+)$"), TokenType.WHITESPACE),
        Rule(re.compile(r"^\\\n?$"), TokenType.LINE_CONTINUE),
    ]

    exercise_config: List[ExerciseDict] = [
        {
            "name": "Definiowanie zmiennych",
            "exercise": ExerciseType.VARIABLE_DECLARATION,
        },
        {
            "name": "Zapis konstrukcji warunkowych if",
            "exercise": ExerciseType.IF_STATEMENT,
        },
        {
            "name": "Zapis konstrukcji warunkowych switch",
            "exercise": ExerciseType.SWITCH_STATEMENT,
        },
        {"name": "Definiowanie pętli for", "exercise": ExerciseType.FOR_LOOP_STATEMENT},
        {
            "name": "Definiowanie pętli do...while",
            "exercise": ExerciseType.DO_WHILE_LOOP_STATEMENT,
        },
        {
            "name": "Definiowanie tablic statycznych",
            "exercise": ExerciseType.STATIC_ARRAY_DECLARATION,
        },
        {
            "name": "Definiowanie tablic dynamicznych (wskaźniki)",
            "exercise": ExerciseType.VLA_POINTER_DECLARATION,
        },
        {"name": "Definicja funkcji", "exercise": ExerciseType.FUNCTION_DEFINITION},
    ]
