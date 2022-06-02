import os
from ccheck.config import Config
from ccheck.domain.token import Token
from ccheck.domain.token_type import TokenType
from ccheck.services.tokenizer import TokenizerService

expected = [
    Token(TokenType.DIRECTIVE, content="#include"),
    Token(TokenType.WHITESPACE, content=" "),
    Token(TokenType.QUOTE, content='"stdio.h"'),
    Token(TokenType.WHITESPACE, content="\n"),
    Token(TokenType.DIRECTIVE, content="#include"),
    Token(TokenType.WHITESPACE, content=" "),
    Token(TokenType.QUOTE, content='"stdlib.h"'),
    Token(TokenType.WHITESPACE, content="\n\n"),
    Token(TokenType.IDENTIFIER, content="int"),
    Token(TokenType.WHITESPACE, content=" "),
    Token(TokenType.IDENTIFIER, content="main"),
    Token(TokenType.OPEN_PAREN, content="("),
    Token(TokenType.IDENTIFIER, content="int"),
    Token(TokenType.WHITESPACE, content=" "),
    Token(TokenType.IDENTIFIER, content="argc"),
    Token(TokenType.OPERATOR, content=","),
    Token(TokenType.WHITESPACE, content=" "),
    Token(TokenType.IDENTIFIER, content="char"),
    Token(TokenType.WHITESPACE, content=" "),
    Token(TokenType.OPERATOR, content="**"),
    Token(TokenType.IDENTIFIER, content="argv"),
    Token(TokenType.CLOSE_PAREN, content=")"),
    Token(TokenType.WHITESPACE, content=" "),
    Token(TokenType.OPEN_CURLY, content="{"),
    Token(TokenType.WHITESPACE, content="\n    "),
    Token(TokenType.IDENTIFIER, content="printf"),
    Token(TokenType.OPEN_PAREN, content="("),
    Token(TokenType.QUOTE, content='"%d\\n"'),
    Token(TokenType.OPERATOR, content=","),
    Token(TokenType.WHITESPACE, content=" "),
    Token(TokenType.IDENTIFIER, content="foo"),
    Token(TokenType.OPEN_PAREN, content="("),
    Token(TokenType.IDENTIFIER, content="atoi"),
    Token(TokenType.OPEN_PAREN, content="("),
    Token(TokenType.IDENTIFIER, content="argv"),
    Token(TokenType.OPEN_SQUARE, content="["),
    Token(TokenType.NUMBER, content="1"),
    Token(TokenType.CLOSE_SQUARE, content="]"),
    Token(TokenType.CLOSE_PAREN, content=")"),
    Token(TokenType.CLOSE_PAREN, content=")"),
    Token(TokenType.CLOSE_PAREN, content=")"),
    Token(TokenType.OPERATOR, content=";"),
    Token(TokenType.WHITESPACE, content="\n    "),
    Token(TokenType.IDENTIFIER, content="float"),
    Token(TokenType.WHITESPACE, content=" "),
    Token(TokenType.IDENTIFIER, content="c"),
    Token(TokenType.WHITESPACE, content=" "),
    Token(TokenType.OPERATOR, content="="),
    Token(TokenType.WHITESPACE, content=" "),
    Token(TokenType.NUMBER, content="5"),
    Token(TokenType.OPERATOR, content=";"),
    Token(TokenType.WHITESPACE, content="\n    "),
    Token(TokenType.IDENTIFIER, content="float"),
    Token(TokenType.WHITESPACE, content=" "),
    Token(TokenType.IDENTIFIER, content="b"),
    Token(TokenType.OPERATOR, content="="),
    Token(TokenType.IDENTIFIER, content="c"),
    Token(TokenType.OPERATOR, content="+"),
    Token(TokenType.NUMBER, content="2"),
    Token(TokenType.OPERATOR, content=";"),
    Token(TokenType.WHITESPACE, content="\n    "),
    Token(TokenType.IDENTIFIER, content="return"),
    Token(TokenType.WHITESPACE, content=" "),
    Token(TokenType.NUMBER, content="0"),
    Token(TokenType.OPERATOR, content=";"),
    Token(TokenType.WHITESPACE, content="\n"),
    Token(TokenType.CLOSE_CURLY, content="}"),
]


def test_tokenizer():
    tokenizer = TokenizerService(Config())

    file = "tokenizer_test_fixture.c"

    with open(
        os.path.join(os.path.dirname(__file__), file), "r", encoding="utf8"
    ) as fixture:
        actual = tokenizer.tokenize(fixture.read())

        print(*actual, sep="\n")

        assert len(actual) == len(expected)
        assert all(a == b for a, b in zip(actual, expected))
