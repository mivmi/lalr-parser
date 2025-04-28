# lalr-parser

> A lightweight LALR(1) parser and lexer framework for Python

---

## Project Overview

This project provides a simple yet powerful framework for building parsers and lexers in Python.  
It is designed with LALR(1) parsing techniques and an optimized lexical analyzer, aiming for high performance and extensibility.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mivmi/lalr-parser.git
cd lalr-parser
pip install -e .
```

## Usage Example

### Lexer
```python
from parser.lexer import BaseLexer, token


class MathLexer(BaseLexer):
    ADD = '+'
    MINUS = '-'
    MULTIPLY = '*'
    DIVISION = '/'
    
    OPEN_PAR = '('
    CLOSE_PAR = ')'

    # ignore space
    @token('WS', ignore=True)
    def ws_handler(self, value: str):
        if value.isspace():
            return value

    # parse number
    @token('NUM')
    def number_handler(self, value: str):
        if value.isdigit():
            buffer = value
            for next_char in self.iter():
                if not next_char.isdigit():
                    self.set_position(-1)
                    break

                buffer += next_char

            return buffer
```

### Parser

```python
from parser import BaseParser, grammar

class MathParser(BaseParser):
    LEXER = MathLexer
    START = 'expr'
    
    
    @grammar('expr (`ADD` | `MINUS`) term', name='expr')
    def expr(self, expr, op, term):
        return {'_': op.name.lower(), 'left': expr, 'right': term}

    @grammar('term', name='expr')
    def term_to_expr(self, term):
        return term
    
    @grammar('term (`MULTIPLY` | `DIVISION`) factor', name='term')
    def term(self, term, op, factor):
        return {'_': op.name.lower(), 'left': term, 'right': factor}

    @grammar('factor', name='term')
    def factor_to_term(self, factor):
        return factor

    @grammar('`OPEN_PAR`! expr `CLOSE_PAR`!', name='factor')
    def factor(self, expr):
        return expr

    @grammar('`NUM`', name='factor')
    def num_to_factor(self, num):
        return int(num.value)

```

# Parsing

```python

parser = MathParser()
tree = parser.parse("3 + (4 * 5)")
print(tree)

```
```json
{
   "_": "add",
   "left": 3,
   "right": {
      "_": "multiply",
      "left": 4,
      "right": 5
   }
}

```