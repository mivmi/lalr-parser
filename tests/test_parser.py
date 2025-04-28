import pytest
from parser import parser, errors
from examples.math import MathParser

@pytest.fixture
def math_parser():
    return MathParser()

def test_result(math_parser):
    result = math_parser.parse('1 + 2')

    assert result == {
        '_': 'add',
        'left': 1,
        'right': 2
    }


def test_factor(math_parser):
    result = math_parser.parse('1 + 2 * ( 4  - 3) / 5')

    assert result == {
        '_': 'add',
        'left': 1,
        'right': {
            '_': 'division',
            'left': {
                '_': 'multiply',
                'left': 2,
                'right': {
                    '_': 'minus',
                    'left': 4,
                    'right': 3
                }
            },
            'right': 5
        }
    }

def test_invalid_characters(math_parser):
    with pytest.raises(errors.LexerError):
        math_parser.parse('2 & 3')


def test_rr_conflict_error():
    with pytest.raises(errors.RRConflictError):
        class _(parser.BaseParser):
            START = 'root'
            # root: ID
            start_id = parser.Production(
                parser.NonTerminal('root'),
                rhs=[parser.Terminal('ID')]
            )
    
            start_id2 = start_id


def test_sr_conflict_error():
    with pytest.raises(errors.SRConflictError):
        class _(parser.BaseParser):
            START = 'root'

            # root: ID
            start_id = parser.Production(
                parser.NonTerminal('root'),
                rhs=[parser.Terminal('ID')]
            )
            # root: root ID
            start_recursion = parser.Production(
                parser.NonTerminal('root'),
                rhs=[
                    parser.NonTerminal('root'),
                    parser.Terminal('ID')
                ]
            )
            # root: ID ID
            start_double_id = parser.Production(
                parser.NonTerminal('root'),
                rhs=[
                    parser.Terminal('ID'),
                    parser.Terminal('ID')
                ]
            )
            
