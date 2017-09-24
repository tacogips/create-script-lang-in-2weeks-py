import re
import string
import token

class Lexer:
    # TODO maybe miss escape char
    _token_pattern_string = r'"(' + '\\' + r'|[^"]|\n)*"'

    # not allow start with a number
    _token_symbols = r'[a-zA-Z_]\w*|' + \
        '|'.join(['==', '<=', '>=', '&&', '\\', r'\|', r'\p{P}'])

    _token_regex = re.compile('{0}(({1})|({2})|({3})|{4})?'.format(
        r'\s*',
        r'//.*',  # comment
        r'\d',   # number
        _token_pattern_string,  # string
        _token_symbols))  # symbol

    def __init__(self,reader):

        self.has_more = True
        self.tokens = []
        self.reader = reader

    def read(self):
        if (_fill_token_if_need(0)):
            return self.tokens.pop(0)
        else:
            return token.EOF


    def _fill_token_if_need(self, token_index):
        while(token_index >= len(self.tokens)):
            if(self.has_more):
                self._read_line()
            else:
                return false
        return true


    def _read_line(self):
        line =  self.reader.readline()
        if not line:
            self.has_more = false

        matched = re.match(line)
        if not matched:
            # TODO parse error


        else:
            matched.group()





print(token.EOF)
