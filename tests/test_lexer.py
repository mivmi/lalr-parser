import pytest
from parser import errors
from examples.math import MathLexer

EOF = ('$EOF', None)

def unpack_tokens(tokens):
    result = []
    for token in tokens:
        result.append((token.name, token.value))

    return result


@pytest.fixture
def maker():
    def wrapper(content: str):
        return MathLexer(content)
    return wrapper


def test_results(maker):
    lexer = maker('2 + 3')
    tokens = unpack_tokens(lexer.tokenize())

    expected_tokens = [
        ('NUM', '2'),
        ('ADD', '+'),
        ('NUM', '3'),
        EOF
    ]

    assert tokens == expected_tokens

def test_long_token(maker):
    lexer = maker('123456 + 7890')
    tokens = unpack_tokens(lexer.tokenize())

    expected_tokens = [
        ('NUM', '123456'),
        ('ADD', '+'),
        ('NUM', '7890'),
        EOF
    ]

    assert tokens == expected_tokens

def test_invalid_characters(maker):
    lexer = maker('2 & 3')
    with pytest.raises(errors.LexerError):
        lexer.tokenize()
