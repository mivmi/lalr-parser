from parser import BaseParser, grammar, lexer


class MathLexer(lexer.BaseLexer):
    ADD = '+'
    MINUS = '-'
    MULTIPLY = '*'
    DIVISION = '/'
    
    OPEN_PAR = '('
    CLOSE_PAR = ')'

    # ignore space
    @lexer.token('WS', ignore=True)
    def ws_handler(self, value: str):
        if value.isspace():
            return value

    # parse number
    @lexer.token('NUM')
    def number_handler(self, value: str):
        if value.isdigit():
            buffer = value
            for next_char in self.iter():
                if not next_char.isdigit():
                    self.set_position(-1)
                    break

                buffer += next_char

            return buffer


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


parser = MathParser()

print(parser.parse('1 + 3'))